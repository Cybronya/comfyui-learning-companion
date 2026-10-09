#!/usr/bin/env python3
"""从 RunningHub 搜索「文生视频」分类的最新 100 个工作流 ID。

原理：
- 搜索接口 POST https://www.runninghub.cn/api/search/workflow 支持 tagIds 筛选
- 先扫描前几页提取所有 tag_id 和 name，找到"文生视频"的 tag_id
- 再用 tagIds 参数搜索该分类下最新排序的前 100 个 ID
- 输出到独立的 ID 文件，不与旧 ID 混合
- 最后比对旧 ID 文件，输出重复清单
"""
from __future__ import annotations

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

URL = "https://www.runninghub.cn/api/search/workflow"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Origin": "https://www.runninghub.cn",
    "Referer": "https://www.runninghub.cn/search",
}
PAGE_SIZE = 30

# 旧 ID 文件（用于跨分类去重，不包含本分类自身）
OLD_ID_FILES = [
    Path(r"F:\Program Files\ComfyUI\download\ids-by-tag\图片生成\文生图_ids.txt"),
    Path(r"F:\Program Files\ComfyUI\download\ids-by-tag\图片生成\图生图_ids.txt"),
    Path(r"F:\Program Files\ComfyUI\download\ids-by-tag\图片生成\反推提示词_ids.txt"),
    Path(r"F:\Program Files\ComfyUI\download\minimax-h3-workflow-ids.txt"),
    Path(r"F:\Program Files\ComfyUI\download\minimax-h3-workflow-ids-02.txt"),
    Path(r"F:\Program Files\ComfyUI\download\minimax-h3-workflow-ids-03.txt"),
]

# 输出文件（同时是输入：读已有 ID 去重，写合并后的完整集合）
OUT_FILE = Path(r"F:\Program Files\ComfyUI\download\ids-by-tag\视频生成\文生视频_ids.txt")


def api_post(body: dict) -> dict:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(URL, data=data, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"API 错误 {e.code}: {e.read().decode('utf-8', 'replace')[:200]}")
        return {}
    except Exception as e:
        print(f"请求异常: {e}")
        return {}


def find_wenshengshipin_tag_id(max_pages: int = 5) -> str | None:
    """扫描前几页，提取所有 tag，找"文生视频"的 tag_id。"""
    print("=== 第 1 步：扫描标签，找「文生视频」tag_id ===")
    all_tags: dict[str, str] = {}  # tag_id -> tag_name
    current = 1
    while current <= max_pages:
        body = {"size": PAGE_SIZE, "current": current, "search": "", "tags": [], "sort": "NEWEST"}
        r = api_post(body)
        data = r.get("data") or {}
        recs = data.get("records") or []
        if not recs:
            break
        for rec in recs:
            for tag in (rec.get("tags") or []):
                tid = tag.get("id", "")
                tname = tag.get("name", "")
                all_tags[tid] = tname
        current += 1
        print(f"  第 {current - 1} 页扫描完成，累计 {len(all_tags)} 个不同标签")

    # 找"文生视频"
    wen_id = None
    for tid, tname in all_tags.items():
        if "文生视频" in tname:
            wen_id = tid
            print(f"  找到「文生视频」tag_id: {tid} (name: {tname})")

    if not wen_id:
        # 打印所有标签供参考
        print("  未找到「文生视频」，以下是扫描到的所有标签：")
        for tid, tname in sorted(all_tags.items(), key=lambda x: x[1]):
            print(f"    {tid}  {tname}")
        return None

    return wen_id


