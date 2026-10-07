# AGENTS.md

ComfyUI Learning Companion —— 面向 AI Agent / 协作者的入口文档。

**接手本项目时，先读完本文，再动手。** 本文是项目的唯一入口文档：
第 2-7 节是不变的约定与环境（必读），第 8 节是项目定位，第 9 节是实时状态（改代码后必须一起更新）。

- 最后更新：2026-10-07
- **版本号唯一权威来源：`docs/roadmap.md` 第 3 节**（本文不另立版本表，只在状态描述里引用）
- 规则版本：v0.3.1（Skill 规范定稿）｜v0.4 架构标准化 ✅｜v0.5 引擎实装进行中
- 仓库：https://github.com/Cybronya/comfyui-learning-companion （public，分支 master，无 git tag）

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

- 白名单制 `.gitignore`：根下 `/*` 全忽略，只放行 `.gitignore` / `README.md` /
  `AGENTS.md` / `docs/` / `skills/` / `comfyui_library/` / `engine/`。
  **新增顶层文件必须同步在 `.gitignore` 加一行 `!/<文件名>`，否则不会被跟踪。**
- 分支 `master`，远程 `https://github.com/Cybronya/comfyui-learning-companion.git`（public）。
- 提交身份：cybronya / wangxinloo@163.com。
- 提交信息用**中文短句**描述模块与动作，与既有历史保持一致。

#### 推送纪律（2026-10-05 用户明确要求）

**不要自动 `git push`。** 改完代码和文档后停下来，把改动摘要告诉用户，等用户说「提交 / 推送」
再做。具体规则：

- `git add` / `git commit` 与 `git push` 分开对待：commit 可以在明确要求提交时做，
  **push 只能由用户显式要求触发**。
- 用户没明确说推送时，最多做到 commit，然后报告「本地已提交 N 个 commit，等你确认推送」。
- 不确定「刚才那句算不算要求推送」时，按不算处理 —— 宁可不推，也不要擅自推。
- 推送前跑一次 `git status`，确认没有测试副产物（`__pycache__/`、`engine/engine/`、
  被测试写脏的 `context_store.json` / `experience_store.json`）混进暂存区。
- **运行期副产物已在 `.gitignore` 末尾统一忽略**：`context_store.json` /
  `experience_store.json` / `retrieval_store.json` / `knowledge_graph.json` /
  `learning_queue.md`。它们都能由源码重新生成，不该入库。
  注意 `context_store.json` 与 `experience_store.json` **历史上已被跟踪**，
  加 ignore 规则不会自动取消跟踪 —— 要真正忽略需 `git rm --cached`。

### 3.2 网络（最高频的坑）

GitHub 走本地代理 **`127.0.0.1:3067`**（Karing）。

- `push` 报 `Empty reply` / `SSL handshake` / `Failed to connect ... over proxy 127.0.0.1`
  → **代理掉线，不是代码问题**。等代理恢复后 `git push origin master` 重试即可。
- 直连 github.com 会被 TLS 握手重置，不要试图绕过代理。
- 镜像前缀只能用于下载，**不能用于 push**。
- 本节只在你已决定推送后用得上；**推送触发条件见 3.1 推送纪律**。

### 3.3 RunningHub 下载（2026-10-07 用户明确要求）

- **无论什么情况都用登录态下载**。工作流导出（`/api/workflow/export`）
  一律走自动化浏览器的登录态（Playwright 持久配置，页头有个人按钮），
  **禁止匿名 API 直调导出**。市场列表 / 分类树等只读接口可匿名。
- 412（作者导出限制）处理顺序见 `skills/comfyui-learning/tools/README.md`：
  先按 ID/标题在既有目录找 → 浏览器登录态走「下载」按钮 → 仍失败记例外不重试。

### 3.4 Python

- 版本 3.12.10。
- 工具脚本与引擎代码**只用标准库**，不引入第三方依赖。
- 读 JSON 一律 `utf-8-sig`（Windows 下 ComfyUI 导出的 JSON 带 BOM）。

### 3.5 测试

测试脚本在 `engine/test_*.py`，共 **18 个**（`test_database.py` /
`test_database_integration.py` 测的是 `comfyui_library/database` 及其引擎接入）。
**必须加 `-X utf8`**（控制台默认 GBK，中文输出乱码）。

**6 个旧测试用裸导入**（`from workflow_parser.parser import ...`），
从仓库根用 `python -m engine.xxx` 会 `ModuleNotFoundError`，**只能在 `engine/` 目录下跑**：

```powershell
cd "F:\Program Files\ComfyUI\engine"
python -X utf8 test_parser.py
python -X utf8 test_workflow_understanding.py
python -X utf8 test_workflow_analyzer.py
python -X utf8 test_diagnostics.py
python -X utf8 test_context.py
python -X utf8 test_response.py
```

**12 个用包导入（`from engine.xxx` / `from comfyui_library.database`）**，**从仓库根跑**：

```powershell
cd "F:\Program Files\ComfyUI"
python -X utf8 -m engine.test_learning_loop
python -X utf8 -m engine.test_knowledge_evolution
python -X utf8 -m engine.test_retrieval
python -X utf8 -m engine.test_agent_core
python -X utf8 -m engine.test_answer
python -X utf8 -m engine.test_autonomous_learning
python -X utf8 -m engine.test_workflow_learning
python -X utf8 -m engine.test_knowledge_consolidation
python -X utf8 -m engine.test_learning_scheduler
python -X utf8 -m engine.test_knowledge_graph
python -X utf8 -m engine.test_database
python -X utf8 -m engine.test_database_integration
```

改 `engine/` 下的模块后，18 个测试全跑一遍（6 个在 `engine/` 目录 + 12 个从根目录）。

改动引擎代码后，至少跑一遍相关的 `test_*.py`，确认 exit=0 再提交。

---

## 4. 模块地图

