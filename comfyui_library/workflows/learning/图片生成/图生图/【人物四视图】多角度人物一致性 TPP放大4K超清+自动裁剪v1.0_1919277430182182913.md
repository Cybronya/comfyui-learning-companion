---
key: 图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json
name: 【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json
hash: d9a57d40ce53a05a
coverage: 0.923077
learned_at: 2026-10-23 11:49:25
nodes: [LyingSigmaSampler, ImageListToImageBatch, InspyrenetRembg, StringFunction|pysssss, TTP_Tile_image_size, ImageScaleToTotalPixels, Florence2Run, RandomNoise, TTP_Image_Assy, FluxGuidance, easy cleanGpuUsed, TTP_Image_Tile_Batch, easy cleanGpuUsed, ImpactImageBatchToImageList, KSamplerSelect, VAEEncode, VAEDecodeTiled, SamplerCustomAdvanced, CLIPTextEncode, BasicGuider, BasicScheduler, GetImageSize, InvertMask, Image Overlay, CR Color Panel, CLIPTextEncode, ControlNetApplySD3, FluxGuidance, easy imageSize, EmptyLatentImage, VAEDecode, easy clearCacheAll, easy cleanGpuUsed, KSampler, CR Color Panel, Image Overlay, Image Overlay, Image Overlay, Image Overlay, ImageCrop, ImageCrop, ImageCrop, ImageCrop, Image Batch, CLIPTextEncode, ShowText|pysssss, SaveImage, VAELoader, Anything Everywhere3, Anything Everywhere, Anything Everywhere, ShowText|pysssss, SaveImage, ETN_Translate, Florence2Run, LoadImage, CR Text Concatenate, ETN_Translate, Florence2ModelLoader, UNETLoader, DualCLIPLoader, ControlNetLoader, CR Upscale Image, LoraLoader, LoadImage]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.7000000000000002, "denoise": 1, "height": 512, "lora_name": "F.1-小红书真实写真_FLUX-小红书真实写真.safetensors", "sampler_name": "deis", "scheduler": "beta", "seed": 31713104784309, "steps": 25, "strength_clip": 1, "strength_model": 0.8, "width": 512}
---

# 图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【人物四视图】多角度人物一致性 TPP放大4K超清+自动裁剪v1.0_1919277430182182913.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `LyingSigmaSampler` ★核心
- `ImageListToImageBatch`
- `InspyrenetRembg`
- `StringFunction|pysssss`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `Florence2Run`
- `RandomNoise`
- `TTP_Image_Assy`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `ImpactImageBatchToImageList`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `BasicScheduler`
- `GetImageSize`
- `InvertMask`
- `Image Overlay`
- `CR Color Panel`
- `CLIPTextEncode` ★核心
- `ControlNetApplySD3` ★核心
- `FluxGuidance`
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `CR Color Panel`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `ImageCrop`
- `ImageCrop`
- `ImageCrop`
- `ImageCrop`
- `Image Batch`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `SaveImage`
- `VAELoader`
- `Anything Everywhere3`
- `Anything Everywhere`
- `Anything Everywhere`
- `ShowText|pysssss`
- `SaveImage`
- `ETN_Translate`
- `Florence2Run`
- `LoadImage`
- `CR Text Concatenate`
- `ETN_Translate`
- `Florence2ModelLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ControlNetLoader`
- `CR Upscale Image`
- `LoraLoader` ★核心
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `controlnet_strength` = `0.7000000000000002`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `31713104784309`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `F.1-小红书真实写真_FLUX-小红书真实写真.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **92%**（60/65）

**有卡**：`LyingSigmaSampler`、`ImageListToImageBatch`、`InspyrenetRembg`、`StringFunction|pysssss`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`Florence2Run`、`RandomNoise`、`TTP_Image_Assy`、`FluxGuidance`、`easy cleanGpuUsed`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`KSamplerSelect`、`VAEEncode`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`BasicGuider`、`BasicScheduler`、`GetImageSize`、`InvertMask`、`Image Overlay`、`CR Color Panel`、`ControlNetApplySD3`、`easy imageSize`、`EmptyLatentImage`、`VAEDecode`、`easy clearCacheAll`、`KSampler`、`ImageCrop`、`Image Batch`、`SaveImage`、`VAELoader`、`ETN_Translate`、`LoadImage`、`CR Text Concatenate`、`Florence2ModelLoader`、`UNETLoader`、`DualCLIPLoader`、`ControlNetLoader`、`CR Upscale Image`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader
