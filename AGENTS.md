# AGENTS.md

ComfyUI Learning Companion —— 面向 AI Agent / 协作者的入口文档。

**接手本项目时，先读完本文，再动手。** 本文是项目的唯一入口文档：
第 2-7 节是不变的约定与环境（必读），第 8 节是项目定位，第 9 节是实时状态（改代码后必须一起更新）。

- 最后更新：2026-10-05
- 规则版本：v0.3.1（规范定稿）｜v0.4 架构标准化 ✅｜v0.5 设计文档已入库 + 引擎实装进行中
- 仓库：https://github.com/Cybronya/comfyui-learning-companion （public，分支 master）

---

## 1. 必读三份（按顺序）

| 顺序 | 文件 | 作用 |
|---|---|---|
| 1 | `AGENTS.md`（本文） | 环境、硬约定、模块地图、**实时状态** |
| 2 | `docs/roadmap.md` + `docs/architecture.md` | 版本目标与总体架构 |
| 3 | `docs/learning-engine.md` / `docs/engine-api.md` | 引擎设计与 API（改 `engine/` 前必读） |

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
AGENTS.md                     ← 本文件（唯一入口：约定 + 状态）
README.md / CHANGELOG.md      对外门面
docs/                         设计文档（10 篇）
skills/
  _core/                      Skill 框架骨架（🔶 占位）
  comfyui-learning/           主技能 + 11 个子技能（规范 + schema + 模板 + 工具）
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
3. 更新**本文第 9 节**的「已完成 / 进行中 / 待办」与顶部日期 —— 这是**强制**的。
   2026-10-05 教训：新增模块后没回头更新文档，状态曾落后代码十余个 commit。
4. 提交（中文信息）→ `git push origin master`（失败先看 3.2 是不是代理掉线）。
5. 文档里的流程图一律用代码块包裹，防止 GitHub 渲染粘连。
6. 不确定的内容标 `TODO(待验证)`，禁止编造参数。

## 7. 外部资源指针

- 自定义节点来源**权威清单**：
  `F:\Program Files\Git\openi\ComfyUI-Minimax-H3\comfyui\custom_nodes\NODES_SOURCES.md`
  （涉及"哪个插件 / 上游是谁"先读它）
- 用户主项目背景：围绕 ComfyUI **MiniMax H3**（视频生成）工作，H3 相关知识卡有 TODO 待补。
- 引擎数据落盘：`engine/context/context_store.json`（上下文）、`engine/learning_loop/experience_store.json`（经验，
  初始为空数组 `[]`，跑 `test_learning_loop.py` 会写入示例数据，提交前记得还原）

---

## 8. 项目定位

把零散 ComfyUI Workflow 转化为结构化知识的 AI Agent 框架：
分析 → 知识提取 → Pattern 发现 → 个人知识库 → AI 学习助手。

**不做**：自动运行 Workflow、自动下载模型、替代用户创作。

**本仓库根目录同时是 ComfyUI 本体安装目录**（`custom_nodes/`、`models/`、`output/` 等是本体文件，
不属于本项目）。改动前务必确认自己在动哪一边。

---

## 9. 实时状态

> 改代码后必须更新本节与顶部「最后更新」日期。

### 9.1 已完成

**文档层**

| 模块 | 路径 | 状态 |
|---|---|---|
| 入口文档 | `AGENTS.md` | ✅ 本文件（2026-10-05 建立，唯一入口） |
| 对外文档 | `docs/` | ✅ 10 篇：architecture / workflow-schema / knowledge-system / skill-system / workflow-analysis / pattern-learning / pattern_evolution / roadmap / learning-engine / engine-api |
| 门面 | `README.md` / `CHANGELOG.md` | ✅ 已入库（CHANGELOG 仍停在 v0.3.1，见待办 6） |

**Skill 层（`skills/`）**

