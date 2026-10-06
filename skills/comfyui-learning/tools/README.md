# tools/ — RunningHub 工作流收集与下载工具链

> 面向 AI Agent 的操作手册：接口事实、推荐流程、关键约定与踩坑实录。
> 接口参数均为 2026-10-06 浏览器抓包实测确认，**换接口/换字段前必须重新抓包，禁止盲猜**。

## 工具分工

| 脚本 | 用途 | 状态 |
|---|---|---|
| `collect_by_tag.py` | **按功能分类**收集工作流 ID（主路径） | 2026-10-06 新增 |
| `collect_workflow_ids.py` | 按关键词搜索收集 ID（旧路，增量续收） | 可用 |
| `download_by_ids.py` | 按 ID 清单批量下载工作流 JSON | 已升级：`--meta` + 按 ID 去重 |
| `compare_workflow.py` / `workflow_compare.py` | 工作流对比 | 存量工具 |
| `extract_png_workflow.py` | 从 PNG 提取嵌入的 workflow | 存量工具 |
| `workflow_parser.py` / `knowledge_builder.py` | 解析/知识构建 | 存量工具 |

## 接口事实（全部无需登录即可用）

```
分类树（两级嵌套：大类 → 小类）
    POST https://www.runninghub.cn/api/portal/tag/tree
    body {"rang":"WORKFLOW"}
    返回 level1 大类（图片生成/视频生成/数字人…）+ childTags 小类（文生图/图生图…）

分类列表（市场页数据源）
    POST https://www.runninghub.cn/api/portal/template/list
    body {"size":30, "current":<页码>, "tags":["<小类ID>",...], "sort":"NEWEST"}
    · 每页 30 条；tags 传小类 ID；大类 = 其全部小类 ID 的并集（与网页点大类行为一致）
    · sort=NEWEST 按发布时间倒序；另有 RECOMMEND（默认推荐）
    · 记录自带 id/name/owner/publishTime/nodeCount/tags

关键词搜索（搜索页数据源，旧路）
    POST https://www.runninghub.cn/api/search/workflow
    body {"size":30, "current":<页码>, "search":"<关键词>", "tags":[], "sort":"NEWEST"}

下载导出
    POST https://www.runninghub.cn/api/workflow/export
    body {"workflowId":"<ID>"}
    · 返回纯 ComfyUI 画布 JSON（nodes/links/groups），顶层 id 是画布 UUID，全文搜不到平台 ID
    · 响应必须含 "nodes" 字段才算有效工作流
    · 公开作品无需登录；少数作品返回 412（作者导出限制，登录态 API 直调也可能 412）
```

## 推荐工作流（收集 → 下载 → 增量闭环）

```
collect_by_tag.py（收集 ID）
    python collect_by_tag.py --list                    # 查看大类/小类结构
    python collect_by_tag.py 文生图 100 --out download/ids-by-tag
    python collect_by_tag.py 图生图 100 --out download/ids-by-tag
    python collect_by_tag.py 风格画作/热门IP 50          # 同名小类用「父/子」消歧
        ↓ 产出 <out>/<大类>/<小类>_ids.txt + _meta.csv + _state.json

download_by_ids.py（按 ID 下载，与收集清单同名配套）
    python download_by_ids.py <ids.txt> --meta <meta.csv> --out <目录>
        ↓ 产出 <目录>/<名字>_<id>.json + manifest.csv
        ↓ 重跑安全：按 ID 去重，只补增量
```

## 关键约定

1. **分类是两级嵌套，只按小类收集**：大类（图片生成）下挂小类（文生图/图生图/反推提示词）。
   传大类名会被拒绝并列出小类；「数字人/音频生成/其他」这类大类=唯一同名小类的自动按小类处理。
2. **落盘镜像结构**（清单层与下载层同名对应，方便按目录处理）：
   - 清单：`download/ids-by-tag/<大类>/<小类>_ids.txt|_meta.csv|_state.json`
   - 下载：`download/workflows-by-tag/<大类>/<小类>/*.json + manifest.csv`
3. **meta 表精简 4 列 `id,name,author,publishTime`**：
   tags/nodeCount 无消费方已删；author/publishTime 保留是为了对齐 manifest 五列
   `id,name,author,publishTime,file` 不出空值。load 端兼容 4/5/6 列。
