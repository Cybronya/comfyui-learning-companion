---
name: unknown_workflow_sampler_clip_unet_329
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91025
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein移除_局部重绘工作流_2013104344488480770.json, 图片生成/图生图/Klein单图像编辑（头发飘动版）_2052707351915966465.json, 平台全量/Flux2-klein一键移除_2099022893144436737.json, 平台全量/Flux2-klein移除流和局部重绘+高清放大工作流_2031248244512133122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_329

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-klein移除_局部重绘工作流_2013104344488480770.json、图片生成/图生图/Klein单图像编辑（头发飘动版）_2052707351915966465.json、平台全量/Flux2-klein一键移除_2099022893144436737.json、平台全量/Flux2-klein移除流和局部重绘+高清放大工作流_2031248244512133122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 3/4 个有
- `LayerUtility: ColorImage V2` —— 3/4 个有
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `LayerUtility: ImageBlend` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `取色器_孤海` —— 2/4 个有
- `GetImageSize+` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LG_LoadImage` —— 1/4 个有
- `LayerUtility: ColorPicker` —— 1/4 个有
- `MasksToMaskList` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `TTP_Image_Assy` —— 1/4 个有
- `TTP_Image_Tile_Batch` —— 1/4 个有
- `TTP_Tile_image_size` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