```
AGENTS.md                     ← 本文件（唯一入口：约定 + 状态）
README.md                     对外门面（版本号只做指针，不重复维护）
docs/                         设计文档（10 篇）
skills/
  _core/                      Skill 框架骨架（🔶 占位）
  comfyui-learning/           主技能 + 11 个子技能（规范 + schema + 模板 + 工具）
comfyui_library/
  database/                   **长期知识存储底座**（2026-10-06 新增，只存与查、不学习）
    models.py                 WorkflowRecord / NodeRecord / PatternRecord / ExperienceRecord
    database.py               WorkflowDatabase：JSON 持久化（utf-8-sig 读 / version 守卫 / 缺键回填）
    workflow_repository.py    workflow 增删查；add/delete 自动对账节点反向索引 used_in
    node_repository.py        节点 → used_in（register 支持补 category）
    pattern_repository.py     模式登记；回填 workflow.patterns（互引防漂移）
    experience_repository.py  学习经验（同 workflow_id 最新覆盖）
    index_manager.py          三个派生索引的构建与落盘（save_all() 可重建）
    storage/                  workflow_database.json + workflow/node/pattern_index.json
                              （此处 node_index.json 是**节点使用索引**，与
                              knowledge/nodes/node_index.json 知识卡索引同名不同物）
  knowledge/nodes/            节点知识卡（6 张）+ node_index.json
  knowledge/patterns/         Pattern 卡（2 张，手写）
    _consolidated/            **归纳出的模式**（自动生成，勿手改）
                              每个模式一个 .md，knowledge_consolidation 产出
  knowledge/summaries/        节点摘要（1 张）
  workflows/{wan,flux,sdxl,sd1.5}/   真实 workflow 样本（目前仅 sd1.5 有内容）
    learning/                 **学习记录唯一存放处**（Markdown，非 JSON）
      index.md                汇总索引，一行一个 workflow 带链接
      <family>/<name>.md     每个 workflow 一份记录：frontmatter 存元数据
                              正文存学到的内容（结构/参数/体检/缺口/发现）
                              路径常量见 engine/workflow_learning/paths.py
                              扫描器按 SKIPPED_DIR_NAMES 跳过本目录，否则记录会被
                              当成 workflow 学习，形成无限循环
                              可直接 grep：grep -rl "LoraLoader" learning/
engine/                       可执行层（v0.5 起）
  models.py / workflow_loader.py / learning_engine.py      核心数据模型与加载
  workflow_parser/            JSON → 结构化解析（+ 知识库注入）
  workflow_analyzer/          图构建 / 连接分析 / 模式识别 / 分类
  diagnostics/                参数检测 / 图结构检查 / 质量检查
  context/                    Workflow + Conversation 上下文与持久化
  response_generator/         问题分析 / 提示词构建 / 回答生成
  learning_loop/              对比 → 改进分析 → 经验积累
  knowledge_evolution/        从「参数改动记录」归纳 → 改参数会怎样（2026-10-05）
  knowledge_consolidation/    从「完整 workflow」归纳 → 这类流程长什么样（2026-10-06）
                              （ExperienceLoader 优先读 WorkflowDatabase.experiences）
  retrieval/                  关键词召回 + 排序 → 喂给回答生成器（2026-10-05 新增）
  agent_core/                 总控：把上面模块编成六阶段 Agent（2026-10-06 新增）
                              （2026-10-06 起 retrieve 阶段挂知识图谱：
                               问题/工作流命中的节点追加跨条目事实到回答，
                               config.enable_graph / graph_json_path 控制）
  autonomous_learning/        自主学习：给任务，Agent 自己读懂未知 workflow（2026-10-06 新增）
  workflow_learning/          批量学习：扫描目录 → 学 → 记 → 幂等重跑（2026-10-06 新增）
                              （database_bridge.py：学习记录镜像进 comfyui_library/database；
                                ignore_nodes.py：布线节点忽略清单）
  learning_scheduler/         学习调度：定优先级 → 排队 → 执行 → 状态可续跑（2026-10-06 新增）
                              （判「已学」先查数据库 status，库里没有再回退 Markdown）
  knowledge_graph/            知识图谱：把 workflow/节点/模式/问题连成网，供跨条目查询（2026-10-06 新增）
                              （2026-10-06 起 co_used 与 nodes_without_cards
                               共享 workflow_learning 的布线节点忽略清单）
  workflow_index_manager.py   workflow / pattern 索引管理
```

## 5. 文档地图

| 想了解 | 读 |
|---|---|
| 总体架构 | `docs/architecture.md` |
| **版本号（唯一权威）** | `docs/roadmap.md` 第 3 节 |
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
4. **停下来汇报改动摘要，等用户明确要求才提交 / 推送**（见 3.1 推送纪律）。
   提交信息用中文短句。**不要自动 `git push`。**
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
| 门面 | `README.md` | ✅ 已入库；版本号收敛到 `docs/roadmap.md`，本文与 README 均不重复维护（`CHANGELOG.md` 已于 2026-10-05 删除，发布前改用 git tag + GitHub Releases） |

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
| 节点知识卡 | ✅ 452 张（16 张人工核对：6 张 SD1.5 基础卡 + 10 张高频卡；436 张自动起草于 2026-10-06，来源 `node-analysis/tools/draft_cards_from_workflows.py`——输入/输出槽与取值分布为 404 个 workflow 实测，作用为名称推断标 TODO(待验证)）+ `node_index.json` v1.2（auto_drafted 标记区分两类卡） |
| 布线节点忽略清单 | ✅ `engine/workflow_learning/ignore_nodes.py`（Note / Reroute / GetNode / SetNode / 注释、预览与 rgthree 分组控件等，不建卡、不计缺口；`node_frequency(exclude_ignored=True)` 排建卡优先级） |
| Pattern 卡 | ✅ 2 张（sd15-t2i-basic / sd15-t2i-lora） |
| 节点摘要 | ✅ 1 张（loraloader） |
| 真实 workflow 样本 | 🔶 仅 `workflows/sd1.5/` 有内容（`_workflow.json` / `_prompt.json` / `basic.json` / 两张 png）；`wan` / `flux` / `sdxl` 为空骨架 |
| 知识卡格式对齐 | 🔶 8 张 v0.2 遗产卡（`skills/comfyui-learning/knowledge/`）内容有效但**格式先于 v0.3.1 规范**，待迁移 |

**数据库层（`comfyui_library/database/`，2026-10-06 新增）**

| 内容 | 状态 |
|---|---|
| `WorkflowDatabase` 持久化核心 | ✅ utf-8-sig 读 / `version` 守卫 / 缺键回填 / 非法 JSON 带文件名报错；默认落 `database/storage/workflow_database.json`，`summary()` 一行摘要 |
| 四仓库 | ✅ workflow（增删查 + add/delete 对账 used_in + patterns 并集合并 + content_hash）/ node（register 带 category，只填空不覆盖）/ pattern（add 回填 workflow.patterns，悬空成员可见）/ experience（同 workflow_id 最新覆盖 + delete + `data` 结构化载荷） |
| `IndexManager` | ✅ 三个派生索引构建 + 落盘（workflow_index / node_index / pattern_index，`save_all()` 可重建） |
| 测试 | ✅ `engine/test_database.py`（23 组）+ 引擎接库集成 `engine/test_database_integration.py`（14 组），均从仓库根跑、全走 TemporaryDirectory |

**引擎层（`engine/`，v0.5 实装）**

14 个子包全部落地并有 `test_*.py` 覆盖；16 个测试脚本全部 exit=0（2026-10-06 复测，
6 个在 `engine/` 目录 + 10 个从仓库根，见 3.4）；同日新增 `comfyui_library/database/`
存储底座，配套 `test_database.py`（23 组）与引擎接库集成测试
`test_database_integration.py`（14 组）：

