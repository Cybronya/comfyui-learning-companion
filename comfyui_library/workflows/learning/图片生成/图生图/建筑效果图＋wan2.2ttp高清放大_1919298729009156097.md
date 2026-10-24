---
key: 图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json
name: 建筑效果图＋wan2.2ttp高清放大_1919298729009156097
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json
hash: 88f2b370d673383c
coverage: 0.855263
learned_at: 2026-10-23 12:51:11
nodes: [AIO_Preprocessor, ShowText|pysssss, VAEDecode, ControlNetLoader, ControlNetApplyAdvanced, CheckpointLoaderSimple, PreviewImage, ControlNetLoader, ApplyFBCacheOnModel, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, IPAdapterUnifiedLoader, CLIPVisionLoader, EmptyLatentImage, LayerUtility: GetImageSize, ControlNetApplyAdvanced, AIO_Preprocessor, KSampler, PreviewImage, CLIPTextEncode, LoadImage, RH_Captioner, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, IPAdapterAdvanced, easy compare, easy int, easy int, easy ifElse, easy ifElse, easy showAnything, easy showAnything, easy showAnything, VAEDecodeTiled, UNETLoader, CLIPTextEncode, VAEEncodeTiled, easy forLoopEnd, SimpleMath+, SimpleMath+, ImageResize+, Get Image Size, SeedVR2BlockSwap, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageSize, ImageSharpen, easy imageColorMatch, ImageResize+, easy batchAnything, easy imageCount, ImageFromBatch, easy showAnything, ImpactMinMax, SeedVR2, easy imageBatchToImageList, easy imageListToImageBatch, ImageUpscaleWithModel, UpscaleModelLoader, KSampler, ModelSamplingSD3, VAELoader, ConstrainImage|pysssss, TTP_Image_Assy, ImageCASharpening+, PreviewImage, ColorMatch, PathchSageAttentionKJ, CLIPTextEncode, easy forLoopStart, easy cleanGpuUsed, SaveImage, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "比鲁斯建筑景观室内大模型_0.40B_PRO.safetensors", "controlnet_strength": 0.7500000000000001, "denoise": 0.10000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 760269860150679, "steps": 3, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/建筑效果图＋wan2.2ttp高清放大_1919298729009156097.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `AIO_Preprocessor`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `ControlNetLoader`
- `ApplyFBCacheOnModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `IPAdapterUnifiedLoader`
- `CLIPVisionLoader`
- `EmptyLatentImage` ★核心
- `LayerUtility: GetImageSize`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `RH_Captioner`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `IPAdapterAdvanced`
- `easy compare`
- `easy int`
- `easy int`
- `easy ifElse`
- `easy ifElse`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncodeTiled` ★核心
- `easy forLoopEnd`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResize+`
- `Get Image Size`
- `SeedVR2BlockSwap`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `ImageSharpen`
- `easy imageColorMatch`
- `ImageResize+`
- `easy batchAnything`
- `easy imageCount`
- `ImageFromBatch`
- `easy showAnything`
- `ImpactMinMax`
- `SeedVR2`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `ConstrainImage|pysssss`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `PreviewImage`
- `ColorMatch`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `easy cleanGpuUsed`
- `SaveImage`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.7500000000000001`
- `checkpoint` = `比鲁斯建筑景观室内大模型_0.40B_PRO.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `760269860150679`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **86%**（65/76）

**有卡**：`AIO_Preprocessor`、`VAEDecode`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`CheckpointLoaderSimple`、`ApplyFBCacheOnModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`IPAdapterUnifiedLoader`、`CLIPVisionLoader`、`EmptyLatentImage`、`LayerUtility: GetImageSize`、`KSampler`、`LoadImage`、`RH_Captioner`、`LoraLoaderModelOnly`、`IPAdapterAdvanced`、`easy compare`、`easy int`、`VAEDecodeTiled`、`UNETLoader`、`VAEEncodeTiled`、`easy forLoopEnd`、`SimpleMath+`、`ImageResize+`、`Get Image Size`、`SeedVR2BlockSwap`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageSize`、`ImageSharpen`、`easy imageColorMatch`、`easy batchAnything`、`easy imageCount`、`ImageFromBatch`、`ImpactMinMax`、`SeedVR2`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ModelSamplingSD3`、`VAELoader`、`ConstrainImage|pysssss`、`TTP_Image_Assy`、`ImageCASharpening+`、`ColorMatch`、`PathchSageAttentionKJ`、`easy forLoopStart`、`easy cleanGpuUsed`、`SaveImage`、`CLIPLoader`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