def collect_by_tag_id(tag_id: str, target: int, sort: str = "NEWEST") -> list[str]:
    """用 tagIds 参数搜索指定分类，按最新排序收集 ID。"""
    print(f"\n=== 第 2 步：按 tag_id={tag_id} 搜索最新 {target} 个 ===")
    new_ids: list[str] = []
    names: dict[str, str] = {}
    current = 1
    max_pages = 10
    while len(new_ids) < target and current <= max_pages:
        body = {
            "size": PAGE_SIZE,
            "current": current,
            "search": "",
            "tags": [tag_id],
            "sort": sort,
        }
        r = api_post(body)
        data = r.get("data") or {}
        recs = data.get("records") or []
        total = data.get("total", 0)
        if current == 1:
            print(f"  平台该分类总数: {total}")
        if not recs:
            print(f"  第 {current} 页无数据，停止")
            break
        for rec in recs:
            rid = rec["id"]
            if rid not in names:
                names[rid] = rec.get("name", "")
                new_ids.append(rid)
                if len(new_ids) >= target:
                    break
        current += 1
        print(f"  第 {current - 1} 页完成，已收集 {len(new_ids)} 个")

    return new_ids, names


def load_old_ids() -> set[str]:
    """加载所有旧 ID 文件，合并为集合。"""
    old_ids: set[str] = set()
    for f in OLD_ID_FILES:
        if f.exists():
            ids = [line.strip() for line in f.read_text(encoding="utf-8").splitlines() if line.strip()]
            old_ids.update(ids)
            print(f"  {f.name}: {len(ids)} 个 ID")
        else:
            print(f"  {f.name}: 文件不存在，跳过")
    print(f"  旧 ID 合计: {len(old_ids)} 个")
    return old_ids


def load_existing_ids() -> set[str]:
    """读取本分类已有 ID（OUT_FILE 自身），用于去重。"""
    existing: set[str] = set()
    if OUT_FILE.exists():
        ids = [line.strip() for line in OUT_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
        existing.update(ids)
        print(f"  {OUT_FILE.name} 已有: {len(ids)} 个 ID")
    else:
        print(f"  {OUT_FILE.name} 不存在，首次收集")
    return existing


def main() -> int:
    # 1. 找标签
    tag_id = find_wenshengshipin_tag_id(max_pages=5)
    if not tag_id:
        print("未找到「文生视频」分类 tag_id，无法继续。")
        return 1

    # 2. 收集 ID（从 API 拉 300 个）
    collected_ids, names = collect_by_tag_id(tag_id, target=300, sort="NEWEST")
    if not collected_ids:
        print("未收集到任何 ID。")
        return 1

    print(f"\nAPI 收集到 {len(collected_ids)} 个 ID")

    # 3. 去重：减去本分类已有 ID
    print("\n=== 去重 ===")
    existing_ids = load_existing_ids()
    collected_set = set(collected_ids)
    new_ids = [wid for wid in collected_ids if wid not in existing_ids]
    print(f"  API 收集: {len(collected_ids)}  已有: {len(existing_ids)}  新增: {len(new_ids)}")

    # 4. 写回合并后的完整集合（已有 + 新增）
    combined = list(existing_ids) + new_ids
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(combined) + "\n", encoding="utf-8")
    print(f"合并后共 {len(combined)} 个 ID，已写入: {OUT_FILE.resolve()}")

    # 5. 比对跨分类重复
    print("\n=== 跨分类去重 ===")
    old_ids = load_old_ids()
    new_set = set(new_ids)
    duplicates = sorted(new_set & old_ids)
    unique_new = sorted(new_set - old_ids)

    print(f"\n新增 ID: {len(new_ids)}")
    print(f"与跨分类重复: {len(duplicates)} 个")
    print(f"真正新增: {len(unique_new)} 个")

    if duplicates:
        print(f"\n--- 重复 ID（{len(duplicates)} 个）---")
        for rid in duplicates[:20]:
            print(f"  {rid}  {names.get(rid, '')[:40]}")
        if len(duplicates) > 20:
            print(f"  ... 其余 {len(duplicates) - 20} 个见重复清单")

    print(f"\n--- 新增 ID 前 20 个 ---")
    for rid in unique_new[:20]:
        print(f"  {rid}  {names.get(rid, '')[:40]}")
    if len(unique_new) > 20:
        print(f"  ... 其余 {len(unique_new) - 20} 个见 ID 文件")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
