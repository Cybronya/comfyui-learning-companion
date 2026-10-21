---
name: unknown_workflow_upscale_lora_sampler_17
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImageJPG_GH, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize, CR Text, Text Concatenate (JPS)]
members: [图片生成/图生图/2089694393820340226.json, 图片生成/图生图/2102580135840018433.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json, 视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2089694393820340226.json、图片生成/图生图/2102580135840018433.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088069964401041409.json、视频生成/图生视频/flux2-klein-TTP分块放大+_+轻量版 (1)_2088143314515226625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImageJPG_GH`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Flux2Scheduler` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Joy_caption_two_advanced` —— 1/4 个有
- `Joy_caption_two_load` —— 1/4 个有
- `OllamaCaptionerExtraOptions` —— 1/4 个有
- `PainterFluxImageEdit` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `Text Concatenate (JPS)` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy imageBatchToImageList、easy imageColorMatch、easy imageListToImageBatch、easy imageSize
