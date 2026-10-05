# Project Status（项目开发状态记忆）

> 本文件是 ComfyUI Learning Companion 的**实时状态**记忆。
> 任何 Agent / 协作者接手前先读本文件与根目录 `AGENTS.md`；每次开发完成后必须更新本文件对应章节。
> 稳定的约定（环境、命令、硬规则、模块地图）在 `AGENTS.md`，本文件不重复，只记会变的状态。

- 最后更新：2026-10-05
- 规则版本：v0.3.1（规范定稿）｜v0.4 架构标准化 ✅｜v0.5 设计文档已入库 + **引擎实装进行中（已越过 Phase 1）**
- 仓库：https://github.com/Cybronya/comfyui-learning-companion （public，分支 master）
- 入口文档：`AGENTS.md`（根目录，接手先读）

---

## 1. 项目定位

基于 AI Agent 的 ComfyUI 知识学习框架：把大量零散 Workflow 转化为结构化知识
（分析 → 提取 → Pattern 发现 → 个人知识库 → AI 学习助手）。
**不做**：自动运行 Workflow、自动下载模型、替代用户创作。

## 2. 仓库与环境约定

详见 `AGENTS.md` 第 3 节。要点复述：

- 仓库根：`F:\Program Files\ComfyUI`（同时是 ComfyUI 本体安装目录），git 身份 cybronya / wangxinloo@163.com
- `.gitignore` 白名单制：只跟踪 `AGENTS.md` / `README.md` / `CHANGELOG.md` / `docs/` / `skills/` /
  `comfyui_library/` / `engine/`；**新增顶层文件必须同步加 `!/<文件名>`**
- GitHub 访问走本地代理 127.0.0.1:3067（Karing）；**push 失败（Empty reply / SSL handshake /
  Failed to connect over proxy）= 代理掉线**，恢复后 `git push origin master` 重试；
  镜像前缀只能用于下载不能用于 push
- Python 3.12.10；工具脚本只依赖标准库；读 JSON 用 `utf-8-sig`
- 测试必须在 `engine/` 目录内运行 `python test_*.py`（6 个脚本用裸导入，根目录 `python -m` 会失败）

## 3. 已完成

### 3.1 文档层

| 模块 | 路径 | 状态 |
|---|---|---|
| 对外文档 | `docs/` | ✅ 10 篇：architecture / workflow-schema / knowledge-system / skill-system / workflow-analysis / pattern-learning / pattern_evolution / roadmap / learning-engine / engine-api |
| 入口文档 | `AGENTS.md` | ✅ 2026-10-05 新增：环境 + 硬约定 + 测试方式 + 模块地图 + 文档地图 |
| 门面 | `README.md` / `CHANGELOG.md` | ✅ 已入库（CHANGELOG 仍停在 v0.3.1，见待办 6） |

### 3.2 Skill 层（`skills/`）

| 模块 | 路径 | 状态 |
|---|---|---|
| 顶层规范 | `comfyui-learning/SKILL.md` | ✅ v0.3.1 定稿（角色 / 五职责 / 输出规范 / 版本限制） |
| Workflow 规则 | `comfyui-learning/workflow/` | ✅ 三件套：analysis / template / compare |
| Scanner | `comfyui-learning/scanner/` | ✅ 三规范 + `tools/` 四脚本（实测跑通） |
| Node Analysis | `comfyui-learning/node-analysis/` | ✅ 规范 + `tools/` 三脚本（AST 提类，实测跑通） |
| Model Management | `comfyui-learning/model-management/` | ✅ 规范 + `tools/` 三脚本（四类型识别实测全对） |
| Workflow Explanation | `comfyui-learning/workflow-explanation/` | ✅ 规则 + schema + 四模板 |
| Troubleshooting | `comfyui-learning/troubleshooting/` | ✅ 规则 + schema + 三模板 |
| Memory | `comfyui-learning/memory/` | ✅ 规则 + schema + 三模板（三级可信度 Confirmed/Generated/Temporary） |
| Project Knowledge | `comfyui-learning/project-knowledge/` | ✅ 规则 + schema + 三模板 |
| RAG | `comfyui-learning/rag/` | 🔶 接口占位：四模块函数级验证通过，`__main__` 为 pass |
| Core 框架 | `_core/` | 🔶 骨架（skill-discovery / loading / standard / registry 占位） |

