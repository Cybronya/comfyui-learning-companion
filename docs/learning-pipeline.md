# Learning Pipeline — 学习流水线设计

Version: v1.0（2026-10-10 定稿）
入口脚本：`skills/comfyui-learning/tools/learn_pipeline.py`

---

# 1. 这篇文档讲什么

把零散 ComfyUI workflow 从 RunningHub 收集、下载、入库、学习、归纳的
完整流程固化成文档。此前这些细节散落在 `AGENTS.md` 9.2 节的各批次
记录里，新会话接手时需要翻多处才能拼出全貌，本文统一收口。

**一句话流程**：

```
收集 ID → 算缺失 → 下载 → 指纹去重入库 → 预建知识卡 → 增量学习 → 数据库对账 → 重建图谱
```

---

# 2. 六步流水线（learn_pipeline.py）

| 步骤 | 脚本 / 模块 | 产出 |
|---|---|---|
| ① 收集 ID | `collect_by_tag.py` | `download/ids-by-tag/<大类>/<小类>_ids.txt` + `_meta.csv` + `_state.json` |
| ② 算缺失 | pipeline 内置 `missing_ids()` | 清单里还没下载文件的 ID |
| ③ 下载 | `download_by_ids.py` | `download/workflows-by-tag/<大类>/<小类>/<名字>_<id>.json` + `manifest.csv` |
| ④ 去重入库 | `import_workflows.py` | `comfyui_library/workflows/<大类>/<小类>/*.json`（指纹唯一） |
| ⑤ 预建卡 | `draft_cards_from_workflows.draft_for_files()` | 新节点知识卡（`comfyui_library/knowledge/nodes/`） |
| ⑥ 学习 + 对账 | `create_batch_learner().learn_folder()` + `cleanup_stale()` | 学习记录 Markdown + WorkflowDatabase 镜像 + 索引 |
| ⑦ 重建图谱 | `build_graph()` | `engine/knowledge_graph/knowledge_graph.json` |

常用参数：

```powershell
# 全自动：收集 + 下载 + 入库 + 学习 + 图谱
python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --tag "视频生成/文生视频" --count 200

# 只消化已下载的文件（跳过收集/下载两步）
python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --tag "视频生成/文生视频" --skip-collect --skip-download

# 换排序挖增量（NEWEST 榨干后试 RECOMMEND）
python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py --tag "图片生成/文生图" --sort RECOMMEND
```

注意：`--skip-collect` 目前**不会**真正跳过收集阶段（pipeline 恒跑
`collect_by_tag.py`，该开关只作用于下载步，见已知问题）。

---

# 3. 三层去重（核心设计）

流水线有三层互相独立的去重，各管一段：

| 层级 | 时机 | 手段 | 拦什么 |
|---|---|---|---|
| **ID 级** | 下载前 | `manifest.csv` + 文件名 `_<id>.json` 后缀双口径（`missing_ids()`） | 同一个 ID 重复下载；断点续传也靠它 |
| **内容指纹级** | 入库时（学习**前**） | sha256 内容指纹，与库内 + 批次内比对（`import_workflows.py`） | **不同 ID 上传但内容完全一样**的重复工作流（同作者传多遍、搬运等） |
| **学习幂等级** | `learn_folder()` 时 | `LearningStore` 按 `content_hash` 判已学 | 学过且文件没改 → 跳过；文件内容变了 → 自动重学 |

流程图：

```
收集 ID（API 翻页，状态库去重）
    ↓
算缺失（manifest + 文件名后缀双口径）      ← ID 级去重
    ↓
只下载缺失的（文件已存在自动跳过）
    ↓
指纹去重入库                              ← 内容指纹级去重（学习之前）
    ↓   闸门拦截：库内已有同指纹 → 跳过
预建知识卡（首次学习覆盖率即准，无需二次重学）
    ↓
增量学习（幂等）                          ← 学习幂等级去重
    ↓   已学 + 指纹一致 → 跳过；内容变了 → 重学
数据库对账（清死键）+ 重建图谱
```

## 3.1 为什么指纹去重必须在学习之前

2026-10-06 的教训：当时 504 条学习记录里有 45 组内容完全相同
（同一 workflow 不同文件名/平台 id 重复上传）。重复会让：

- 节点频次统计虚高——最坏 2 倍（只在重复文件里出现的节点）；
- `min_frequency=2` 的模式归纳被「同一文件传两遍」凑出假模式；
- 聚合层统计（覆盖率分布等）整体失真。

因此把指纹闸门固化在 `import_workflows.py`，挡在学习之前。
学习环节不再需要「剔重」——入库后的文件已全部指纹唯一，
学习器只做「判断这个文件之前学没学过」的幂等检查。

## 3.2 分层的好处

下载、入库、学习三个环节彼此独立、各自幂等：

- 下载可以随时中断续传（ID 级）；
- 入库可以反复跑（指纹级幂等）；
- 学习可以随时重跑（学习幂等级）。

任何一步挂掉都不影响其他层，重跑即恢复。

---

# 4. 目录约定

```
download/                            # 库外收件箱（不入库，.gitignore 白名单只放行 *.py）
  ids-by-tag/<大类>/<小类>_ids.txt       # ID 清单（每行一个 ID）
                       <小类>_meta.csv      # id/name/author/publishTime
                       <小类>_state.json    # 续收状态（已见过的 ID）
  workflows-by-tag/<大类>/<小类>/        # 下载落盘
                       <名字>_<id>.json   # 名字在前便于识别，ID 后缀保证唯一
                       manifest.csv       # 下载清单（合并模式，历史记录保留）

comfyui_library/workflows/           # 库内正身（学习对象）
  <大类>/<小类>/*.json                  # 指纹唯一，同名不同内容自动 _dup 后缀
  learning/                             # 学习记录（Markdown，唯一存放处）
    index.md                            # 汇总索引
    <大类>/<小类>/<名字>_<id>.md         # frontmatter 存元数据 + 正文存所学

comfyui_library/database/storage/    # 数据库派生存储（不入库）
  workflow_database.json                # 主库（workflow/node/pattern/experience）
  workflow_index.json 等                # 三个派生索引（save_all 可重建）

comfyui_library/knowledge/nodes/     # 节点知识卡（3149+ 张）
comfyui_library/knowledge/patterns/_consolidated/  # 归纳出的模式卡
engine/knowledge_graph/knowledge_graph.json        # 知识图谱落盘
```

---

# 5. 已知问题与坑

| 问题 | 说明 | 状态 |
|---|---|---|
| `--skip-collect` 不生效 | pipeline 恒跑 `collect_by_tag.py`，开关只作用于下载步 | 待修 |
| NEWEST 流 200 页上限 | `collect_by_tag.py` 只扫 200 页（6000 条），更老的 ID 拿不到；平台总量超出部分需换 `--sort` 或加深页数 | 待定 |
| 清单覆盖不全时回退命名 | manifest 没有的 ID 落盘为 `<id>.json`（无名），不影响学习但可读性差 | 接受 |
| 重复 ID 跨分类 | 同一工作流可能同时属于多个分类，ID 清单按分类独立维护，靠指纹闸门兜底 | 接受（设计如此） |
| 大批次学习耗时 | 全库 learn_folder 实测约 1-2 分钟（性能修复后），D5 测试需 run_in_background | 已解决 |

---

# 6. 批次记录速查

见 `AGENTS.md` 9.2 节。文生视频三批（2026-10-10）累计入库 538 个、
新建知识卡 253 张，NEWEST 流前 200 页增量已耗尽。
