---
name: unknown_workflow_generic_1288
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [GroundingDinoModelLoader (segment anything2), GroundingDinoSAMSegment (segment anything), ImpactDilateMask, JoinImageWithAlpha, LoadImage, MaskBlur+, SAMModelLoader (segment anything), SaveImage]
problems: []
missing: []
members: [图片生成/图生图/sim-双层背景锯齿修复抠图_2003432165843058689.json, 图片生成/图生图/双层背景锯齿修复抠图_2003311540587593729.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1288

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/sim-双层背景锯齿修复抠图_2003432165843058689.json、图片生成/图生图/双层背景锯齿修复抠图_2003311540587593729.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `GroundingDinoModelLoader (segment anything2)`
- `GroundingDinoSAMSegment (segment anything)`
- `ImpactDilateMask`
- `JoinImageWithAlpha`
- `LoadImage`
- `MaskBlur+`
- `SAMModelLoader (segment anything)`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 1/2 个有
- `MaskFillHole` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
