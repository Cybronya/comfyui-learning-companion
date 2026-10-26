---
name: unknown_workflow_upscale_sampler_clip_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7135
common_nodes: [Any Switch (rgthree), AutoCropFaces, BasicGuider, BasicScheduler, BetterFilmGrain, CLIPTextEncode, CheckpointLoaderSimple, DF_Int_to_Float, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize+, GetImageSizeAndCount, GetNode, Image Bloom Filter, Image Chromatic Aberration, Image Comparer (rgthree), Image H264 Compression (mtb), Image Lucy Sharpen, Image Paste Face, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, Label (rgthree), LoadImage, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, PreviewImage, RandomNoise, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy anythingIndexSwitch, easy imageBatchToImageList, easy imageListToImageBatch, easy int, easy seed]
problems: []
missing: []
members: [图片生成/文生图/专业人像高清 大分辨率模糊图片 小分辨率模糊图片即可_1915063664146321409.json, 数字人/数字人/图片高清放大-阿浩_2026856926528675842.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/专业人像高清 大分辨率模糊图片 小分辨率模糊图片即可_1915063664146321409.json、数字人/数字人/图片高清放大-阿浩_2026856926528675842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AutoCropFaces`
- `BasicGuider`
- `BasicScheduler`
- `BetterFilmGrain`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DF_Int_to_Float`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Bloom Filter`
- `Image Chromatic Aberration`
- `Image Comparer (rgthree)`
- `Image H264 Compression (mtb)`
- `Image Lucy Sharpen`
- `Image Paste Face`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `MathExpression|pysssss`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `RandomNoise`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