| 模块 | 状态 |
|---|---|
| 顶层规范 `comfyui-learning/SKILL.md` | ✅ v0.3.1 定稿（角色 / 五职责 / 输出规范 / 版本限制） |
| `workflow/` Workflow 规则 | ✅ 三件套：analysis / template / compare |
| `scanner/` | ✅ 三规范 + `tools/` 四脚本（实测跑通） |
| `node-analysis/` | ✅ 规范 + `tools/` 三脚本（AST 提类，实测跑通） |
| `model-management/` | ✅ 规范 + `tools/` 三脚本（四类型识别实测全对） |
| `workflow-explanation/` | ✅ 规则 + schema + 四模板 |
| `troubleshooting/` | ✅ 规则 + schema + 三模板 |
| `memory/` | ✅ 规则 + schema + 三模板（三级可信度 Confirmed/Generated/Temporary） |
| `project-knowledge/` | ✅ 规则 + schema + 三模板 |
| `rag/` | 🔶 接口占位：四模块函数级验证通过，`__main__` 为 pass |
| `_core/` | 🔶 骨架（skill-discovery / loading / standard / registry 占位） |

**知识库（`comfyui_library/`）**

| 内容 | 状态 |
|---|---|
| 节点知识卡 | ✅ 6 张（Checkpoint / CLIPTextEncode / EmptyLatent / KSampler / SaveImage / VAEDecode）+ `node_index.json` v1.0（含 role / difficulty / learning_topics） |
| Pattern 卡 | ✅ 2 张（sd15-t2i-basic / sd15-t2i-lora） |
| 节点摘要 | ✅ 1 张（loraloader） |
| 真实 workflow 样本 | 🔶 仅 `workflows/sd1.5/` 有内容（`_workflow.json` / `_prompt.json` / `basic.json` / 两张 png）；`wan` / `flux` / `sdxl` 为空骨架 |
| 知识卡格式对齐 | 🔶 8 张 v0.2 遗产卡（`skills/comfyui-learning/knowledge/`）内容有效但**格式先于 v0.3.1 规范**，待迁移 |

**引擎层（`engine/`，v0.5 实装）**

七个模块全部落地并有 `test_*.py` 覆盖；7 个测试脚本在 `engine/` 目录下全部 exit=0（2026-10-05 复测）：

| 模块 | 能力 | 测试 |
|---|---|---|
| `models.py` / `workflow_loader.py` / `learning_engine.py` | 三个 Core Data Model（WorkflowObject / NodeInfo / LinkInfo）；JSON→WorkflowObject；`learn_workflow` 最小闭环 | `test_workflow_understanding.py` |
| `workflow_parser/` | JSON → 结构化解析；`KnowledgeLoader` 从 `node_index.json` / 知识卡自动填充 role / category / learning_topics；捕获 `widgets_values`；`parse_data` 可直接解析 dict；解析后自动写入上下文 | `test_parser.py` |
| `workflow_analyzer/` | `GraphBuilder` 图构建 + `ConnectionAnalyzer` 连接分析 + `PatternDetector` 模式识别 + `WorkflowClassifier` 分类 | `test_workflow_analyzer.py` |
| `diagnostics/` | `ParameterChecker`（KSampler widgets 提取 cfg / steps）+ `GraphChecker` 图结构检查 + `QualityChecker` 质量检查 + `rules.py` 规则表，输出问题与建议 | `test_diagnostics.py` |
| `context/` | dataclass 化 `WorkflowContext` / `ConversationContext` + `ContextManager`（精简接口 + last_update）+ 持久化 `context_store.json` | `test_context.py` |
| `response_generator/` | `QuestionAnalyzer` 问题分析 + `PromptBuilder` 上下文提示词构建 + 知识注入 + `ResponseTemplate`（**替代原 teaching 骨架，lesson_generator 已删除**） | `test_response.py` |
| `learning_loop/` | `workflow_compare`（节点 / 参数差异）+ `improvement_analyzer`（改动影响推断）+ `experiment_tracker`（经验持久化 / 检索 / 按类型与标签过滤）；附 README / ARCHITECTURE / USAGE_EXAMPLE | `test_learning_loop.py` |
| `workflow_index_manager.py` | workflow / pattern 索引的增删改查 | 工具脚本，无单测 |