4. **manifest 合并模式**：读入旧行 → 本次 ID 覆盖/追加 → 历史中不在本次范围的行原样保留。
   禁止整文件重写。每次下载后核对「JSON 文件数 = manifest 数据行数 = ID 清单条数」。
5. **按 ID 去重（download_by_ids.py 默认行为）**：
   下载前扫输出目录文件名尾缀 ID（`_<id>.json`，兼容早期纯 `<id>.json`），命中的跳过下载
   但 manifest 补记——重跑任何命令都是安全增量，文件被挪动/改名也不影响。
6. **命名规则（全链路统一）**：`<安全化名字>_<id>.json`；Windows 非法字符 `\ / : * ? " < > |`
   及换行制表符替换为 `_`、去首尾空格与点号、截断 80 字符、无名字回退纯 `<id>.json`。
   同标题多作品靠 ID 后缀保证唯一。
7. **增量续收原理**（state.json）：最新流是动态的（新帖把旧的往后挤），固定页码会漏收。
   用已见 ID 集合做位置锚点，每次从第 1 页扫描跳过已见、只收未见。
8. **限速**：请求间隔 0.4 秒防风控；单批数百条实测稳定（396/396 零失败）。
9. **412 处理顺序**：先在既有下载目录按 ID/标题找是否已有 → 有则归位；
   无则走浏览器页面详情页「下载」按钮流程（Playwright 拦截 download 事件 saveAs）；
   仍失败（作者导出限制）记录为例外，**不无限重试**。
10. **读文件一律 `utf-8-sig`**：Windows 下 PowerShell/Excel 生成的清单 txt 带 BOM，
    裸 utf-8 会把 `\ufeff` 混进第一个 ID 导致 404。

## 登录态事实（重要，容易误判）

- 自动化浏览器（Playwright 持久配置）**默认自带 RunningHub 登录态**（页头有个人按钮）。
- 但在页面里**裸调 `fetch()` 不带站点注入的令牌**，用户接口会返回
  `{"code":403,"msg":"TOKEN_MISSION"}`——**不能以此判断未登录**。
- 正确的登录态判据：抓站点自己发出的请求响应（如 `/api/message/user/unreadCount`
  返回 `code:0`）或检查页头个人中心/头像元素。
- 收集（tag/tree、template/list）与绝大多数导出（workflow/export）无需登录；
  412 限制件才需要登录态，且走页面下载按钮流程最稳。

## 踩坑实录（都是真踩过）

| 坑 | 后果 | 正确做法 |
|---|---|---|
| PowerShell `Import-Csv | Export-Csv` 指向同一文件 | 管道边读边写，原文件被截断清空 | 先写临时文件再替换；或用 Python |
| PowerShell 内联 `python -c` 写多行探测代码 | 引号转义极易语法错误 | 写临时 .py 执行，结论确认后删除 |
| 裸 `fetch()` 返回 TOKEN_MISSION 403 | 误判"未登录"，白折腾登录流程 | 见上方「登录态事实」 |
| 接口参数盲猜（如 searchKey/keyword） | 不报错而是返回全站数据，污染清单 | 先抓包拿真实请求体（Playwright `page.on('request')`） |
| 固定页码续收 | 新帖插入导致漏收/重收 | state.json 已见 ID 锚点，从第 1 页扫 |
| 用纯标题当文件名 | 同标题互相覆盖 | 必须带 `_<id>` 后缀 |
| run_code/evaluate 绑定独立 managed 页面 | 与侧栏浏览器 tabs 不互通，误以为页面没加载 | run_code 内自己 `page.goto` |
| 同 ID 多副本直接删 | 内容可能不一致 | 先 MD5 对比，一致才删，同步修 manifest |

## 当前库存（2026-10-06）

```
download/ids-by-tag/图片生成/          ← 清单层
    文生图 201 / 图生图 100 / 反推提示词 100（state.json 支持续收）
download/workflows-by-tag/图片生成/    ← 下载层（镜像结构）
    文生图 201 / 图生图 100 / 反推提示词 100 个 JSON + manifest.csv
    （396/396 下载零失败，三方账面一致）
download/workflows-json/               ← 早期 MiniMax H3 关键词批次（150 条，独立 manifest）
```
