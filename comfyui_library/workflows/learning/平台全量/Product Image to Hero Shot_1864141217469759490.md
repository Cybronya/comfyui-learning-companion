---
key: 平台全量/Product Image to Hero Shot_1864141217469759490.json
name: Product Image to Hero Shot_1864141217469759490
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Product Image to Hero Shot_1864141217469759490.json
hash: 9e71ec11c028fb15
coverage: 0.857143
learned_at: 2026-11-14 00:48:35
nodes: [ImageInvert, VAEDecode, ImageInvert, ImageInvert, SaveImage, Image Comparer (rgthree), Image Blending Mode, PreviewImage, ImageInvert, Image Blending Mode, SplitImageWithAlpha, Image Blending Mode, Image Blending Mode, ImageCompositeMasked, VAEEncode, Reroute, Reroute, SplitImageWithAlpha, Image Blend by Mask, Image Blending Mode, Image Levels Adjustment, CheckpointLoaderSimple, CLIPTextEncode, MaskToImage, KSampler, IPAdapterUnifiedLoader, IPAdapterAdvanced, GrowMask, LoadAndApplyICLightUnet, ICLightConditioning, VAEEncode, ICLightApplyMaskGrey, PreviewImage, ImageGaussianBlur, ImageGaussianBlur, easy imageRemBg, CLIPTextEncode, SplitImageWithAlpha, ImageResize+, LoadImage, ImpactInt, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 0, "steps": 30}
---

# 平台全量/Product Image to Hero Shot_1864141217469759490.json

> 来源文件 `comfyui_library/workflows/平台全量/Product Image to Hero Shot_1864141217469759490.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `ImageInvert`
- `VAEDecode` ★核心
- `ImageInvert`
- `ImageInvert`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Blending Mode`
- `PreviewImage`
- `ImageInvert`
- `Image Blending Mode`
- `SplitImageWithAlpha`
- `Image Blending Mode`
- `Image Blending Mode`
- `ImageCompositeMasked`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `SplitImageWithAlpha`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Levels Adjustment`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `MaskToImage`
- `KSampler` ★核心
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `GrowMask`
- `LoadAndApplyICLightUnet`
- `ICLightConditioning`
- `VAEEncode` ★核心
- `ICLightApplyMaskGrey`
- `PreviewImage`
- `ImageGaussianBlur`
- `ImageGaussianBlur`
- `easy imageRemBg`
- `CLIPTextEncode` ★核心
- `SplitImageWithAlpha`
- `ImageResize+`
- `LoadImage`
- `ImpactInt`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `epicrealism_naturalSinRC1VAE.safetensors`
- `seed` = `0`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`ImageInvert`、`VAEDecode`、`SaveImage`、`Image Blending Mode`、`SplitImageWithAlpha`、`ImageCompositeMasked`、`VAEEncode`、`Image Blend by Mask`、`Image Levels Adjustment`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`MaskToImage`、`KSampler`、`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`GrowMask`、`LoadAndApplyICLightUnet`、`ICLightConditioning`、`ICLightApplyMaskGrey`、`ImageGaussianBlur`、`easy imageRemBg`、`ImageResize+`、`LoadImage`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、IPAdapterAdvanced、IPAdapterUnifiedLoader