### 3.3 知识库（`comfyui_library/`）

| 内容 | 状态 |
|---|---|
| 节点知识卡 | ✅ 6 张（Checkpoint / CLIPTextEncode / EmptyLatent / KSampler / SaveImage / VAEDecode）+ `node_index.json` v1.0（含 role / difficulty / learning_topics） |
| Pattern 卡 | ✅ 2 张（sd15-t2i-basic / sd15-t2i-lora） |
| 节点摘要 | ✅ 1 张（loraloader） |
| 真实 workflow 样本 | 🔶 仅 `workflows/sd1.5/` 有内容（`_workflow.json` / `_prompt.json` / `basic.json` / 两张 png）；`wan` / `flux` / `sdxl` 为空骨架 |
| 知识卡格式 | 🔶 8 张 v0.2 遗产卡（`skills/comfyui-learning/knowledge/`）内容有效但**格式先于 v0.3.1 规范**，待对齐 |

### 3.4 引擎层（`engine/`，v0.5 实装）

七个模块全部落地并有 `test_*.py` 覆盖，7 个测试脚本在 `engine/` 目录下全部 exit=0（2026-10-05 复测）：

| 模块 | 路径 | 能力 | 测试 |
|---|---|---|---|
| 核心模型与加载 | `models.py` / `workflow_loader.py` / `learning_engine.py` | 三个 Core Data Model（WorkflowObject / NodeInfo / LinkInfo）；JSON→WorkflowObject；`learn_workflow` 最小闭环 | `test_workflow_understanding.py` |
| Workflow 解析 | `workflow_parser/` | JSON → 结构化解析；`KnowledgeLoader` 从 `node_index.json` / 知识卡自动填充 role / category / learning_topics；捕获 `widgets_values`；`parse_data` 可直接解析 dict；解析后自动写入上下文 | `test_parser.py` |
| Workflow 分析 | `workflow_analyzer/` | `GraphBuilder` 图构建 + `ConnectionAnalyzer` 连接分析 + `PatternDetector` 模式识别 + `WorkflowClassifier` 分类 | `test_workflow_analyzer.py` |
| 诊断引擎 | `diagnostics/` | `ParameterChecker`（KSampler widgets 提取 cfg / steps）+ `GraphChecker` 图结构检查 + `QualityChecker` 质量检查 + `rules.py` 规则表，输出问题与建议 | `test_diagnostics.py` |
| 上下文引擎 | `context/` | dataclass 化 `WorkflowContext` / `ConversationContext` + `ContextManager`（精简接口 + last_update）+ 持久化 `context_store.json` | `test_context.py` |
| 回答生成 | `response_generator/` | `QuestionAnalyzer` 问题分析 + `PromptBuilder` 上下文提示词构建 + 知识注入 + `ResponseTemplate`（**替代原 teaching 骨架，lesson_generator 已删除**） | `test_response.py` |
| 学习循环 | `learning_loop/` | `workflow_compare`（节点 / 参数差异）+ `improvement_analyzer`（改动影响推断）+ `experiment_tracker`（经验持久化 / 检索 / 按类型与标签过滤）+ `experience_store.json`；附 README / ARCHITECTURE / USAGE_EXAMPLE | `test_learning_loop.py` |
| 索引管理 | `workflow_index_manager.py` | workflow / pattern 索引的增删改查 | 工具脚本，无单测 |

当前引擎主链路：

```
Workflow JSON
  → workflow_parser      解析 + 知识注入
  → workflow_analyzer    图构建 / 模式 / 分类
  → diagnostics          参数 / 图结构 / 质量诊断
  → response_generator   回答生成
        ↓
  learning_loop          用户改工作流 → 对比 → 改进分析 → 经验积累
```

## 4. 当前进行中

**v0.5 引擎实装**：Phase 1（Workflow Loader）✅、Phase 2（analyzer 三件）✅ 之后，
又完成了 context 上下文引擎、response_generator 回答生成、diagnostics 诊断引擎、learning_loop 学习循环。
原 implementation-plan 的 Phase 3-5（knowledge_writer / pattern_manager / learning_engine 完整串联 + CLI）
尚未实装，且 plan 文件本身缺失（`docs/implementation-plan.md` 不存在，状态文档曾引用它 → 见待办 5）。

