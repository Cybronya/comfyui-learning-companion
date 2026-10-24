---
key: 图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json
name: Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json
hash: 7afcb09d4ef2f374
coverage: 0.60274
learned_at: 2026-10-23 11:16:30
nodes: [CLIPLoader, VAELoader, UNETLoader, CLIPLoader, SetNode, ImageScaleToTotalPixels, GetNode, GetNode, SetNode, GetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, KSampler, VAEDecode, TextEncodeQwenImage21, easy imageSizeByLongerSide, GetNode, SetNode, PrimitiveFloat, LoadImage, SaveImage, PreviewImage, GetNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, DapaoImagePadDirectionNode, TextGenerateLTX2Prompt, RHHiddenNodes, QwenImage21Cache, Any Switch (rgthree), GetNode, GetNode, GetNode, Image Comparer (rgthree), SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SetNode, GetNode, SetNode, GetNode, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1百分比可控扩图，画布精准延展一键放大_2112266614245773314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `easy imageSizeByLongerSide`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `DapaoImagePadDirectionNode`
- `TextGenerateLTX2Prompt`
- `RHHiddenNodes`
- `QwenImage21Cache`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **60%**（44/73）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`easy imageSizeByLongerSide`、`LoadImage`、`SaveImage`、`DapaoImagePadDirectionNode`、`TextGenerateLTX2Prompt`、`RHHiddenNodes`、`QwenImage21Cache`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
