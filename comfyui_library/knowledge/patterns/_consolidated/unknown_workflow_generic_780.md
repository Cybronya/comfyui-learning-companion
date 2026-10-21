---
name: unknown_workflow_generic_780
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.866
common_nodes: [CR Prompt Text, HAIGC_LoadImagesFromZip, Int, RunningHubRVCOneClickTrain, ShellAgentPluginOutputText, easy saveText]
problems: []
missing: []
members: [图片生成/文生图/RVC模型训练器_2101876081258229762.json, 音频生成/音频生成/心然·寻源-RVC模型训练器_2100912929473392642.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_780

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/RVC模型训练器_2101876081258229762.json、音频生成/音频生成/心然·寻源-RVC模型训练器_2100912929473392642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `HAIGC_LoadImagesFromZip`
- `Int`
- `RunningHubRVCOneClickTrain`
- `ShellAgentPluginOutputText`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
