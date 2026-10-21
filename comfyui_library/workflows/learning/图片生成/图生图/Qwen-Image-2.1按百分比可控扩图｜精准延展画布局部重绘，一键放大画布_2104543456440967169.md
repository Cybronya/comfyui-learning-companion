---
key: 图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json
name: Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json
hash: eb3883f4623f23fd
coverage: 0.690476
learned_at: 2026-10-21 00:43:18
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPLoader, QwenImage21Cache, SetNode, ImageScaleToTotalPixels, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, GetNode, Any Switch (rgthree), GetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, KSampler, VAEDecode, SetNode, TextEncodeQwenImage21, easy imageSizeByLongerSide, GetNode, SetNode, PrimitiveFloat, LoadImage, SaveImage, Image Comparer (rgthree), PreviewImage, GetNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, DapaoImagePadDirectionNode, TextGenerateLTX2Prompt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1按百分比可控扩图｜精准延展画布局部重绘，一键放大画布_2104543456440967169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `TextEncodeQwenImage21`
- `easy imageSizeByLongerSide`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `DapaoImagePadDirectionNode`
- `TextGenerateLTX2Prompt`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（58/84）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`QwenImage21Cache`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`easy imageSizeByLongerSide`、`LoadImage`、`SaveImage`、`DapaoImagePadDirectionNode`、`TextGenerateLTX2Prompt`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
