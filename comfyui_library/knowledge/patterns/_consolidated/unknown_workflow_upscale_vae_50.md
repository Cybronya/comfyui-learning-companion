---
name: unknown_workflow_upscale_vae_50
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.815
common_nodes: [Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, MathExpression|pysssss, PreviewImage, PrimitiveFloat, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/建筑_角色通用放大-seedvr2_2049762190231609346.json, 图片生成/图生图/建筑效果图套A0大板8k放大工作流_2011999694133665794.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/建筑_角色通用放大-seedvr2_2049762190231609346.json、图片生成/图生图/建筑效果图套A0大板8k放大工作流_2011999694133665794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
