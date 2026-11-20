---
key: 平台全量/Product Photography Relight v3_1890226586728407041.json
name: Product Photography Relight v3_1890226586728407041
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Product Photography Relight v3_1890226586728407041.json
hash: 7b39e89701e960e1
coverage: 0.647059
learned_at: 2026-11-14 00:48:35
nodes: [CLIPTextEncode, Note, Reroute, Note, Note, Note, Note, PreviewImage, Note, VAEEncode, CheckpointLoaderSimple, Note, MaskToImage, ICLightConditioning, VAEEncode, LoadAndApplyICLightUnet, CLIPTextEncode, VAEDecode, KSampler, SAMLoader, GroundingDinoModelLoader (segment anything), VAEDecode, KSampler, Note, Note, Note, Note, ImageInvert, CLIPTextEncode, ImageInvert, ImageInvert, Image Blending Mode, Image Blending Mode, Note, Note, CheckpointLoaderSimple, Note, EmptyLatentImage, SplitImageWithAlpha, ImageGaussianBlur, ImageInvert, Image Blending Mode, PreviewImage, ImageGaussianBlur, PreviewImage, Note, SplitImageWithAlpha, Note, KSampler, VAEDecode, EmptyLatentImage, PreviewBridge, Image Blending Mode, Image Blending Mode, Note, ControlNetLoader, ControlNetApply, ControlNetApply, MaskToImage, Note, Note, Note, ImpactGaussianBlurMask, PreviewImage, Note, GrowMask, ImpactGaussianBlurMask, CLIPTextEncode, PreviewImage, Note, LoadImage, JWImageResize, DepthAnythingPreprocessor, AnimeLineArtPreprocessor, PreviewBridge, GrowMaskWithBlur, Image Blend by Mask, PreviewImage, PreviewImage, PreviewImage, PreviewBridge, RemapMaskRange, LoadImageMask, MaskToImage, MaskToImage, GroundingDinoSAMSegment (segment anything), LoadImage, PreviewBridge, Note, Note, MaskFromColor+, Note, Note, ControlNetLoader, Image Blend by Mask, ImageResize+, PreviewBridge, PreviewImage, Image Levels Adjustment, SaveImage, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image, image_to_image, controlnet]
missing: []
parameters: {"batch_size": 1, "cfg": 3.6, "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors", "controlnet_strength": 0.8, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 180794899782057, "steps": 40, "width": 1024}
---

# 平台全量/Product Photography Relight v3_1890226586728407041.json

> 来源文件 `comfyui_library/workflows/平台全量/Product Photography Relight v3_1890226586728407041.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `Note`
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `MaskToImage`
- `ICLightConditioning`
- `VAEEncode` ★核心
- `LoadAndApplyICLightUnet`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `ImageInvert`
- `CLIPTextEncode` ★核心
- `ImageInvert`
- `ImageInvert`
- `Image Blending Mode`
- `Image Blending Mode`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `EmptyLatentImage` ★核心
- `SplitImageWithAlpha`
- `ImageGaussianBlur`
- `ImageInvert`
- `Image Blending Mode`
- `PreviewImage`
- `ImageGaussianBlur`
- `PreviewImage`
- `Note`
- `SplitImageWithAlpha`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `PreviewBridge`
- `Image Blending Mode`
- `Image Blending Mode`
- `Note`
- `ControlNetLoader`
- `ControlNetApply` ★核心
- `ControlNetApply` ★核心
- `MaskToImage`
- `Note`
- `Note`
- `Note`
- `ImpactGaussianBlurMask`
- `PreviewImage`
- `Note`
- `GrowMask`
- `ImpactGaussianBlurMask`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Note`
- `LoadImage`
- `JWImageResize`
- `DepthAnythingPreprocessor`
- `AnimeLineArtPreprocessor`
- `PreviewBridge`
- `GrowMaskWithBlur`
- `Image Blend by Mask`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewBridge`
- `RemapMaskRange`
- `LoadImageMask`
- `MaskToImage`
- `MaskToImage`
- `GroundingDinoSAMSegment (segment anything)`
- `LoadImage`
- `PreviewBridge`
- `Note`
- `Note`
- `MaskFromColor+`
- `Note`
- `Note`
- `ControlNetLoader`
- `Image Blend by Mask`
- `ImageResize+`
- `PreviewBridge`
- `PreviewImage`
- `Image Levels Adjustment`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、image_to_image、controlnet

## 关键参数

- `checkpoint` = `epicrealism_naturalSinRC1VAE.safetensors`
- `seed` = `180794899782057`
- `steps` = `40`
- `cfg` = `3.6`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.8`

## 知识

覆盖率 **65%**（66/102）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`CheckpointLoaderSimple`、`MaskToImage`、`ICLightConditioning`、`LoadAndApplyICLightUnet`、`VAEDecode`、`KSampler`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`、`ImageInvert`、`Image Blending Mode`、`EmptyLatentImage`、`SplitImageWithAlpha`、`ImageGaussianBlur`、`PreviewBridge`、`ControlNetLoader`、`ControlNetApply`、`ImpactGaussianBlurMask`、`GrowMask`、`LoadImage`、`JWImageResize`、`DepthAnythingPreprocessor`、`AnimeLineArtPreprocessor`、`GrowMaskWithBlur`、`Image Blend by Mask`、`RemapMaskRange`、`LoadImageMask`、`GroundingDinoSAMSegment (segment anything)`、`MaskFromColor+`、`ImageResize+`、`Image Levels Adjustment`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApply、ControlNetLoader