引擎主链路：

```
Workflow JSON
  → workflow_parser      解析 + 知识注入
  → workflow_analyzer    图构建 / 模式 / 分类
  → diagnostics          参数 / 图结构 / 质量诊断
  → response_generator   回答生成
        ↓
  learning_loop          用户改工作流 → 对比 → 改进分析 → 经验积累
```

### 9.2 进行中

**v0.5 引擎实装**：Phase 1（Workflow Loader）✅、Phase 2（analyzer 三件）✅ 之后，
又完成了 context 上下文引擎、response_generator 回答生成、diagnostics 诊断引擎、learning_loop 学习循环。

引擎目前是**多个可独立运行的能力模块**，尚未由单一入口串联；`engine/__init__.py` 只导出 `LearningEngine`，
实际能力面远大于此。Phase 3-5（knowledge_writer / pattern_manager / 完整串联 + CLI）尚未实装。

### 9.3 待办（按优先级）

1. **统一引擎入口与串联**：CLI（`python -m engine learn`）+ 把 parser → analyzer → diagnostics →
   response_generator → learning_loop 串成一条链；`engine/__init__.py` 只导出 `LearningEngine`，能力面需对齐
2. **实战首跑**：向 `comfyui_library/workflows/{wan,flux,sdxl}/` 放入第一批真实 workflow（json + 分析 md），
   跑通 scanner → 解析 → 诊断 → 回答全链路，产出 `workflow_manifest.json`
3. **补齐 Phase 3-5**：`knowledge_writer`（产出 `knowledge/workflows/` 五件套）→ `pattern_manager`
   （`pattern_index.json` 至今未建立，是 SKILL.md 要求的三索引之一）
4. **测试入口统一**：6 个 `test_*.py` 改用 `from engine.xxx` 包导入，使其可从仓库根
   `python -m engine.test_xxx` 直接运行（现状只有 `test_learning_loop.py` 符合）
5. **文档修正**：补写缺失的 `docs/implementation-plan.md`（旧状态文档曾引用它但文件不存在），或删掉相关引用
6. **CHANGELOG 补记**：仍停在 v0.3.1，v0.4 / v0.5 与全部引擎模块均未入账
7. **RAG v0.4 实装**：embedding 接入；统一 `build_index`（text 键）与 `search_database`（content 键）
   的键名；`prepare_documents` 的 content 从 `str(item)` 改为规范拼装
8. **knowledge/ 卡片对齐 v0.3.1**：格式迁移 + 补 MiniMax H3 与 Wan 的差异对照卡（wan 卡内 TODO）
9. **遗留清理（用户未决）**：旧 `workflow_analysis/`（复数）目录与现行 `workflow/`（单数）内容重叠；
   `memory/learning_records.md`、`workflow_index.json` 旧格式是否并入 memory 子技能体系

### 9.4 维护规则

1. 改动任何子技能 / 工具 / 引擎模块 → 提交信息用**中文短句**描述模块与动作
2. 完成一批开发 → **必须**更新 9.1 / 9.2 / 9.3 与顶部「最后更新」日期
3. 新增顶层文件 → 同步在 `.gitignore` 加 `!/<文件名>`，否则不会被跟踪
4. 新增子技能 → 照既有结构（skill.md + `*_rules.md` + `*_schema.json` + README.md + templates|tools）
5. 工具脚本与引擎代码：只依赖标准库；读 JSON 用 `utf-8-sig`；
   **改动后必须自测**（`engine/` 目录下 `python test_*.py`，确认 exit=0）再提交
6. 文档竖排流程图一律用代码块包裹（防 GitHub 渲染粘连）
7. 不确定的内容标 `TODO(待验证)`，禁止编造参数
