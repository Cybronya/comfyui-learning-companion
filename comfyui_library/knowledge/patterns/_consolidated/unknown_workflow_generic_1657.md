---
name: unknown_workflow_generic_1657
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7085
common_nodes: [BiRefNetRMBG, ImageCropByMask, ImpactSEGSToMaskList, LoadImage, MaskToSEGS, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/九宫格切下的NPC、敌人生成三视图+抠图+切割_2092518029019144193.json, 平台全量/抠图+分割_2092125821828943873.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1657

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/九宫格切下的NPC、敌人生成三视图+抠图+切割_2092518029019144193.json、平台全量/抠图+分割_2092125821828943873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNetRMBG`
- `ImageCropByMask`
- `ImpactSEGSToMaskList`
- `LoadImage`
- `MaskToSEGS`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/2 个有
- `StringReplace` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
