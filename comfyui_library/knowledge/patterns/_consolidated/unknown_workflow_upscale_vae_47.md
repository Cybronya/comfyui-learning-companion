---
name: unknown_workflow_upscale_vae_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.744
common_nodes: [Image Comparer (rgthree), ImageBlur, ImageCASharpening+, ImageResize+, LayerUtility: BooleanOperatorV2, LayerUtility: SaveImagePlus, LoadImage, MathExpression|pysssss, PrimitiveBoolean, PrimitiveInt, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, ZML_SwitchOutput, easy cleanGpuUsed, easy ifElse, easy imageScaleDownBy, easy imageSizeByLongerSide, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/seedVR2_产品放大_2111751139820654594.json, 图片生成/图生图/seedVR2_实拍放大_2108477817993392129.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/seedVR2_产品放大_2111751139820654594.json、图片生成/图生图/seedVR2_实拍放大_2108477817993392129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageBlur`
- `ImageCASharpening+`
- `ImageResize+`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: SaveImagePlus`
- `LoadImage`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `ZML_SwitchOutput`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageScaleDownBy`
- `easy imageSizeByLongerSide`
- `easy imageSizeBySide`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
