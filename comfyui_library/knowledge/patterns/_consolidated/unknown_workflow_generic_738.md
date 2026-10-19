---
name: unknown_workflow_generic_738
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.504
common_nodes: [AppendImageBatch, CR Prompt Text, ImageConcatMulti, ImageFromBatch+, JWInteger, RH_LLMAPI_Pro_Node, SaveImage, SaveText, ShellAgentPluginOutputText, ShowAnything|Mie, VHS_LoadVideo, VHS_VideoInfo, easy forLoopEnd, easy forLoopStart, easy imageConcat, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/2046474090080378881.json, 视频生成/图生视频/2041794960168591361.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_738

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2046474090080378881.json、视频生成/图生视频/2041794960168591361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `AppendImageBatch`
- `CR Prompt Text`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `JWInteger`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `SaveText`
- `ShellAgentPluginOutputText`
- `ShowAnything|Mie`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageConcat`
- `easy mathInt`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