引擎目前是**多个可独立运行的能力模块**，尚未由单一入口串联；`engine/__init__.py` 只导出 `LearningEngine`。

## 5. 待办（按优先级）

1. **统一引擎入口与串联**：CLI（`python -m engine learn`）+ 把 parser → analyzer → diagnostics →
   response_generator → learning_loop 串成一条链；`engine/__init__.py` 目前只导出 `LearningEngine`，
   实际能力面远大于此
2. **实战首跑**：向 `comfyui_library/workflows/{wan,flux,sdxl}/` 放入第一批真实 workflow（json + 分析 md），
   跑通 scanner → 解析 → 诊断 → 回答全链路，产出 `workflow_manifest.json`
3. **补齐 Phase 3-5**：`knowledge_writer`（产出 `knowledge/workflows/` 五件套）→ `pattern_manager`
   （`pattern_index.json` 至今未建立，是 SKILL.md 要求的三索引之一）
4. **测试入口统一**：6 个 `test_*.py` 改用 `from engine.xxx` 包导入，使其可从仓库根
   `python -m engine.test_xxx` 直接运行（现状只有 `test_learning_loop.py` 符合）
5. **文档修正**：补写缺失的 `docs/implementation-plan.md`（或删掉对它的引用）；
   修正 `project-status.md` 旧版「9 篇文档」计数（实为 10 篇）
6. **CHANGELOG 补记**：仍停在 v0.3.1，v0.4 / v0.5 与全部引擎模块均未入账
7. **RAG v0.4 实装**：embedding 接入；统一 `build_index`（text 键）与 `search_database`（content 键）
   的键名；`prepare_documents` 的 content 从 `str(item)` 改为规范拼装
8. **knowledge/ 卡片对齐 v0.3.1**：格式迁移 + 补 MiniMax H3 与 Wan 的差异对照卡（wan 卡内 TODO）
9. **遗留清理（用户未决）**：旧 `workflow_analysis/`（复数）目录与现行 `workflow/`（单数）内容重叠；
   `memory/learning_records.md`、`workflow_index.json` 旧格式是否并入 memory 子技能体系

## 6. 关键事实与资源指针

- ComfyUI 本体与 custom_nodes：本仓库即 ComfyUI 本体安装目录（`custom_nodes/`、`models/` 在根下）
- 自定义节点来源**权威清单**：
  `F:\Program Files\Git\openi\ComfyUI-Minimax-H3\comfyui\custom_nodes\NODES_SOURCES.md`
  （用户主项目仓库，涉及"哪个插件/上游是谁"先读它）
- Workflow 知识库目录：`comfyui_library/workflows/{wan,flux,sdxl,sd1.5}/`（仅 sd1.5 有真实样本）
- 主项目背景：用户围绕 ComfyUI MiniMax H3（视频生成）工作
- 引擎数据落盘：`engine/context/context_store.json`（上下文）、`engine/learning_loop/experience_store.json`（经验）

## 7. 维护规则（给后续 Agent）

1. 改动任何子技能 / 工具 / 引擎模块 → 提交信息用**中文短句**描述模块与动作
2. 完成一批开发 → **必须**更新本文件的「已完成 / 进行中 / 待办」与「最后更新」日期
   （2026-10-05 教训：文档曾落后代码十余个 commit，context / diagnostics / learning_loop 等模块均未入账；
   根因是新增模块后没回头更新本文件。现已加 `AGENTS.md` 作为入口强化此流程）
3. 新增顶层文件 → 同步在 `.gitignore` 加 `!/<文件名>`，否则不会被跟踪
4. 新增子技能 → 照既有结构（skill.md + `*_rules.md` + `*_schema.json` + README.md + templates|tools）
5. 工具脚本与引擎代码：只依赖标准库；读 JSON 用 `utf-8-sig`；**改动后必须自测**
   （`engine/` 目录下 `python test_*.py`，确认 exit=0）再提交
6. 文档竖排流程图一律用代码块包裹（防 GitHub 渲染粘连）
7. 不确定的内容标 `TODO(待验证)`，禁止编造参数
