# Project Status（项目开发状态记忆）

> 本文件是 ComfyUI Learning Companion 的工作记忆。
> 任何 Agent / 协作者接手前先读本文件；每次开发完成后必须更新本文件对应章节。

- 最后更新：2026-10-04
- 规则版本：v0.3.1（规范定稿）｜v0.4 架构标准化 ✅｜**v0.5 设计文档已入库（Learning Engine，引擎实现未开始）**
- 仓库：https://github.com/Cybronya/comfyui-learning-companion （public，分支 master）

---

## 1. 项目定位

基于 AI Agent 的 ComfyUI 知识学习框架：把大量零散 Workflow 转化为结构化知识
（分析 → 提取 → Pattern 发现 → 个人知识库 → AI 学习助手）。
**不做**：自动运行 Workflow、自动下载模型、替代用户创作。

## 2. 仓库与环境约定

- 仓库根：`F:\Program Files\ComfyUI`（本地），git 身份 cybronya / wangxinloo@163.com（仓库局部配置）
- `.gitignore` 白名单制：只跟踪 `skills/`、`comfyui_library/`、`docs/`、`README.md`、`CHANGELOG.md`，其余全部忽略
- GitHub 访问走本地代理 127.0.0.1:3067；**push 失败（Empty reply / SSL handshake）= 代理掉线**，等恢复后 `git push origin master` 重试即可，镜像前缀只能用于下载不能用于 push
- 提交身份与凭据：曾在对话中明文出现过的 PAT 建议已轮换；日常推送优先 `git push origin master`

## 3. 已完成（从底到顶）

| 模块 | 路径 | 状态 |
|---|---|---|
| 顶层规范 | `skills/comfyui-learning/SKILL.md` | ✅ v0.3.1 定稿（角色/五职责/输出规范/版本限制） |
| Workflow 规则 | `skills/comfyui-learning/workflow/` | ✅ 三件套：analysis / template / compare |
| Workflow Scanner | `skills/comfyui-learning/scanner/` | ✅ 三规范 + `tools/` 四脚本（实测跑通，读 JSON 用 utf-8-sig） |
| Node Analysis | `skills/comfyui-learning/node-analysis/` | ✅ 规范 + `tools/` 三脚本（AST 提类，实测跑通） |
| Model Management | `skills/comfyui-learning/model-management/` | ✅ 规范 + `tools/` 三脚本（四类型识别实测全对） |
| RAG | `skills/comfyui-learning/rag/` | 🔶 接口占位（v0.4 实装）：四模块函数级验证通过，`__main__` 为 pass |
| Workflow Explanation | `skills/comfyui-learning/workflow-explanation/` | ✅ 规则 + explanation_schema + 四模板 |
| Troubleshooting | `skills/comfyui-learning/troubleshooting/` | ✅ 规则 + error_schema + 三模板 |
| Memory | `skills/comfyui-learning/memory/` | ✅ 规则 + memory_schema + 三模板（三级可信度 Confirmed/Generated/Temporary） |
| Project Knowledge | `skills/comfyui-learning/project-knowledge/` | ✅ 规则 + knowledge_schema + 三模板 |
| Core 框架 | `skills/_core/` | 🔶 骨架（skill-discovery / loading / standard / registry 占位） |
| 对外文档 | `docs/` | ✅ 9 篇全部入库：architecture / workflow-schema / knowledge-system / skill-system / workflow-analysis / pattern-learning / roadmap（v0.4 七篇）+ **learning-engine.md / engine-api.md（v0.5 设计，含引擎五模块+models.py、Core Data Model、全 API 定义与 CLI）**。v0.5 文档链（architecture → skill-system → learning-engine → engine-api → workflow-analysis → pattern-learning → knowledge-system）已在 engine-api.md 第 19 节固化 |
| 门面 | `README.md` / `CHANGELOG.md` | ✅ 已入库 |

知识卡（v0.2 遗产）：`skills/comfyui-learning/knowledge/` 下 nodes×3、models×3、concepts×2 共 8 张，内容有效但**格式先于 v0.3.1 规范**，待对齐。

## 4. 当前进行中

- **v0.5 Learning Engine**：设计文档已全部入库（`docs/learning-engine.md` 流程设计 + `docs/engine-api.md` API 设计），**代码实现未开始**。注意 API 设计比流程设计多一个模块：engine/ 实际为六文件（五模块 + `models.py`，Core Data Model：WorkflowObject / AnalysisResult / KnowledgeObject）

## 5. 待办（下一步，按优先级）

1. **实战首跑**：向 `comfyui_library/workflows/{wan,flux,sdxl}/` 放入第一批真实 workflow（json+分析 md），跑通 scanner → workflow 分析 → explanation 全链路，产出 `workflow_manifest.json`
2. **v0.5 Learning Engine 实装**：按 `docs/learning-engine.md` 第 14 节 + `docs/engine-api.md` 实现 engine/ 六文件（含 models.py 三个 Core Data Model；API、SkillContext、EngineResult、CLI 均已在 engine-api.md 定稿）
3. **RAG v0.4 实装**：embedding 接入；统一 `build_index`（text 键）与 `search_database`（content 键）的键名；`prepare_documents` 的 content 从 `str(item)` 改为规范拼装
4. **knowledge/ 卡片对齐 v0.3.1**：格式迁移 + 补 MiniMax H3 与 Wan 的差异对照卡（wan 卡内 TODO）
5. **pattern_index 尚未建立**：SKILL.md Memory 管理要求的三索引之一（workflow_index ✅ 已有 / pattern_index ❌ / learning_records ✅ 已有）
6. **遗留清理（用户未决）**：旧 `workflow_analysis/`（复数）目录与现行 `workflow/`（单数）内容重叠；`memory/learning_records.md`、`workflow_index.json` 旧格式是否并入 memory 子技能体系

## 6. 关键事实与资源指针

- ComfyUI 本体与 custom_nodes：本仓库即 ComfyUI 本体安装目录（`custom_nodes/`、`models/` 在根下）
- 自定义节点来源**权威清单**：`F:\Program Files\Git\openi\ComfyUI-Minimax-H3\comfyui\custom_nodes\NODES_SOURCES.md`（用户主项目仓库，涉及"哪个插件/上游是谁"先读它）
- Workflow 知识库目录：`comfyui_library/workflows/{wan,flux,sdxl}/`（当前为空骨架，.gitkeep 占位）
- 主项目背景：用户围绕 ComfyUI MiniMax H3（视频生成）工作

## 7. 维护规则（给后续 Agent）

1. 改动任何子技能 / 工具 → 提交信息用中文短句描述模块与动作
2. 完成一批开发 → 更新本文件的「已完成 / 进行中 / 待办」与「最后更新」日期
3. 新增子技能 → 照既有结构（skill.md + *_rules.md + *_schema.json + README.md + templates|tools）
4. 工具脚本：只依赖标准库；读 JSON 用 `utf-8-sig`；改动后必须用临时数据自测再提交
5. 文档竖排流程图一律用代码块包裹（防 GitHub 渲染粘连）
6. 不确定的内容标 `TODO(待验证)`，禁止编造参数
