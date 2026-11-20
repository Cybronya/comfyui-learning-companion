---
name: unknown_workflow_sampler_clip_unet_426
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.947667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json, 平台全量/超级修复无损放大TTP分块放大  klein SeedVR2 目前效果最好_2072848289875193857.json, 平台全量/（自动化-B）MSQupscale_1.0合成工作流_2118267543982006273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_426

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/（自动化）MSQcompose_1.2合成工作流_2116567648644452354.json、平台全量/超级修复无损放大TTP分块放大  klein SeedVR2 目前效果最好_2072848289875193857.json、平台全量/（自动化-B）MSQupscale_1.0合成工作流_2118267543982006273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `NumberComparison` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_DolaSeedream50ProImageToImage` —— 1/3 个有
- `math_calculate` —— 1/3 个有
- `ttN int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
