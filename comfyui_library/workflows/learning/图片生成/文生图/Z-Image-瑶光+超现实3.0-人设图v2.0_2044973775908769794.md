---
key: 图片生成/文生图/Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794.json
name: Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794.json
hash: 1830c0412baae065
coverage: 0.833333
learned_at: 2026-10-21 02:55:55
nodes: [LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, ImageScaleToTotalPixels, PreviewImage, Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, INTConstant, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, KSampler, FastFilmGrain, Fast Groups Bypasser (rgthree), EmptyLatentImage, CR Text, UNETLoader, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1004029254038945, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-瑶光+超现实3.0-人设图v2.0_2044973775908769794.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `FastFilmGrain`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `CR Text`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1004029254038945`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`LayerColor: BrightnessContrastV2`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`INTConstant`、`SeedVR2VideoUpscaler`、`SaveImage`、`KSampler`、`FastFilmGrain`、`EmptyLatentImage`、`CR Text`、`UNETLoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
