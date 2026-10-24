---
name: unknown_workflow_upscale_sampler_clip_16
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.797571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader_Any, CLIPTextEncode, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json, 图片生成/图生图/flux2-klein-TTP分块放大+_+轻量版_2085538612657086465.json, 图片生成/图生图/flux2-klein-TTP分块放大_四视图放大专用_2096880958858416130.json, 图片生成/图生图/flux2-klein-TTP分块放大_四视图放大专用_2097172513771048962.json, 图片生成/图生图/flux2-klein-ttp高清放大_去噪真实感还原_2093238016969109506.json, 图片生成/图生图/flux2-klein-ttp高清放大_去噪真实感还原_2093509996926562305.json, 图片生成/图生图/klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json、图片生成/图生图/flux2-klein-TTP分块放大+_+轻量版_2085538612657086465.json、图片生成/图生图/flux2-klein-TTP分块放大_四视图放大专用_2096880958858416130.json、图片生成/图生图/flux2-klein-TTP分块放大_四视图放大专用_2097172513771048962.json、图片生成/图生图/flux2-klein-ttp高清放大_去噪真实感还原_2093238016969109506.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
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
- `GetNode` —— 6/7 个有
- `Image Overlay` —— 6/7 个有
- `ImageNoiseAugmentation` —— 6/7 个有
- `KuwaharaBlur` —— 6/7 个有
- `LayerMask: BiRefNetUltraV2` —— 6/7 个有
- `LayerMask: LoadBiRefNetModelV2` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `MaskPreview+` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `SaveImageJPG_GH` —— 5/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/7 个有
- `Mask Invert` —— 4/7 个有
- `AddMask` —— 2/7 个有
- `GoohaiUniversalSlider` —— 2/7 个有
- `GrowMaskWithBlur` —— 2/7 个有
- `easy sam3ImageSegmentation` —— 2/7 个有
- `easy sam3ModelLoader` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
