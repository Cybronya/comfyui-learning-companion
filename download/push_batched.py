#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""分批推送（大包绕过代理限流 + 绕过 GitHub Push Protection）。

背景
----
代理在上传 >100MB 的 pack 时会 reset 连接（curl 55 Send failure）；
偶发 502 / CONNECT tunnel failed 瞬时错误。

**GitHub Push Protection**：库里的工作流是从 RunningHub 公开下载的，
作者把**自己的** API Key 写在节点 widget 值里（DeepSeek / 豆包 Ark 等）。
这些密钥不属于我们，但 GitHub 一律拦截 —— 命中即整批拒绝（GH013
"Push cannot contain secrets"）。密钥共 144 个唯一值 / 244 个文件，
其中 **5 个是远端尚不存在的新引入密钥**，正是被拦的那批。
解决：在**构造批次树时**对 blob 做脱敏（本地工作区文件不动，
原始数据留在本地），推给 GitHub 的版本里密钥替换成同长度占位串。

方案
----
把 base..target 的变更按体积均衡切成 N 批，为每批构造一个**累积提交**
（第 k 批提交 = base + 前 k 批文件），逐个推送到 master。
Git 每次推送只传该批新增的对象，单包从 334MB 降到 ~4MB。

关键技术点
----------
1. 用**临时索引**（GIT_INDEX_FILE）构造提交，真实索引与工作区零改动；
2. 用 `git update-index --index-info` 从**对象库**直接注入 blob 条目，
   完全不读工作区文件 —— 所以不受工作区状态影响，也极快；
3. `--index-info` 走 stdin 批量喂，绕开 Windows 命令行长度限制；
4. **断点续推按内容判定**（逐文件比对远端树与目标树的 blob），
   不依赖批次编号 —— 批次划分会随批量参数变化而变化，靠编号跳批会错位。

全部批次推完后，force push 把 target 提交放回 master
（对象已在远端，传输量接近 0），恢复单提交历史。

用法
----
  python push_batched.py <target-commit> [base-commit]
