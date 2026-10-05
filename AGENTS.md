# AGENTS.md

ComfyUI Learning Companion —— 面向 AI Agent / 协作者的入口文档。

**接手本项目时，先读完本文，再动手。** 本文只放"不会变"的东西（环境、约定、命令、地图）。
会变的状态（已完成 / 进行中 / 待办）一律只写在 `skills/PROJECT_MEMORY/project-status.md`，避免两处打架。

---

## 1. 必读三份（按顺序）

| 顺序 | 文件 | 作用 |
|---|---|---|
| 1 | `AGENTS.md`（本文） | 环境、命令、硬约定、模块地图 |
| 2 | `skills/PROJECT_MEMORY/project-status.md` | **实时状态**：已完成 / 进行中 / 待办优先级 |
| 3 | `docs/roadmap.md` + `docs/architecture.md` | 版本目标与总体架构 |

动手前若对某个模块有疑问，再进 `docs/` 里的专题文档（见第 5 节）。

---

## 2. 这是什么项目

把零散 ComfyUI Workflow 转化为结构化知识的 AI Agent 框架：
分析 → 知识提取 → Pattern 发现 → 个人知识库 → AI 学习助手。

**不做**：自动运行 Workflow、自动下载模型、替代用户创作。

**本仓库根目录同时是 ComfyUI 本体安装目录**，`custom_nodes/`、`models/`、`output/` 等是本体文件，
不是本项目内容。改动前务必确认自己在动哪一边。

---

## 3. 硬约定（踩过坑，务必遵守）

### 3.1 git

- 白名单制 `.gitignore`：根下 `/*` 全忽略，只放行 `.gitignore` / `README.md` / `CHANGELOG.md` /
  `AGENTS.md` / `docs/` / `skills/` / `comfyui_library/` / `engine/`。
  **新增顶层文件必须同步在 `.gitignore` 加一行 `!/<文件名>`，否则不会被跟踪。**
- 分支 `master`，远程 `https://github.com/Cybronya/comfyui-learning-companion.git`（public）。
- 提交身份：cybronya / wangxinloo@163.com。
- 提交信息用**中文短句**描述模块与动作，与既有历史保持一致。

### 3.2 网络（最高频的坑）

GitHub 走本地代理 **`127.0.0.1:3067`**（Karing）。

- `push` 报 `Empty reply` / `SSL handshake` / `Failed to connect ... over proxy 127.0.0.1`
  → **代理掉线，不是代码问题**。等代理恢复后 `git push origin master` 重试即可。
- 直连 github.com 会被 TLS 握手重置，不要试图绕过代理。
- 镜像前缀只能用于下载，**不能用于 push**。

### 3.3 Python

- 版本 3.12.10。
- 工具脚本与引擎代码**只用标准库**，不引入第三方依赖。
- 读 JSON 一律 `utf-8-sig`（Windows 下 ComfyUI 导出的 JSON 带 BOM）。

### 3.4 测试

测试脚本在 `engine/test_*.py`，**必须在 `engine/` 目录下运行**：

```powershell
cd "F:\Program Files\ComfyUI\engine"
python test_parser.py
```

6 个测试脚本用的是裸导入（`from workflow_parser.parser import ...`），
从仓库根用 `python -m engine.test_parser` 会 `ModuleNotFoundError`。
只有 `test_learning_loop.py` 两种方式都能跑。
改动引擎代码后，至少跑一遍相关的 `test_*.py`，确认 exit=0 再提交。

---

## 4. 模块地图

```
AGENTS.md                     ← 本文件（入口）
README.md / CHANGELOG.md      对外门面
docs/                         设计文档（10 篇）
skills/
  _core/                      Skill 框架骨架（🔶 占位）
  comfyui-learning/           主技能 + 11 个子技能（规范 + schema + 模板 + 工具）
  PROJECT_MEMORY/             项目级长期记忆 ← 实时状态
comfyui_library/
  knowledge/nodes/            节点知识卡（6 张）+ node_index.json
  knowledge/patterns/         Pattern 卡（2 张）
  knowledge/summaries/        节点摘要（1 张）
  workflows/{wan,flux,sdxl,sd1.5}/   真实 workflow 样本（目前仅 sd1.5 有内容）
engine/                       可执行层（v0.5 起）
  models.py / workflow_loader.py / learning_engine.py      核心数据模型与加载
  workflow_parser/            JSON → 结构化解析（+ 知识库注入）
  workflow_analyzer/          图构建 / 连接分析 / 模式识别 / 分类
  diagnostics/                参数检测 / 图结构检查 / 质量检查
  context/                    Workflow + Conversation 上下文与持久化
  response_generator/         问题分析 / 提示词构建 / 回答生成
  learning_loop/              对比 → 改进分析 → 经验积累（最新）
  workflow_index_manager.py   workflow / pattern 索引管理
```

## 5. 文档地图

| 想了解 | 读 |
|---|---|
| 总体架构 | `docs/architecture.md` |
| 版本目标 | `docs/roadmap.md` |
| 引擎设计与 API | `docs/learning-engine.md`、`docs/engine-api.md` |
| Workflow 数据结构 | `docs/workflow-schema.md` |
| 分析怎么做的 | `docs/workflow-analysis.md`、`docs/pattern-learning.md`、`docs/pattern_evolution.md` |
| 知识体系怎么组织 | `docs/knowledge-system.md` |
| Skill 体系规范 | `docs/skill-system.md`、`skills/comfyui-learning/SKILL.md` |

模块级设计文档在模块目录内：`engine/learning_loop/{README,ARCHITECTURE,USAGE_EXAMPLE}.md`。

---

## 6. 工作方式

1. 动手前读第 1 节的三份文件。
2. 改代码 → 跑相关 `test_*.py` 自测（约定要求，不能跳）。
3. 更新 `project-status.md` 的「已完成 / 进行中 / 待办」与日期 —— 这是**强制**的，
   上一轮就是因为漏了这步，文档落后代码十几个 commit。
4. 提交（中文信息）→ `git push origin master`（失败先看 3.2 是不是代理掉线）。
5. 文档里的流程图一律用代码块包裹，防止 GitHub 渲染粘连。
6. 不确定的内容标 `TODO(待验证)`，禁止编造参数。

## 7. 外部资源指针

- 自定义节点来源**权威清单**：
  `F:\Program Files\Git\openi\ComfyUI-Minimax-H3\comfyui\custom_nodes\NODES_SOURCES.md`
  （涉及"哪个插件 / 上游是谁"先读它）
- 用户主项目背景：围绕 ComfyUI **MiniMax H3**（视频生成）工作，H3 相关知识卡有 TODO 待补。