| 模块 | 能力 | 测试 |
|---|---|---|
| `models.py` / `workflow_loader.py` / `learning_engine.py` | 三个 Core Data Model（WorkflowObject / NodeInfo / LinkInfo）；JSON→WorkflowObject；`learn_workflow` 最小闭环 | `test_workflow_understanding.py` |
| `workflow_parser/` | JSON → 结构化解析；`KnowledgeLoader` 从 `node_index.json` / 知识卡自动填充 role / category / learning_topics；捕获 `widgets_values`；`parse_data` 可直接解析 dict；解析后自动写入上下文 | `test_parser.py` |
| `workflow_analyzer/` | `GraphBuilder` 图构建 + `ConnectionAnalyzer` 连接分析 + `PatternDetector` 模式识别 + `WorkflowClassifier` 分类 | `test_workflow_analyzer.py` |
| `diagnostics/` | `ParameterChecker`（KSampler widgets 提取 cfg / steps）+ `GraphChecker` 图结构检查 + `QualityChecker` 质量检查 + `rules.py` 规则表，输出问题与建议 | `test_diagnostics.py` |
| `context/` | dataclass 化 `WorkflowContext` / `ConversationContext` + `ContextManager`（精简接口 + last_update）+ 持久化 `context_store.json` | `test_context.py` |
| `response_generator/` | **双产出，无 LLM 依赖**：`generate()` 出给 LLM 的提示词；`answer(state)` 出给人读的 Markdown（全规则拼装）。新增 `AnswerBuilder`（结论/工作流现状/诊断分组/相关知识/下一步五段式）+ `KnowledgeDistiller`（把 241 行的知识卡按问题蒸馏成 3 段要点）| `test_response.py`、`test_answer.py`（10 组）|
| `learning_loop/` | `workflow_compare`（节点 / 参数差异）+ `improvement_analyzer`（改动影响推断）+ `experiment_tracker`（经验持久化 / 检索 / 按类型与标签过滤）；附 README / ARCHITECTURE / USAGE_EXAMPLE | `test_learning_loop.py` |
| `knowledge_evolution/` | **从「参数改动记录」归纳**：`ExperienceCollector`（learning_loop 经验归一化 + 节点清单补全）→ `PatternMiner`（节点组合频次 + 参数区间统计）→ `KnowledgeGenerator`（可读知识 + 风险提示）→ `KnowledgeStore`；主入口 `evolve()`。**局限**：`mine()` 用节点集合精确匹配（`tuple(sorted(set(nodes)))`），节点差一个就归不到同组，`knowledge_consolidation` 的聚类已改进但未回填到此 | `test_knowledge_evolution.py`（8 组）|
| `knowledge_consolidation/` | **从「完整 workflow」归纳**：`ExperienceLoader`（读 learning/*.md）→ `PatternMiner`（按 workflow_type 分组 + **Jaccard 相似度贪心聚类**，容忍额外节点、忽略 Note 类注释节点）→ `ParameterStatistics`（**逐模式统计**，含中位数/集中度，`seed` 等噪声参数排除）→ `KnowledgeBuilder`（**常见问题按骨架归并聚合** + 建议 + 跨模式对比，阈值复用 RISK_RULES）→ `KnowledgeStore`（Markdown 落盘到 `knowledge/patterns/_consolidated/`）；主入口 `ConsolidationEngine.consolidate()`；**接库**：`ExperienceLoader(database=)`
优先读 `experiences.data` 结构化载荷，库空回退 Markdown | `test_knowledge_consolidation.py`（21 组）|
| `retrieval/` | `KnowledgeIndex`（倒排索引 + 去重）→ `KnowledgeMatcher`（10 主题，中英混排 + 节点类型别名 + 症状词）→ `KnowledgeRanker`（工作流命中 +10 / 类型可信度 / 症状多成因）→ `KnowledgeRetriever.retrieve()` + `format_for_prompt()`；索引可从 `comfyui_library/knowledge` + 两个 store 自动构建 | `test_retrieval.py`（10 组）|
| `workflow_index_manager.py` | workflow / pattern 索引的增删改查 | 工具脚本，无单测 |
| `agent_core/` | **总控**：`AgentState`（各阶段产物 + `stages_run`/`stages_skipped`/`errors`/`answer`）+ `AgentPipeline`（阶段链，单阶段失败隔离）+ `DEFAULT_CONFIG`（阶段开关，未知键报错）+ `ComfyUIAgent.ask()`（返回 AgentState）/ `ask_text()`（直接返回中文回答字符串）。六阶段：context → parse → analyze → diagnose → retrieve → respond。离线能力 `evolve()` / `build_index()` / `set_workflow()` | `test_agent_core.py`（16 组，含真实模块端到端）|
| `autonomous_learning/` | **自主学习**：`TaskPlanner`（计划真依赖任务意图与节点特征）+ `WorkflowExplorer`（**推导 analyzer 不提供的生成流程链** Model→Condition→Latent→Sampling→Decode→Output）+ `KnowledgeGapDetector`（**两档缺口**：完全无知识 / 仅同族通用知识，别名感知）+ `SpecialAnalyzer`（执行计划里的专项步骤：ControlNet/LoRA/参数区间/复现基线/denoise 语义等）+ `Reflection`（量化自评 + 核心缺口封顶等级）+ `LearningReport`（渲染成人读报告）。主入口 `AutonomousLearner.learn()` / `learn_text()` | `test_autonomous_learning.py`（12 组，含真实 workflow 与未知节点两例）|
| `workflow_learning/` | **批量学习管理**：`WorkflowScanner`（`.json` + `.png`，**默认跳过 `_workflow.json`/`_prompt.json` 伴生文件与 `_learning/` 状态目录**；键用相对路径避免同名冲突）+ `LearningStore`（**Markdown 后端**，一个 workflow 一个 `.md`，内容指纹 sha256 判定重学，失败记录不算已学，`prune_missing` 清理失效记录，`node_frequency` 供挖模式用，自动维护 `index.md`）+ `markdown_format.py`（frontmatter 序列化/解析，仅标准库）+ `WorkflowLearner.learn()`（单文件：analyzer + explorer + retriever + gap_detector + diagnostics）+ `BatchWorkflowLearner.learn_folder()`（批量入口，幂等）；**接库**：`database=`
  传入时经 `database_bridge` 把每条记录镜像进 WorkflowDatabase，`sync_database()` 迁移存量 | `test_workflow_learning.py`（17 组，含幂等、内容变更重学、grep 可检索性）|
| `learning_scheduler/` | **学习调度**（只排队与状态，不重复实现学习逻辑）：`LearningTask`（key 用相对路径 + 状态机 pending/running/completed/failed/skipped/**abandoned**）+ `PriorityCalculator`（**内容信号主导**：节点数 +1/个、缺卡节点 +8/个、未见过的节点类型 +4/种、曾失败 +2/次、内容已变更 +5；文件名关键词缩放到 1 倍只作 tie-break）+ `TaskQueue`（优先级降序 + 稳定同分、**`retain_keys()` 增量合并而非 reset**、重试上限用尽转 abandoned 隔离）+ `SchedulerState`（从队列**计算**出来的投影，不独立维护）+ `ScheduleStore`（**Markdown 队列**，含 retry/错误/排序依据，可续跑）+ `LearningScheduler.build_schedule()/run()/resume()`；**接库**：判「已学」先查
  WorkflowDatabase.status（库无记录回退 Markdown），run 后镜像进库 | `test_learning_scheduler.py`（16 组，含重试跨次生效、异常隔离、歧义名不猜）|
| `knowledge_graph/` | **知识图谱**：`KnowledgeGraph`（**邻接索引** `_out`/`_in`，取邻居 O(出度) 而非 O(全部边)；同 id 顶点**属性合并**而非覆盖；加边按三元组去重）+ 8 种顶点（workflow/node/pattern/card/problem/solution/family/concept）+ 11 种关系（contains/requires/member_of/matches/has_problem/problem_in/suggests/has_card/covers/co_used/has_topic）+ `GraphBuilder`（从 LearningStore + KnowledgeStore + node_index.json 建图；**共现两阶段 + 阈值**，超大 workflow 排除；**未匹配的模式成员可见**不静默丢弃）+ `GraphQuery`（`workflows_using` 支持不完整节点名、`paths` 多跳 BFS、`neighborhood`、`nodes_without_cards` 按使用次数排建卡优先级、`describe/render` 人读输出）+ `GraphStore`（JSON 存读，**边属性不丢**、版本守卫、悬空边可见）。**顶点 id 带类型前缀**（`node:KSampler`）防同名跨类型覆盖 | `test_knowledge_graph.py`（26 组，含真实库端到端、歧义名不猜、悬空边往返）|

**两条新入口**（接在既有四条之后）：

```
学习调度（决定「先学什么」）：

    create_scheduler(learner).render_plan()   # 只看计划，不执行
    create_scheduler(learner).run()           # 执行队列
    create_scheduler(learner).resume()        # 中断续跑

    WorkflowScanner → build_schedule（查 LearningStore 跳过已学 + 读节点 + 打分）
                   → TaskQueue（优先级降序）
                   → run（循环取任务 → WorkflowLearner.learn → 更新状态）
                   → ScheduleStore（Markdown，可续跑）

    状态落 engine/learning_scheduler/learning_queue.md（可 grep）

知识图谱（决定「怎么跨条目查」）：

    build_graph(verbose=True)     # 从三个数据源建图并落 JSON

    WorkflowLearning 学习记录 ─┐
    Consolidation 归纳模式   ─┼→ GraphBuilder → KnowledgeGraph → GraphQuery
    node_index.json 知识卡   ─┘                          │
                                                     跨条目查询

    qy.workflows_using("ControlNetApply")   # 哪些流程用了它
    qy.problems_of("sdxl/portrait")          # 这个流程有哪些问题
    qy.nodes_without_cards()                 # 该先给哪些节点建卡
    qy.paths("KSampler", "ControlNetApply")  # 两者什么关系（多跳）
```

存储底座（不学习、只存与查；2026-10-06 新增，同日完成引擎接入）：

    Workflow Files
      ↓ workflow_learning（LearningStore 记录正身 + database_bridge 镜像）
    WorkflowDatabase（comfyui_library/database/storage/workflow_database.json）
      ├─ workflows    WorkflowRepository    workflow 增删查（status + content_hash 判重学）
      ├─ nodes        NodeRepository        节点 → used_in
      ├─ patterns     PatternRepository     模式 ↔ workflow（回填互引）
      ├─ experiences  ExperienceRepository  学习经验（含 data 结构化载荷，归纳引擎吃它）
      └─ indexes      IndexManager          workflow/node/pattern_index.json（派生，save_all 重建）
      ↓ 消费方
    learning_scheduler（查库判已学）／knowledge_consolidation（读库归纳）

引擎主链路（由 `agent_core` 串起，2026-10-06 首次端到端跑通）：

```
用户提问 (+ 可选 workflow)
  ↓
agent_core/ComfyUIAgent.ask()
  ├─ context      记录问题到会话上下文
  ├─ parse        workflow_parser    JSON → WorkflowKnowledge
  ├─ analyze      workflow_analyzer  图构建 / 模式识别 / 分类
  ├─ diagnose     diagnostics        参数 / 图结构 / 质量诊断
  ├─ retrieve     retrieval          关键词召回 + 排序（吃 workflow_nodes 加权）
  └─ respond      response_generator  产出 state.answer（人话，无 LLM）
                                    + state.response（LLM 提示词，可选）

最简用法（不需要 LLM）：
    agent.ask_text("为什么图很僵硬", workflow_json)   → 直接返回中文 Markdown

离线旁路：learning_loop → knowledge_evolution（evolve）、retrieval（build_index）

自主学习（另一条入口，给任务而非提问）：
    AutonomousLearner.learn(task, workflow_json)
        plan → explore → retrieve → detect_gaps → 专项分析 → reflect → report → deposit

批量学习（第三条入口，一次吃下一个目录）：
    create_batch_learner(...).learn_folder()   # 不传路径 = comfyui_library/workflows/
        扫描 → 查记录（比对内容指纹）→ 跳过已学
          → 逐个 learn → 写一条 Markdown 记录 → 汇总
        幂等：重跑全部跳过；文件内容变了自动重学
        记录落在 comfyui_library/workflows/learning/（Markdown，唯一存放处）

知识归纳（第四条入口，把一批记录变成通用规律）：
    create_consolidation_engine().consolidate()
        读 workflows/learning/*.md → 按类型分组 + Jaccard 聚类
          → 逐模式统计参数 → 聚合常见问题 → 生成建议
        产出落在 comfyui_library/knowledge/patterns/_consolidated/（Markdown）
```

**无 LLM 设计**：回答内容全部来自三处确定性数据源 —— diagnostics 的实测值 + 阈值判定、
知识卡的参数说明与常见错误、evolution store 的多经验统计。模板固定五段式
（结论 / 当前工作流 / 发现的问题 / 相关知识 / 下一步建议）。
不调 LLM 的代价是**开放性提问无法推理**（如「讲讲扩散原理」只能给知识卡原文要点），
这类需求才真正需要接模型。

### 9.2 进行中

**2026-10-07 下载学习流水线固化（learn_pipeline.py）**：把人肉八步
（收集→算缺失→下载→去重入库→学习→补卡→force 重学→图谱）固化为
`skills/comfyui-learning/tools/learn_pipeline.py` 一键执行，并修掉四个坑：
① 卡改为**学习前**按新批次文件预建（频次 ≥1 也建，`draft_for_files()`），
   首次学习的覆盖率即准，废除「学完补卡再 force 重学」的双遍浪费；
② 数据库死键自动对账（`database_bridge.cleanup_stale()`，此前已手工
   清过两次）；
③ 缺失 ID 以 manifest + 文件名后缀双口径计算；
④ 全程幂等，无新文件时各阶段自动空转。
端到端幂等验证通过，test_database / test_workflow_learning /
test_database_integration 全过。以后新工作流只需一条命令：
`python -X utf8 skills/comfyui-learning/tools/learn_pipeline.py`。

**2026-10-07 概念层补全（技法名可查）+ feeds_into 进回答**：
① GraphBuilder._mine_concepts() 从 workflow 标题按词表挖 26 个技法
概念（SelfLift/双采/数字人/首尾帧/去油…），workflow-[has_topic]->
concept 678 条；GraphQuery.workflows_using() 支持概念名反查，
新增 nodes_of_concept()（标志性节点聚合）。agent_core 问题文本
命中概念名时输出「技法出现在 N 个 workflow + 标志节点」。
② agent._collect_graph_facts() 接入 flows_of：回答附「通常从/
通常喂给（次数/数据类型）」。能力对比：SelfLift 查询 0 → 15 个
workflow；KSampler 问题从共现 5 条 → 含有向数据流 4 条。
重构 _collect_graph_facts 时曾把 facts 声明插进 for-else 结构
导致概念事实被清空——已修，教训：方法内插入代码块前先看清
既有分支结构。图谱 4974 顶点 / 58187 边。

**2026-10-07 宏观数据流入图（feeds_into）**：co_used 只说明
「一起出现」分不清谁喂谁。新增 REL_FEEDS_INTO 有向关系——
GraphBuilder._aggregate_dataflow() 用 workflow_analyzer 的
ConnectionAnalyzer 逐文件解析真实连线，按（源节点→目标节点）
聚合为 feeds_into 边（count = 多少个 workflow 这样连，
data_types = MODEL/LATENT/CONDITIONING/IMAGE 等类型分布；
布线节点跳过，同 workflow 内同源同宿只计一次）。
GraphQuery 新增 `top_flows(data_type)` / `flows_of(node, direction)`。
实测 1667 条有向边，结构性规律首次可见：CLIPTextEncode→KSampler 686、
TextEncodeQwenImage21→KSampler 380（Qwen 族专属编码路径）、
CLIPTextEncode→ConditioningZeroOut→KSampler 266/181（加速流指纹）、
UNETLoader→LoraLoaderModelOnly→…→KSampler 的 MODEL 链 715/615/577。
图谱 4596 顶点 / 54382 边。遗留：feeds_into 尚未接进 agent_core 回答。

**2026-10-07 派生索引失真修复**：发现
`database/storage/node_index.json` 停留在早期 sd1.5 时代（仅 8 个节点，
LoraLoaderModelOnly 不在内）——批量学习路径只写主库，从未重建派生索引。
修复：`learn_pipeline.py` 学习阶段 finally 里补 `db.indexes.save_all()`
（workflow/node/pattern 三索引随主库一起刷新），并手工重建了一次
（node_index 8 → 1621 个节点）。test_database /
test_database_integration 全过。

**2026-10-07 文生图第六批（+100，全库 1751 条）**：learn_pipeline
一键完成（NEWEST 流已榨干：扫 24 页 0 新增 → 改 RECOMMEND 续收
5144 个新 ID（已知累计 11679 / 平台总量 13941）→ 下载 100 → 入库
100（去重闸门拦 1502 个重复）→ 学习前预建卡 92 张 → 学习 100/100
零失败 → 死键对账 0 → 图谱 5447 顶点 / 63606 边）。
知识卡 1208 → **1300 张**。全库 1751 条：平均 74%，深懂（≥80%）
799 个，浅懂 2。本批来源以 HiDream/Flux 对比、洗图去 AI 味类为主。

**2026-10-07 文生图第五批（+100，全库 1551 条）**：learn_pipeline
一键完成（下载 100 → 预建卡 126 → 学习 100/100 零失败 → 图谱
4949 顶点 / 57559 边）。知识卡 1082 → **1208 张**。全库 1551 条：
平均 74%，深懂（≥80%）704 个，浅懂 2。

**2026-10-07 文生图第四批（+100，全库 1451 条）**：首次用
`learn_pipeline.py` 一键跑完全流程（收集 4003 → 下载 100 → 入库 100
→ **学习前预建卡 171 张** → 学习 100/100 零失败仅数十秒 → 死键对账
0 → 图谱 4596 顶点 / 52715 边）。预建卡生效：知识卡 911 → **1082 张**，
首轮覆盖率即准（无需 force 重学）。全库 1451 条：平均 74%，
深懂（≥80%）657 个，浅懂（<20%）1。顺手修流水线收集目标 bug
（固定 4 倍 → 现有清单 + 冗余，否则清单超限后永不收集）。

**2026-10-07 文生图第三批（+100，全库 1351 条）**：NEWEST 流续收
1300 后取库外前 100 下载导入（0 失败），新增节点 93 种 → 补卡
（818 → **911 张**），重学刷新后图谱 4155 顶点 / 49034 边 / 1300
workflow（去重后）。全库 1351 条：平均 74% / 中位数 77%，
深懂（≥80%）607 个，浅懂（<20%）4。NEWEST 已知 ID 累计 3203
（含 RECOMMEND 交叉），库外仍剩约 2200 个 ID 可继续增量收集。

**2026-10-07 文生图第二批（+200，全库 1251 条）**：NEWEST 流续收
100 个 + `--sort RECOMMEND` 推荐流续收 100 个，经与 git 基线指纹比对
**200 个均为真正的新工作流（0 重复）**——过程中曾误报「100 个重复」，
根因是导入已完成后又拿下载文件与库比对（自己比自己），验证重复
必须以 git 提交基线为参照。两批入库学习 0 失败（性能修复后整轮仅
62s），新增节点 119 种 → 补卡（699 → **818 张**），node_index v1.2。
图谱重建：3702 顶点 / 45273 边。全库 1251 条：平均 73% / 中位数 77%，
深懂（≥80%）554 个，浅懂（<20%）仅 4。经验：NEWEST 流之后可用
RECOMMEND 续收挖增量。

**2026-10-07 性能修复（批量学习慢的根因）**：用户反馈执行明显变慢，
剖析出三层瓶颈并全部修复：
1. **数据库逐条全量落盘**（主因）：`WorkflowRepository.add` 内部对每个
   节点 register 一次，每次都全量写 21MB JSON——200 节点的 workflow
   一次镜像 = 200 次全量写。修复：`WorkflowDatabase.auto_save` 开关
   （默认 True 行为不变），批量路径（`learn_folder` / `sync_all` /
   `sync_record`）统一改为整批只 save 一次，异常也保证落盘。
2. **索引全量重渲染**：`LearningStore.write` 每写一条就重读全部
   Markdown 渲染 index.md（千条时单次写 7s+）。修复：记录缓存
   `_cache`（key→record，惰性构建，write/remove 同步维护）。
3. `sync_record` 批量模式下重复落盘（自己引入的），改为仅在
   非批量调用时落盘。
实测：单文件学习（带库镜像）5.1s → **1.7s**；650+ 文件全量重跑
54s。注意库 21MB 后 `save()` 单次约 0.7-3s（indent=4），批量模式
下每轮只发生一次。另：当日中断的后台学习任务残留进程曾占用记录
文件导致测试 PermissionError，已清理——**后台任务取消后要确认
进程已退出**再跑测试。

**2026-10-07 RunningHub 下载（图片生成/文生图 +401）**：环境无
requests，`collect_by_tag.py` / `download_by_ids.py` 均已改为
标准库 `urllib` 兜底（接口行为与抓包事实一致）。收集续至 401，
下载 401 个新文生图工作流（0 失败），导入闸门拦截 501 个重复后
全部入库学习（0 失败），新增节点 93 种 → 补卡（606 → **699 张**）。
全库 **1051 条**：平均 74% / 中位数 77%，浅懂（<20%）0。
另：改用 urllib 后 412 例外数与之前一致（少数作者限制导出，
按 3.3 节登录态流程处理）。

**2026-10-07 视频生成目录分类（理解度实测）**：用户建
`workflows/视频生成/{图生视频,文生视频,视频生视频}` 三小类并把 146 个
H3 工作流平铺在根目录。按**学习记录的节点构成**分类（真视频加载器
VHS_LoadVideo/LoadVideo/HAIGC_VideoLoader → 视频生视频；仅 LoadImage →
图生视频；纯文本 → 文生视频），再解析 JSON 连线**穿透 GetNode/SetNode
追溯真实输入源**二次修正。结果 85/4/57，与文件名语义交叉验证一致率
约 77%；不一致的两种情况均查实：多参考工作流确实带视频输入（数据对，
命名泛化），以及个别文件名与内容不符（如「图生视频工作流」实际无任何
图像/视频输入节点，疑残缺导出——数据优先于命名）。分类后重学、
清死记录与库旧键 146 条，图谱重建 2379 顶点。

**2026-10-06 H3 视频批次入库（+146，全库 650 条）**：`download/` 根目录
与 `download/workflows-json/` 的 MiniMax H3 工作流经导入工具入库到
`图片生成/H3视频/`（146 个新文件，workflows-json 与根目录内容重叠被
指纹闸门拦截）。导入工具补两道闸门：JSON 必须解析为含 nodes 列表的
dict（拦截 ids-state 等状态文件）+ 可选库内目标子目录参数。
新增 H3 视频栈节点 126 种 → 补卡（知识卡 480 → **606 张**），
node_index v1.2。图谱重建：2378 顶点 / 26377 边 / 599 workflow（去重后）。
全库 650 条：平均 73% / 中位数 78%，深懂档（≥80%）302 个，浅懂 0；
H3 视频子批平均 74%——主项目方向的知识洼地已填平。
过程中发现文件被移动（嵌套 workflows-json/ → 平铺）导致 136 条
「文件不存在」失败记录，按同名平铺文件重学恢复，死记录与库旧键已清；
`test_store_aggregates` 夹具改为每条独立指纹（适配聚合层去重口径）。

**2026-10-06 原始数据导入管线**：新增
`skills/comfyui-learning/tools/import_workflows.py`——
`download/workflows-by-tag/`（原始收件箱）→ 指纹去重 →
`comfyui_library/workflows/`。三道闸门：与库内指纹比对（口径与
WorkflowLearner._hash_file 一致）、批次内去重、同名不同内容自动
改 `_dup` 后缀。首次实跑：下载目录 501 个文件全部与库内重复，
导入 0——现有批次已全覆盖。新工作流的标准流程：
import_workflows.py → learn_folder() → draft_cards_from_workflows.py。

**2026-10-06 聚合层内容去重**：504 条学习记录里 45 组内容完全相同
（96 条，同一 workflow 不同文件名/平台 id 重复上传）。重复会让聚合
统计虚高——最坏 2 倍（只在重复文件里出现的节点），且
`min_frequency=2` 的模式归纳可能被「同一文件传两遍」凑出假模式。
新增 `engine/workflow_learning/dedupe.py`（`dedupe_by_content_hash`，
按指纹保首次，空指纹全保留），接入三个消费方：
`LearningStore.node_frequency()/unique_records()`、
`GraphBuilder.build()`（workflow 504 → 453 顶点）、
`ExperienceLoader`（database 与 Markdown 两路都去重）。
学习层**不去重**——逐条记录是判重学/按 key 查找的基础。
同步放宽 `test_knowledge_consolidation` 的过时断言
（`source_count == len(records)` → `0 < source_count <= len(records)`）。

**2026-10-06 增量学习第二轮（+100 个 workflow，本批 504 个收口）**：
新放入 100 个 workflow，`learn_folder()` 幂等增量学完（0 失败）；
建卡工具再跑一轮为新增节点补 **28 张卡**（知识卡 452 → 480 张），
只对 100 条新记录 force 重学刷新覆盖率。全库 504 个：
平均 73% / 中位数 77%，深懂档（≥80%）222 个，浅懂（<20%）0 个。
图谱重建：1965 顶点 / 20917 边。
顺带修复：`GraphQuery.workflows_using()` 返回改为**确定性排序**——
此前按邻接表插入顺序返回，存读往返后顺序漂移，test F2 的
往返一致性断言失败。

**2026-10-06 建卡收尾（本批 404 个 workflow 学习闭环）**：
新增 `skills/comfyui-learning/node-analysis/tools/draft_cards_from_workflows.py`：
从 workflow JSON 提取输入/输出槽（真实字段名）与 widgets_values 取值分布，
为「用过但没卡」的节点批量起草 Generated 卡（作用只做名称推断并标注
TODO(待验证)，不编造）。一次产出 **436 张卡**（知识卡 16 → 452 张），
node_index 升 v1.2（新增 auto_drafted 标记）。全量重学后：

- 平均覆盖率 **53% → 73%**（中位数 76%），深懂档（≥80%）48 → 177 个，
  浅懂（<20%）35 → **0 个**
- 图谱重建：1805 顶点 / 17626 边，无孤立点无悬空边
- 剩余浅区集中在超大整合流（166 节点的小岚整合版 22%）与
  Wan 数字人（24%）——其节点多为出现 <2 次的长尾，未达建卡阈值
- 忽略清单补充 rgthree 的 Fast Groups Muter/Bypasser（UI 分组控件）

**2026-10-06 知识图谱接进回答链路（同日第二轮）**：
- `agent_core` 的 retrieve 阶段新增 `_collect_graph_facts()`：问题文本或
  当前 workflow 命中的节点，从图谱取「被多少个已学 workflow 使用 +
  共现最密的伙伴（按 strength 排序）」，respond 阶段以
  「## 跨条目知识图谱」小节追加到 `state.answer` 末尾；
  事实同时存 `state.graph_facts`。Agent 默认从
  `graph_json_path`（engine/knowledge_graph/knowledge_graph.json）
  加载已落盘的图——init 不现场建图（那要扫全部学习记录），
  没建过图就记 skip，不报错
- `knowledge_graph` 的 co_used 共现与 `nodes_without_cards()` 建卡优先级
  接入 `workflow_learning.ignore_nodes` 忽略清单：重建后 co_used
  6238 → 4397 条（布线节点配对全部剔除），建卡优先级不再被
  Note/GetNode 霸榜。图谱规模 1693 顶点 / 20641 边
- 遗留（同待办 18）：`matches` 边仍为 0（归纳模式卡成员是合成数据，
  待重跑 consolidation）

**2026-10-06 知识飞轮首轮（批量学习 + 建卡）**：
`comfyui_library/workflows/` 扩充到 **404 个真实 workflow**（Qwen Image 2.1 为主，
含 H3 / Krea2 / FLUX / SDXL / Seedance 等），`workflow_learning` 批量学习全部学完
（0 失败），学习记录与 `WorkflowDatabase`（404 workflow / 639 节点 / 404 experience）
同步。据此完成「学习 → 统计 → 建卡」首轮闭环：

- 新增 `ignore_nodes.py` 布线节点忽略清单（Note / Reroute / GetNode / SetNode /
  注释与预览类），缺口检测不再把纯布线节点算成知识缺口，
  `node_frequency(exclude_ignored=True)` 供建卡优先级排序
  （否则 GetNode/SetNode 以 4600+ 次出现永久霸榜）
- 从 404 条记录统计参数分布，起草 10 张高频节点知识卡（可信度 Generated，
  卡内标注实测分布），`node_index.json` 升 v1.1（6 → 16 张卡）
- 修复 `test_workflow_learning` D5 的过时断言（写测试时样本只有 3 个，
  硬编码 `total_found == 3`，样本扩充后必然失败；改为与扫描结果对账）
- 注意：D5 会备份→清空→重学→还原真实 learning 目录，
  改学习逻辑后磁盘记录要**另跑一次 `learn_folder(force=True)`** 才会持久化

**v0.5 引擎实装**：Phase 1（Workflow Loader）✅、Phase 2（analyzer 三件）✅ 之后，
又完成了 context 上下文引擎、response_generator 回答生成、diagnostics 诊断引擎、learning_loop 学习循环、
knowledge_evolution 知识演化、retrieval 知识检索、**agent_core 总控**（后三者 2026-10-06 完成）。

**2026-10-06 端到端首次跑通**：`agent_core` 把十个模块串成六阶段 Agent，
用 `comfyui_library/workflows/sd1.5/basic.json`（7 节点）实跑，13 条知识带排序分数召回，
耗时约 6.6ms。诊断链路用构造的异常参数验证过（能报出 CFG 过高 / Steps 过低 / 缺 VAEDecode）。

**同日实现无 LLM 回答链路**（用户明确不引入 LLM）：`ResponseGenerator.answer()` +
`AnswerBuilder` + `KnowledgeDistiller`，Agent 现在能直接输出人话 Markdown，
不调模型、不联网。`state.response`（LLM 提示词）保留但降为可选产物。

**同日实现自主学习模块**：`autonomous_learning` 补齐了项目最后一块能力 ——
「给 Agent 一个任务，它自己去读懂未知 workflow」。实测能推导生成流程链、
逐节点检索知识、发现两档知识缺口（完全无知识 / 仅同族通用知识）、
量化自评理解程度并产出可读报告。

**同日实现批量学习模块**：`workflow_learning` 补上「一次吃下一个目录」的入口。
实测 `comfyui_library/workflows/` 3 个文件（1 json + 2 png，含 PNG 元数据提取）
全部学完，64ms，幂等重跑全部跳过，内容改动自动重学。

**同日再实现两个模块**（各带一份独立设计，本次按设计落地时修了若干会直接出错的地方）：

- **`learning_scheduler`**：回答「先学什么、学到哪、哪些学不了」。与 `workflow_learning`
  的分工是「它执行学习，调度器只排队与状态」。落地时相对设计稿改了 7 处，其中一处是
  **老问题的复现**：设计稿用 `registry.exists(wf["name"])` 按文件名去重，
  而这里必须用 `store.exists(key, content_hash)` —— 否则改了参数永远不重学，
  且不同目录的同名 workflow 互相覆盖。
- **`knowledge_graph`**：把学习记录 + 归纳模式 + 知识卡索引连成网，回答跨条目问题
  （「哪些人像流用了 ControlNet」）。实测真实库 43 顶点 / 90 边 / 0 悬空边，
  存读往返一致。落地时把设计稿的单层 `contains` 边扩到 8 种顶点 × 11 种关系，
  并给顶点 id 加类型前缀（裸 id 会让 `sd1.5/basic` 与 `sdxl/basic` 互相覆盖）。

**同日修复的集成缺陷**（均为串起来才暴露，单模块单测查不出）：
- `WorkflowParser` 收路径而 `WorkflowAnalyzer` 收 dict
- `task_type` 占位串 `"unknown"` 是真值，会挡掉真实分类
- `set_workflow()` 登记的工作流在后续追问中不复用
- `workflow_parser/__init__.py` 是空文件（其他包都导出类）
- 诊断 `issue_type` 实际值（`parameter_warning`/`missing_node`/`workflow_warning`）与分类表对不上
- `retrieval` 建索引时用 snake_case 文件名去查 `node_index.json` 的 PascalCase 键，
  **永远查不到** → 知识卡元信息全空、`node` 字段退化成文件名，
  导致覆盖率统计把「有卡」算成「没卡」（实测 100% → 14%）
- `GraphChecker.check(None)` 崩溃（`DiagnosticEngine.analyze` 的 graph 参数并非可选）

**新模块落地时踩到的同类坑（都是「声明了但没人填 / 有人在用但没定义」）**：
- `LearningTask.retry_count` 字段存在但无人使用 → 永久损坏的文件被无限重试，
  队列永远卡在同一批文件上，调度器等于死锁
- `SchedulerState` 的 `total_tasks`/`completed` 无处赋值 → 改成从队列**计算**的投影，
  否则两处状态各自漂移
- `pop_next()` 在去重检查**之前**就把状态改成 `running` → 任务卡在 running 永远不结束
- `build_schedule` 里的 `queue.reset()` 把 retry 历史一起清掉 → 第二次 run 的重试计数归零，
  永久失败的文件重新被无限重试。改成 `retain_keys()` 增量合并
- `queue or TaskQueue(max_retries=...)`：`TaskQueue` 定义了 `__len__`，
  **空队列是 falsy**，调用方传进来的队列连同 `max_retries` 被默认值悄悄顶掉，
  表现为「重试上限怎么设都不生效」。`__init__` 一律用 `is None` 判断
- `KnowledgeGraph.add_node` 直接 `nodes[id] = node` → 后一个 workflow 里的
  `KSampler` 会把前一个已挂好的知识卡属性冲掉；`add_edge` 无去重，重建一次边就翻倍
- `REVERSE_RELATIONS` 字典在它引用的 `REL_COVERS` 常量**之前**求值 → 导入即 NameError
- `GraphStore.save` 丢 `properties`、没有 `load`、没有版本号 → builder 写在边上的
  count/strength 全蒸发，且旧结构文件会被当成新结构读

**同日新增存储底座 `comfyui_library/database/`（Workflow Knowledge Database）**：
分工边界是「engine 管怎么学，database 管学到了什么」—— 只负责 workflow / node /
pattern / experience 四类数据的保存与统一查询，不含任何学习逻辑。
落地时相对设计稿修了 9 处：

- `__init__.py` 漏导出 `IndexManager`；storage/ 列了三个索引文件却只有
  `build_workflow_index()` 一个方法还不落盘 → 补齐三索引构建 + `save_all()`
- 读 JSON 用 utf-8 → 改 `utf-8-sig`（硬约定 3.3）
- 数据文件无版本号 → 加 `version` 守卫（GraphStore 踩过的坑）
- `load()` 不回填缺键 → 旧文件缺 section 会 KeyError，改为 setdefault 回填
- `add()` 只写 workflow 自身字段 → `workflow.nodes` 与 `node.used_in`
  两份状态必然漂移，改为 add/delete 时自动对账反向索引
- `pattern.workflows` 与 `workflow.patterns` 互为引用各写各的 →
  PatternRepository.add 回填，WorkflowRepository.add 对 patterns 并集合并防抹掉
- `NodeRecord.category` 定义了但 register 没处填（「声明了但没人填」）→
  register 加可选 category（只填空，不覆盖已有值）
- 标题「增删查」却没有 delete → 补 WorkflowRepository.delete（连带清 used_in）
  与 ExperienceRepository.delete；删 workflow 不连带删 patterns/experiences，
  悬空保持可见（与 knowledge_graph 对悬空边同一处理）
- 便捷入口：WorkflowDatabase 直接挂 `.workflows / .nodes / .patterns /
  .experiences / .indexes`，不必手工 new 仓库

**同日完成引擎接库（database 成为数据层枢纽）**：新增
`engine/workflow_learning/database_bridge.py` 作为 LearningRecord ↔ 库的翻译层，
三个模块接入（database 参数不传则行为与旧版完全一致，显式开启）：

- `workflow_learning`：`BatchWorkflowLearner(…, database=)` / `create_batch_learner(database=)`
  在 Markdown 落盘后把记录镜像进库（workflow 记录 + 经验结构化载荷）；
  `sync_database()` 对存量记录做一次性迁移。skipped 记录不镜像
- `learning_scheduler`：判「已学」先查库的 `workflow.status + content_hash`
  （`database_bridge.is_learned`：库里没有的 key 返回 None → 回退查 Markdown，不猜；
  status 非 learned 或指纹对不上 → 判需重学）；`run()` 学完写 Markdown 后同样镜像进库
- `knowledge_consolidation`：`ExperienceLoader(database=)` / `create_consolidation_engine(database=)`
  优先从 `experiences.data` 的结构化载荷读（只取 completed；库里一条没有时回退
  读 Markdown 并打印提示，不静默切换）

接库时对模型的两处扩展：`WorkflowRecord` 补 `content_hash`（调度器判重学必需，
只看 status 会让改了参数的文件永远不重学）；`ExperienceRecord` 补 `data` 载荷
（归纳引擎要的是 parameters / problems 等结构化字段，content 只是给人看的摘要）。

接库后发现的问题，已在**同日真实链路实跑**（用 sd1.5 真实 workflow 把
学习 → 库 → 调度 → 归纳 → 图谱 → 问答全环节过一遍）中修掉四个：

- `create_batch_learner()` 默认产出的 `WorkflowLearner` 是**空壳**
  （六模块全 None），学出的记录没有类型 / 参数 / 知识覆盖 / 体检 ——
  现在默认自动装配真实模块（`auto_modules=False` 保留空壳给最小依赖测试）
- `ComfyUIAgent()` 同病：六阶段全部跳过，`ask_text` 永远回
  「暂时无法生成回答」—— 现在默认自动装配（存储路径一律取 config，
  测试塞假模块不受影响）
- `KnowledgeRetriever(dict)` 会把磁盘上的真实 `retrieval_store.json`
  一并加载进 dict 知识库（`KnowledgeIndex` 构造即读盘）—— dict 被磁盘
  内容污染，此前测试能过纯属侥幸。`KnowledgeIndex` 加 `auto_load` 开关，
  dict 模式不再读盘
- `WorkflowRepository` 存的记录缺 `id` 字段（`all()` 出来的记录说不清自己是谁）

另把 `parameters` / `discoveries` 写进 Markdown frontmatter（dict 用行内 JSON），
**Markdown 往返不再丢字段**。真实库 3 条记录已带完整 frontmatter 重学并迁移，
归纳首次产出参数统计（宽度 / 高度 / 步数的中位数与区间），
模式已写回数据库（`pattern_index` 1 条，`workflow.patterns` 同步回填）。

`engine/__init__.py` 仍只导出 `LearningEngine`，未对外暴露 `ComfyUIAgent`（待办第 1 项）。
Phase 3-5（knowledge_writer / pattern_manager）尚未实装。

### 9.3 待办（按优先级）

1. **对外暴露统一入口**：`engine/__init__.py` 只导出 `LearningEngine`（一个 2026-10-04 的
   最小闭环类），十四个子包的能力完全没对外暴露。应改为导出 `ComfyUIAgent` + `create_agent()`，
   并加 CLI（`python -m engine ask "问题" --workflow xx.json`）
2. **workflow 自动喂给演化**：`learning_loop` 的原始经验不含节点清单，
   `knowledge_evolution` 只能靠 `register_nodes()` 人工补。agent_core 已有解析结果，
   应在 `ask()` 里把节点清单回写，让 evolve() 能自动工作（现在需人工构造）
3. **实战首跑（2026-10-06 已完成大半）**：`comfyui_library/workflows/` 已扩到 404 个真实
   workflow 并全部学完。剩余：按 `node_frequency(exclude_ignored=True)` 的频次继续
   起草高频节点卡（现有 16 张，缺卡节点仍有 600+ 种），并扩充主题表覆盖；
   `{wan,flux,sdxl}/` 目录仍是空骨架（样本实际落在 `图片生成/` 下）
4. **产出 workflow_manifest.json**：`skills/comfyui-learning/scanner/tools/build_manifest.py`
   已有该能力，但学习记录已统一到 `comfyui_library/workflows/learning/*.md`，
   manifest 应改为读 `learning/index.md`（避免两套 learned 状态不一致）
5. **补齐 Phase 3-5**：`knowledge_writer`（产出 `knowledge/workflows/` 五件套）→ `pattern_manager`
   （`pattern_index.json` 至今未建立，是 SKILL.md 要求的三索引之一。
   注意 2026-10-06 起 `comfyui_library/database/storage/` 下有一个同名
   `pattern_index.json`，那是数据库的派生查询索引，不是本条要的 Skill 层索引）
6. **归纳知识接进检索**：`knowledge_consolidation` 的产出（`knowledge/patterns/_consolidated/`）
   目前是独立目录，`retrieval._index_pattern_cards` 只扫 `patterns/*.md`，
   不扫子目录 —— 所以归纳出的模式**检索不到**。需让 retriever 递归或显式索引该目录
7. **knowledge_evolution 聚类缺陷回填**：它的 `PatternMiner.mine()` 仍是节点集合精确匹配，
   `knowledge_consolidation` 已改成 Jaccard 聚类但两边并存未打通。
   数据源不同（改动记录 vs 完整 workflow）所以不算重复，但算法应统一，否则长期发散
8. **重跑归纳与图谱（样本已就位）**：样本已扩到 404 个 workflow（2026-10-06），
   但 `knowledge_consolidation` 的现有模式卡仍是早期合成数据，
   `knowledge_graph` 也未重建——需用全量样本重跑 consolidation 与 build_graph，
   并处理同名不同 id 的重复上传样本（约 1/4）
9. **知识卡格式统一化**：`KnowledgeDistiller` 现在按 Markdown 标题切段，
   但 `knowledge/patterns/*.md` 的标题层级不统一（有的用 H3 分组、有的用加粗），
   蒸馏出的片段偶尔混入 ASCII 示意图残片（如 sd15-t2i-basic 的节点连线图）。
   统一 Pattern 卡格式后可显著提升蒸馏质量
10. **测试入口统一**：6 个旧 `test_*.py` 改用 `from engine.xxx` 包导入，使其可从仓库根运行
   （现状 10 个测试已符合，6 个旧的仍只能在 `engine/` 目录跑）
11. **专项阈值需用真实样本校准**：`analysis_steps.PARAM_EXPECTATIONS` 的
   cfg/steps/ControlNet 权重等阈值全来自通行经验（已标 `TODO(待验证)`）。
   等 `comfyui_library/workflows/` 攒够样本，应改由 `knowledge_consolidation`
   的统计区间驱动，与风险提示口径统一
12. **文档修正**：补写缺失的 `docs/implementation-plan.md`（旧状态文档曾引用它但文件不存在），或删掉相关引用；
   为 knowledge_evolution / retrieval / agent_core / autonomous_learning / workflow_learning /
   knowledge_consolidation / learning_scheduler / knowledge_graph 八模块补设计文档
   （15 个模块中仅 learning_loop 有）
13. **发布准备（v1.0 前）**：仓库目前零 git tag，版本号无 git 层面标记；
    首次对外发布时用 `git tag v1.0.0` + GitHub Releases 承载 release notes 与 breaking changes
14. **RAG v0.4 实装**：embedding 接入；统一 `build_index`（text 键）与 `search_database`（content 键）
    的键名；`prepare_documents` 的 content 从 `str(item)` 改为规范拼装
15. **knowledge/ 卡片对齐 v0.3.1**：格式迁移 + 补 MiniMax H3 与 Wan 的差异对照卡（wan 卡内 TODO）
16. **遗留清理（用户未决）**：旧 `workflow_analysis/`（复数）目录与现行 `workflow/`（单数）内容重叠；
    `memory/learning_records.md`、`workflow_index.json` 旧格式是否并入 memory 子技能体系
17. **`knowledge_graph` 接进检索与回答（2026-10-06 已完成主链路）**：
    `agent_core` 的 retrieve 阶段已查图并把跨条目事实追加进回答。
    剩余：`retrieval._index_pattern_cards` 仍只扫 `patterns/*.md`
    不扫 `_consolidated/`（同待办 6）；图谱事实目前只有
    使用者/共现两类，问题边（problem_in）与多跳路径还没接进回答
18. **`knowledge_graph` 的 matches 边目前为空**：`knowledge/patterns/_consolidated/`
    里的 3 张模式卡成员是早期演示时的合成数据（`sd15_basic_0.json`、`sdxl_portrait_0.json` 等），
    库里并不存在这些 workflow，所以真实图的 `matches` 边为 0。
    `GraphBuilder` 会把这些成员记进 `unmatched_members` 并报匹配率（不静默丢弃，
    也不猜着连边）。需先按待办 3/8 扩充真实样本再重跑 consolidation
19. **调度器与图谱的共现算法重复**：`learning_scheduler.PriorityCalculator` 的
    「未见过的节点类型」与 `knowledge_graph` 的 `co_used` 共现都在数节点对。
    数据源不同（前者扫待学文件、后者扫已学记录）可以并存，
    但两边的「新颖度」口径应共享一份定义，否则长期发散（同待办 7 的性质）
20. **引擎接库收尾**（2026-10-06 已打通：workflow_learning 写库镜像 /
    scheduler 查库判已学 / consolidation 读库并写回模式，真实库已完成迁移，
    剩两件）：
    - `agent_core` 的 retrieve/respond 仍未查库；`knowledge_graph` 建图仍直读
      Markdown，未消费 `database/storage/` 的三个派生索引
    - 三个派生索引与 retrieval 倒排索引的口径统一（同待办 7 的性质）

### 9.4 维护规则

1. 改动任何子技能 / 工具 / 引擎模块 → 提交信息用**中文短句**描述模块与动作
2. 完成一批开发 → **必须**更新 9.1 / 9.2 / 9.3 与顶部「最后更新」日期
3. 新增顶层文件 → 同步在 `.gitignore` 加 `!/<文件名>`，否则不会被跟踪
4. 新增子技能 → 照既有结构（skill.md + `*_rules.md` + `*_schema.json` + README.md + templates|tools）
5. 工具脚本与引擎代码：只依赖标准库；读 JSON 用 `utf-8-sig`；
   **改动后必须自测**（`engine/` 目录下 `python test_*.py`，确认 exit=0）再提交
6. 文档竖排流程图一律用代码块包裹（防 GitHub 渲染粘连）
7. 不确定的内容标 `TODO(待验证)`，禁止编造参数
8. **提交 / 推送节奏由用户控制**：改完汇报改动摘要即可，
   未经用户明确要求不得 `git add` / `git commit` / `git push`（见 3.1 推送纪律）