"""
import subprocess
import sys
import os
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)

# 项目内临时工作区（项目规则：不得使用 C 盘 / 系统 TEMP 做临时区）
sys.path.insert(0, str(ROOT))
from engine.tmp_workspace import TMP_ROOT

TMP_ROOT.mkdir(parents=True, exist_ok=True)

# ---- 第三方 API Key：不做任何脱敏（AGENTS.md 3.7）----
# 库里的 Key 是工作流作者在公开分享时自己写进去的，不是我们的凭据。
# 脱敏会改内容指纹 → 去重失效、学习记录与原工作流对不上。
# 遇到 GitHub Push Protection（GH013）时走 Unblock URL 放行，不改库。

TARGET_BATCH_MB = 4       # 每批目标体积
# 关键：代理（Karing）上传数据流时会周期性切断隧道 —— 只读请求（ls-remote）完全正常，
# 一旦真正传 pack 就可能断。实测 1.7MB / 8MB 单包都能推成功，说明没有硬性大小上限，
# 是节点抖动。所以用**多代理轮换 + 幂等重试**对抗，而非无限缩小批次。
# 4MB 是速度与稳定性的平衡点（实测每批 3~10s）。
MAX_FILES = 1200          # 每批文件数上限
MAX_RETRY = 20            # 每批最大重试轮次（代理会周期性抖动，需长退避）
RETRY_BASE_SLEEP = 5      # 重试退避基数（秒），指数增长

PROXIES = [
    # Karing 会随重启变动端口/进程，代理列表必须**实测**而非写死。
    # 2026-11-19 实测：3066 / 3067 可用，3057 / 3065 连不上，旧的 55725 端口已消失。
    # 每个批次按顺序逐个尝试，排在前面但不通的代理会白等 ~2s 超时，故可用优先。
    "http://127.0.0.1:3067",
    "http://127.0.0.1:3066",
    "http://127.0.0.1:55725",
    "http://127.0.0.1:3057",
    "http://127.0.0.1:3065",
    # 空串 = **直连**（不走任何代理）。
    # 2026-11-20 实测：Karing 的代理出口节点断线时，所有端口的 TLS 握手全挂，
    # 但直连 github.com 反而通（HTTP 200）—— 代理出口挂掉时，直连是唯一能走通的路径。
    # 放在最后作为兜底，前面几个代理恢复后会自动优先用代理。
    "",
]


def proxy_args(px):
    """把代理地址转成 git 的 -c 参数。

    空串表示**直连**：必须显式清空各级 proxy 配置，
    否则仓库 config 里的 http.proxy 会生效。
    """
    if not px:
        return ["-c", "http.proxy=", "-c", "https.proxy=",
                "-c", "http.https://github.com.proxy="]
    return ["-c", f"http.https://github.com.proxy={px}"]


def git(*args, env=None, stdin_data=None):
    """执行 git 命令。

    注意：stdin 必须走**二进制模式**。
    Windows 上 text=True 会把 \n 转成 \r\n，
    而 `git update-index --index-info` 的行解析器会把 \r 当成路径的一部分，
    结果全部条目被静默丢弃（stderr 报 "Ignoring path <path>"），
    写出的树等于父提交 —— 表现为"推送成功但内容没变"。
    """
    e = dict(os.environ)
    if env:
        e.update(env)
    if stdin_data is not None:
        # 已是 str 则按 UTF-8 编码为字节，不做换行转换
        data = stdin_data.encode("utf-8") if isinstance(stdin_data, str) else stdin_data
        return subprocess.run(["git", "-c", "core.quotepath=false", *args],
                              capture_output=True, env=e, input=data)
    # 无 stdin 时用**二进制**模式：
    # `git push` 的 stdout 是进度流（含 \r 回车刷新），
    # 走 text=True 会经过 Python 的 universal-newlines 解码，
    # 在代理高延迟（TLS 握手 6 秒级）下容易与管道缓冲互相等待，
    # 表现为 schannel 握手超时 —— 实测同一命令走二进制模式稳定成功。
    return subprocess.run(["git", "-c", "core.quotepath=false", *args],
                          capture_output=True, env=e)


def _text(b):
    """把子进程的字节输出解码成字符串（errors='replace' 避免乱码抛异常）。"""
    if b is None:
        return ""
    if isinstance(b, str):
        return b
    return b.decode("utf-8", errors="replace")


def out(*cmd, env=None):
    r = git(*cmd, env=env)
    return _text(r.stdout).strip()


def remote_head():
    for px in PROXIES:
        r = git(*proxy_args(px),
                "ls-remote", "origin", "refs/heads/master")
        line = _text(r.stdout).strip()
        if line:
            return line.split("\t")[0]
    return None


def is_proxy_error(err):
    """判断错误是否来自代理/传输层（而非 GitHub 的策略拒绝）。

    代理层错误的特征：连不上隧道、TLS 握手被切断、502/503。
    这类错误换代理就能解决；反之（如 GH013 策略拒绝）重试无意义。
    """
    markers = (
        "CONNECT tunnel", "502", "503", "schannel",
        "Failed to connect", "Empty reply", "SSL handshake",
        "Connection reset", "Recv failure", "Send failure",
        "early EOF", "the remote end closed",
    )
    return any(m in err for m in markers)


def push_with_retry(commit):
    """推送到 master：多代理 + 指数退避

    必须用 force：远端 master 可能停在上一次运行的批次提交上，
    与本轮批次提交不构成快进关系，普通 push 会被 [rejected]。
    这是刻意重写 master 历史（最终会 force 回 target 单提交），
    故用 --force 而非 --force-with-lease。

    判定成功的三种方式：
    1. push 返回 0；
    2. push 报错但远端已指向该提交（说明上一次重试其实成功了，
       只是响应丢失/连接重置导致本地看到失败）。
       第 2 种情况必须识别，否则会把成功误判为失败 —— 后续重试同一提交
       会被 GitHub 以 GH013「Push can not be created」拒绝，
       看起来像策略违规，其实是重复推送。
    3. push 报错且错误是「代理层」问题（CONNECT tunnel / schannel / 502）
       —— 此时**跳过该代理继续试下一个**，不要在这里 break：
       Karing 的多个端口各自独立掉线，只试第一个会白白耗尽重试轮次。
    """
    last_err = ""
    for attempt in range(1, MAX_RETRY + 1):
        for px in PROXIES:
            r = git(*proxy_args(px),
                    "push", "--force", "origin", f"{commit}:refs/heads/master")
            if r.returncode == 0:
                print(f"    推送成功 (代理 {px.rsplit(':', 1)[-1]}, 第{attempt}轮)", flush=True)
                return True
            last_err = (_text(r.stderr) + " | " + _text(r.stdout))[:300]
            # Push Protection 拒绝：重试无意义（换代理也一样），立刻中止并报详情
            if "GH013" in last_err or "Push cannot contain secrets" in last_err:
                print("\n!! 被 GitHub Push Protection 拦截 —— 该批含未脱敏的密钥。")
                print("   详情:", _text(r.stderr)[:600])
                return False
            # 关键：push 报错后查远端，若已是该提交则视为成功
            rh = remote_head()
            if rh == commit:
                print(f"    推送已生效 (远端已指向该提交, 代理 {px.rsplit(':', 1)[-1]})", flush=True)
                return True
            # 代理层错误 → 继续试下一个代理（不要 break）
            if is_proxy_error(last_err):
                continue
        if attempt < MAX_RETRY:
            sleep_s = min(RETRY_BASE_SLEEP * (2 ** (attempt - 1)), 300)
            print(f"    失败(第{attempt}轮)，{sleep_s}s 后重试: {last_err[:110]}", flush=True)
            time.sleep(sleep_s)
    print(f"    最终失败: {last_err[:400]}", flush=True)
    return False


def load_target_entries(target):
    """从 target 提交读出 (path, mode, sha) 全量清单 + blob 体积"""
    r = git("ls-tree", "-r", "-l", target)
    if r.returncode != 0:
        print("ls-tree 失败:", _text(r.stderr)[:300]); return None, None
    entries = {}
    sizes = {}
    for line in _text(r.stdout).splitlines():
        if not line.strip():
            continue
        meta, path = line.split("\t", 1)
        parts = meta.split()
        if len(parts) < 3:
            continue
        mode, otype, sha = parts[0], parts[1], parts[2]
        size = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 0
        entries[path] = (mode, otype, sha)
        sizes[path] = size
    return entries, sizes


def main():
    if len(sys.argv) < 2:
        print("用法: push_batched.py <target-commit> [base-commit]")
        return 2
    target = sys.argv[1].strip()
    base = sys.argv[2].strip() if len(sys.argv) > 2 else out("rev-parse", "origin/master")

    if _text(git("cat-file", "-t", target).stdout).strip() != "commit":
        print(f"目标提交不存在: {target}")
        return 1

    orig_msg = out("log", "-1", "--format=%B", target)
    print(f"target = {target}")
    print(f"base   = {base}")

    rh = remote_head()
    print(f"remote = {rh}")
    if rh == target:
        print("\n远端已是目标提交，无需推送。")
        return 0

    # 变更清单
    r = git("diff", "--name-only", f"{base}..{target}")
    files = [f for f in _text(r.stdout).splitlines() if f.strip()]
    if not files:
        print("无文件差异")
        return 0
    print(f"待推送文件 {len(files)} 个", flush=True)

    # 目标树的所有条目（含 blob 体积）
    entries, sizes = load_target_entries(target)
    if entries is None:
        return 1
    for f in files:
        sizes.setdefault(f, 0)
    total = sum(sizes.get(f, 0) for f in files)
    print(f"总体积 {total / 1048576:.1f} MB", flush=True)

    # ---- 第三方 API Key：原样推送，不脱敏（AGENTS.md 3.7）----
    #
    # 库里的 Key 是工作流作者在公开分享时自己写进去的，不是我们的凭据。
    # 脱敏会改变内容指纹 → 去重失效、学习记录与原工作流对不上。
    # 遇到 GitHub Push Protection 拦截时走 Unblock URL 放行，而不是改库。
    #
    # 但**远端当前可能是旧批次提交**（其中部分文件是脱敏版），
    # 所以比对时必须区分：目标树用原始 blob，
    # 远端若有脱敏版则该文件算「未推送」，需要推原始版覆盖。

    # 远端树的全部条目（用于逐文件比对）
    # 注意比对范围要用**目标树全量**而非 base→target 的差异清单：
    # 差异清单只含 base 已有的文件，而批次提交链引入的大量新文件（base 没有）
    # 不在其中，会被误判为「还没推」而重复推送。
    remote_entries = {}
    if rh:
        r = git("ls-tree", "-r", rh)
        for line in _text(r.stdout).splitlines():
            meta, path = line.split("\t", 1)
            parts = meta.split()
            if len(parts) >= 3:
                # 结构对齐 load_target_entries: (mode, otype, sha)
                remote_entries[path] = (parts[0], parts[1], parts[2])

    print("检查远端是否残留脱敏版（需覆盖回原样）…", flush=True)
    n_redacted_remote = 0
    for path, e in entries.items():
        sha = e[2]
        rsha = remote_entries.get(path, (None, None, None))[2]
        if rsha and rsha != sha:
            # 远端 blob 与目标 blob 不同：可能是脱敏版，需要推送原始版
            n_redacted_remote += 1
    if n_redacted_remote:
        print(f"  远端有 {n_redacted_remote} 个文件与目标不一致（含旧脱敏版），将推送原样版本",
              flush=True)
    else:
        print("  远端与目标完全一致，无需密钥处理", flush=True)

    # 原样推送：直接用目标 blob
    push_sha = {path: e[2] for path, e in entries.items()}
    n_redacted = 0  # 已废除脱敏（AGENTS.md 3.7），恒为 0

    # ---- 断点续推：按**内容**而非批号判定 ----
    # 批次划分会随 TARGET_BATCH_MB / 文件体积变化而变化（10MB→124 批，2MB→534 批），
    # 靠提交主题里的「N/M」跳批在改体积后会错位 —— 必须逐文件比对远端树与目标树，
    # 只推 blob 还不一致的文件。
    #
    # 注意比对范围要用**目标树全量**而非 base→target 的差异清单：
    # 差异清单只含 base 已有的文件，而批次提交链引入的大量新文件（base 没有）
    # 不在其中，会被误判为「还没推」而重复推送。
    # 需要检查的文件 = 目标树全量（目标有的都该在远端是同一个 blob）
    check_files = list(entries.keys())
    already = sum(1 for f in check_files
                  if f in remote_entries and remote_entries[f][2] == push_sha[f]
                  and remote_entries[f][0] == entries[f][0])
    print(f"远端已含 {already}/{len(check_files)} 个目标文件", flush=True)

    pending = [f for f in check_files
               if not (f in remote_entries
                       and remote_entries[f][2] == push_sha[f]
                       and remote_entries[f][0] == entries[f][0])]
    print(f"仍需推送 {len(pending)} 个文件 "
          f"({sum(sizes.get(f, 0) for f in pending) / 1048576:.1f} MB)", flush=True)
    if not pending:
        print("远端内容已与目标一致，仅需把 master 指回目标提交。")
        pending = []

    # 按体积均衡装箱（只装真正待推的文件）
    by_top = {}
    for f in pending:
        by_top.setdefault(f.split("/", 1)[0], []).append(f)

    boxes, cur_box, cur_sz = [], [], 0
    limit = TARGET_BATCH_MB * 1048576
    for top, fs in sorted(by_top.items(),
                           key=lambda kv: -sum(sizes.get(f, 0) for f in kv[1])):
        for f in sorted(fs, key=lambda f: -sizes.get(f, 0)):
            sz = sizes.get(f, 0)
            if sz > limit:
                if cur_box:
                    boxes.append(cur_box); cur_box, cur_sz = [], 0
                boxes.append([f]); continue
            if cur_box and (cur_sz + sz > limit or len(cur_box) >= MAX_FILES):
                boxes.append(cur_box); cur_box, cur_sz = [], 0
            cur_box.append(f); cur_sz += sz
    if cur_box:
        boxes.append(cur_box)

    print(f"拆分为 {len(boxes)} 批\n", flush=True)

    # ---- parent 必须在预检前就确定 ----
    # 批次提交是「累积提交」：第 k 批 = parent 的树 + 本批文件。
    # 若 parent 用了 base，已推过的内容（远端头里已有的 blob）就会从累积树里消失，
    # 最终树校验必然失败。远端头本身就是一条以 base 为根的累积链，
    # 所以直接以 rh 为 parent，天然继承已推内容。
    parent = rh if rh else base
    if rh:
        print(f"断点续推：以远端头 {rh[:10]} 为 parent\n", flush=True)
    else:
        print("远端为空，从 base 开始推送\n", flush=True)

    # ---- 预检：验证 index-info 注入真的生效（否则会白跑几十批）----
    probe_files = pending[:50] if pending else list(entries.keys())[:50]
    # 临时索引放项目内 .tmp/（项目规则：不得用 C 盘系统 Temp 做工作区）
    probe_idx = Path(TMP_ROOT) / f"probe_idx_{os.getpid()}"
    if probe_idx.exists():
        probe_idx.unlink()
    penv = {"GIT_INDEX_FILE": str(probe_idx)}
    # 从**远端头**起步（续推时 parent 就是它），否则探针树与实际批次树不一致
    git("read-tree", parent, env=penv)
    plines = [f"{entries[f][0]} {entries[f][2]}\t{f}" for f in probe_files if f in entries]
    r = git("update-index", "--index-info", env=penv,
            stdin_data="\n".join(plines) + "\n")
    if r.stderr and "Ignoring path" in _text(r.stderr):
        print("预检失败: index-info 条目被拒 —", _text(r.stderr)[:200])
        return 1
    ptree = out("write-tree", env=penv)
    parent_tree = out("rev-parse", f"{parent}^{{tree}}")
    # 探针树应包含全部条目（parent 全部 + 探针文件）
    n_entries = len((out("ls-files", env=penv) or "").splitlines())
    parent_n = len((out("ls-tree", "-r", "--name-only", parent) or "").splitlines())
    if not pending:
        # 没有待推文件 = 远端内容已与目标一致，这是**正常终态**，
        # 不能拿「树等于 parent」当失败判据 —— 后面还要做最终 force push
        # 把 master 指回目标提交。
        print(f"无待推文件，跳过批次预检（远端已含 {len(check_files)} 个目标文件）", flush=True)
    else:
        if ptree == parent_tree:
            print("预检失败: 构造树等于 parent 树，注入未生效")
            return 1
        # 条目数检查只在「新增文件」场景有意义：
        # 覆盖已有文件（内容不同但路径相同）时条目数不变是**正常**的，
        # 用它判失败会误报（实测：覆盖 10160 个脱敏版文件时条目数持平）。
        if n_entries < parent_n:
            print(f"预检失败: 索引条目 {n_entries} 少于 parent 的 {parent_n}")
            return 1
        print(f"预检通过 (探针树 {ptree[:10]}, 索引条目 {n_entries}，parent {parent_n})，开始推送\n",
              flush=True)
    try:
        probe_idx.unlink()
    except OSError:
        pass

    # 目标树里被删除的文件（远端还有、目标没有）
    # 用远端树（而非 base）作为参照 —— 远端头可能已删过一部分，
    # 重复注入删除是幂等的，但按远端算能准确反映「还差哪些删除」。
    if remote_entries:
        deleted = [p for p in remote_entries if p not in entries]
    else:
        r = git("ls-tree", "-r", "--name-only", base)
        deleted = [p for p in _text(r.stdout).splitlines()
                   if p.strip() and p.strip() not in entries]
    if deleted:
        print(f"目标树中删除的文件 {len(deleted)} 个", flush=True)

    # **最终提交**要删除的文件，必须按 **base** 算，而不是按远端批次链算。
    # 最终提交的树是从 base 起步重建的（read-tree base），
    # 所以凡是「base 有、目标没有」的文件都会随 base 一起进树 ——
    # 若删除项只按远端链算，这部分文件会漏删，残留在远端。
    # （实测残留 3 个 _consolidated 模式卡：base 有、目标无、远端批次链已无）
    r = git("ls-tree", "-r", "--name-only", base)
    base_paths = [p.strip() for p in _text(r.stdout).splitlines() if p.strip()]
    final_deleted = [p for p in base_paths if p not in entries]
    if final_deleted:
        print(f"最终提交需删除的文件 {len(final_deleted)} 个", flush=True)

    tmp_idx = Path(TMP_ROOT) / f"push_idx_{os.getpid()}"
    tenv = {"GIT_INDEX_FILE": str(tmp_idx)}

    try:
        for idx, batch in enumerate(boxes, 1):
            mb = sum(sizes.get(f, 0) for f in batch) / 1048576
            print(f"[{idx}/{len(boxes)}] {len(batch)} 文件 / {mb:.1f} MB", flush=True)

            # 临时索引从 parent 起步
            if tmp_idx.exists():
                tmp_idx.unlink()
            if git("read-tree", parent, env=tenv).returncode != 0:
                print("  read-tree 失败"); return 1

            # 从对象库注入 blob 条目（不读工作区）
            # 格式: <mode> SP <sha1> TAB <path>
            lines = []
            for f in batch:
                e = entries.get(f)
                if not e:
                    continue
                mode = e[0]
                sha = push_sha.get(f, e[2])   # 原样 blob（不脱敏，AGENTS.md 3.7）
                lines.append(f"{mode} {sha}\t{f}")
            # 删除项: 0 SP <空 sha1> TAB <path>
            for f in deleted:
                lines.append(f"0 {'0' * 40}\t{f}")

            if lines:
                data = "\n".join(lines) + "\n"
                r = git("update-index", "--index-info", env=tenv, stdin_data=data)
                if r.returncode != 0:
                    print("  update-index 失败:", _text(r.stderr)[:300]); return 1
                # 防回归：stderr 出现 "Ignoring path" 说明行格式/换行被拒
                if r.stderr and "Ignoring path" in _text(r.stderr):
                    print("  update-index 拒绝了条目(Ignoring path)，中止")
                    print("  stderr:", _text(r.stderr)[:300]); return 1

            tree = out("write-tree", env=tenv)
            if not tree:
                print("  write-tree 失败"); return 1

            msg = (f"批量推送 {idx}/{len(boxes)}: {len(batch)} 文件\n\n"
                   f"原始提交: {target}\n\n{orig_msg}")
            r = git("commit-tree", tree, "-p", parent, "-m", msg)
            if r.returncode != 0:
                print("  commit-tree 失败:", _text(r.stderr)[:300]); return 1
            commit = _text(r.stdout).strip()

            if not push_with_retry(commit):
                print(f"\n进度 {idx - 1}/{len(boxes)}。修复网络后重跑本脚本可续推。")
                return 1
            parent = commit

        # 校验：最后一批的树应与目标树一致
        final_tree = out("rev-parse", f"{parent}^{{tree}}")
        target_tree = out("rev-parse", f"{target}^{{tree}}")
        print(f"\n最终树校验: {final_tree == target_tree}", flush=True)
        if final_tree != target_tree:
            print("  警告：树不一致，跳过 force push（保留批次历史）", flush=True)
            return 1

        # 构造最终的目标提交
        # parent 必须是**远端当前头**（批次链的头），不是 base：
        #   - base 是原始祖先，批次链与之没有共同的历史分支，
        #     push 时 git 要把整棵树重传一遍（实测 377MB / 45234 个对象）——
        #     这正是分批推送要规避的大包问题，会在代理上传阶段卡死。
        #   - 以远端头为 parent，则只需传「新增/变更的 blob」，
        #     其余对象远端已有，传输量接近 0。
        print("构造最终目标提交…", flush=True)
        if tmp_idx.exists():
            tmp_idx.unlink()
        if git("read-tree", base, env=tenv).returncode != 0:
            print("  read-tree 失败"); return 1
        lines = []
        for path, e in entries.items():
            lines.append(f"{e[0]} {push_sha.get(path, e[2])}\t{path}")
        for f in final_deleted:
            lines.append(f"0 {'0' * 40}\t{f}")
        if lines:
            r = git("update-index", "--index-info", env=tenv,
                    stdin_data="\n".join(lines) + "\n")
            if r.returncode != 0 or (r.stderr and "Ignoring path" in _text(r.stderr)):
                print("  update-index 失败:", _text(r.stderr)[:300]); return 1
        clean_tree = out("write-tree", env=tenv)
        if not clean_tree:
            print("  write-tree 失败"); return 1
        clean_msg = orig_msg.rstrip()
        # parent = 远端头（批次链的最后一环），保证 fast-forward
        final_parent = parent if parent else base
        r = git("commit-tree", clean_tree, "-p", final_parent, "-m", clean_msg)
        if r.returncode != 0:
            print("  commit-tree 失败:", _text(r.stderr)[:300]); return 1
        clean_commit = _text(r.stdout).strip()
        print(f"最终目标提交: {clean_commit} (parent {final_parent[:10]})", flush=True)

        # force push 回最终目标提交（对象已在远端，几乎不传数据）
        print("最终 force push 回目标提交…", flush=True)
        ok = False
        for attempt in range(1, MAX_RETRY + 1):
            for px in PROXIES:
                r = git(*proxy_args(px), "push", "--force",
                        "origin", f"{clean_commit}:refs/heads/master")
                if r.returncode == 0:
                    ok = True; break
                # 响应丢失但实际已生效，也要算成功（否则重复 push 会被 GH013 拒）
                if remote_head() == clean_commit:
                    ok = True; break
                # GitHub Push Protection 拦截：按 AGENTS.md 3.7，
                # 库内第三方 Key **不脱敏**，需走 Unblock URL 人工放行。
                if "GH013" in _text(r.stderr) or "pushProtectionBypassUrl" in _text(r.stderr):
                    print("\n!! 被 GitHub Push Protection 拦截。", flush=True)
                    print("   库内第三方 API Key 按规则不脱敏（AGENTS.md 3.7）。", flush=True)
                    print("   请用错误信息里的 Unblock URL 放行后重跑本脚本。", flush=True)
                    print("   详情:", _text(r.stderr)[:800], flush=True)
                    return 1
            if ok:
                break
            time.sleep(min(RETRY_BASE_SLEEP * attempt, 300))
        print("force push:", "成功" if ok else "失败")
        if not ok:
            return 1
    finally:
        try:
            tmp_idx.unlink()
        except OSError:
            pass

    print("\n本地 HEAD   :", out("rev-parse", "HEAD"))
    print("远端 master :", remote_head())
    print("工作区改动数:", len((out("status", "--short") or "").splitlines()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
