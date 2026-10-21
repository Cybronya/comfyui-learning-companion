---
name: unknown_workflow_upscale_sampler_clip_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.885
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, Fast Bypasser (rgthree), Image Comparer (rgthree), ImageGridSplitNode, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, Int, JjkText, KSamplerSelect, LoadImage, Mute / Bypass Repeater (rgthree), PreviewImage, RH_Captioner_Pro, RH_Nano_Banana2_Gemini31Flash, RH_RhartImageG2ImageToImage, RH_RhartVideoSparkvideo20MiniImageToVideo, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SaveVideo, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageInsetCrop, easy imageListToImageBatch, easy imageSize, easy imagesSplitImage, easy showAnything, kkMergeVideos]
problems: []
missing: []
members: [视频生成/图生视频/2074158653199970305.json, 视频生成/图生视频/2074158159417135105.json, 视频生成/图生视频/2073770723931418626.json, 视频生成/图生视频/2073280704120709122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2074158653199970305.json、视频生成/图生视频/2074158159417135105.json、视频生成/图生视频/2073770723931418626.json、视频生成/图生视频/2073280704120709122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `Fast Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageGridSplitNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `RH_Captioner_Pro`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartVideoSparkvideo20MiniImageToVideo`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageInsetCrop`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imagesSplitImage`
- `easy showAnything`
- `kkMergeVideos`

**可变部分**（部分 workflow 才有）：
- `Switch image [Crystools]` —— 2/4 个有
- `RH_SeedreamV5ProImageToImage` —— 1/4 个有
- `SaveImageJPG_GH` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
