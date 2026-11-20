---
name: unknown_workflow_generic_1328
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, Comfly_Doubao_Seedance2_0_Asset, Comfly_api_set, LoadImage, SaveImage, ShellAgentPluginOutputText, ShowAnything|Mie]
problems: []
missing: []
members: [图片生成/反推提示词/（图像资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2042637519245807617.json, 图片生成/反推提示词/（音频资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2043143353923014658.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1328

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/（图像资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2042637519245807617.json、图片生成/反推提示词/（音频资产）Seedance2.0 真人ID资产库提取(贞贞的AI工坊)_2043143353923014658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Comfly_Doubao_Seedance2_0_Asset`
- `Comfly_api_set`
- `LoadImage`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `ShowAnything|Mie`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `LoadAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
