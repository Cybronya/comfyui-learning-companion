---
name: unknown_workflow_generic_1545
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.873
common_nodes: [LayerUtility: TextJoin, LoadImage, RH_RhartImageNG31FlashImageToImage, SaveImage, TextInput_, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/服装白底图生成_2063799102713982978.json, 图片生成/图生图/电商模特服装拆解生成白底图_2064738937620492290.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1545

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/服装白底图生成_2063799102713982978.json、图片生成/图生图/电商模特服装拆解生成白底图_2064738937620492290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: TextJoin`
- `LoadImage`
- `RH_RhartImageNG31FlashImageToImage`
- `SaveImage`
- `TextInput_`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
