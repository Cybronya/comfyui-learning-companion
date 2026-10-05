# ComfyUI Learning Agent

一个随项目走的 ComfyUI 学习与知识沉淀 Agent：分析工作流、讲解节点与模型、把学到的东西沉淀成可复用的知识卡片，并维护自己的工作流索引与学习记录。

## 它能做什么

- **工作流分析**：丢一个 `workflow.json`（UI 格式或 API 格式都行），产出结构化分析报告（节点清单、数据流、关键参数、模式识别）。
- **工作流对比**：两个 workflow 的节点增删、参数差异一目了然。
- **节点/模型讲解**：先查本地 `knowledge/` 知识卡，没有就查证后新建卡片。
- **知识沉淀**：新节点、新模型、新原理 → 标准化知识卡 + 学习记录，越用越懂你这个项目。

## 目录一览

| 路径 | 内容 |
|---|---|
| `SKILL.md` | Agent 入口规则（触发条件、工作流程、卡片规范） |
| `workflow_analysis/analysis_rules.md` | 工作流分析方法论 |
| `workflow_analysis/workflow_template.md` | 分析报告输出模板 |
| `knowledge/nodes/` | 节点知识卡（sampler、vae、controlnet…） |
| `knowledge/models/` | 模型知识卡（sd、flux、wan…） |
| `knowledge/concepts/` | 原理知识卡（latent、diffusion…） |
| `tools/` | workflow_parser / workflow_compare / knowledge_builder |
| `memory/` | workflow_index.json（索引）+ learning_records.md（流水） |

## 快速开始

```bash
# 1. 解析一个工作流（人类可读摘要）
python tools/workflow_parser.py path/to/workflow.json

# 2. 解析并输出机器可读 JSON
python tools/workflow_parser.py path/to/workflow.json --json

# 3. 对比两个工作流
python tools/workflow_compare.py old.json new.json

# 4. 扫描工作流目录，统计节点使用频率、找"没有知识卡"的节点
python tools/knowledge_builder.py path/to/workflows_dir/

# 5. 为某个节点生成知识卡草稿
python tools/knowledge_builder.py path/to/workflows_dir/ --card KSampler --out knowledge/nodes/
```

> 工具只依赖 Python 标准库，无需额外安装。

## 知识沉淀流程

```
遇到新东西 → 查 knowledge/ 是否已有 → 有：直接引用
                                      └─ 无：查证（上游 README / 官方文档）→ 建卡
                                      → memory/learning_records.md 记一条
分析完 workflow → workflow_index.json 加索引 → 报告套 workflow_template.md
```

## 与项目的关系

- 本技能随 ComfyUI 本体安装目录走：`.ai/` 的上级就是 ComfyUI 本体，`custom_nodes/` 就在旁边。
- MiniMax H3 项目仓库（`F:\Program Files\Git\openi\ComfyUI-Minimax-H3`）内的
  `comfyui/custom_nodes/NODES_SOURCES.md`
  是全部自定义节点的权威来源清单（上游、版本、subtree 维护约定）。
- 本 Agent 只读写 `.ai/` 目录，不碰 ComfyUI 运行文件。
- 跨技能的项目级长期备忘（开发状态、待办、环境约定）统一放在仓库根 `AGENTS.md` 第 9 节，不再单独设目录。

## 维护约定

- 知识卡命名：小写英文短横线，一个主题一个文件。
- 卡片 frontmatter 必填：`name / title / category / tags / updated`。
- 内容不确定就标 `TODO(待验证)`，禁止编造参数。
