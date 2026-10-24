---
name: unknown_workflow_generic_1589
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CR Prompt Text, LoadImage, RH_LLMAPI_Pro_Node, SaveImage, ShellAgentPluginOutputText, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/AI图生剧本_2039001758223044609.json, 视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1589

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/AI图生剧本_2039001758223044609.json、视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 1/2 个有
- `RHMiniMaxH3T2VATextEncode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
