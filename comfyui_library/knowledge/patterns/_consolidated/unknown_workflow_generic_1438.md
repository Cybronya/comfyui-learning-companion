---
name: unknown_workflow_generic_1438
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [AddMask, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, LoadImage, RemoveWatermarkNode, SAMModelLoader (segment anything), SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键全自动去除图片水印_1902342370677960706.json, 图片生成/图生图/最强一键图片去水印_1934210404744912898.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1438

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键全自动去除图片水印_1902342370677960706.json、图片生成/图生图/最强一键图片去水印_1934210404744912898.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `LoadImage`
- `RemoveWatermarkNode`
- `SAMModelLoader (segment anything)`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `MaskToImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
