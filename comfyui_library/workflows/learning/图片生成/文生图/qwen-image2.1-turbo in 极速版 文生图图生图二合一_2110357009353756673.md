---
key: 图片生成/文生图/qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673.json
name: qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673.json
hash: 34a909ac6bad149d
coverage: 0.815385
learned_at: 2026-10-21 02:57:31
nodes: [PrimitiveStringMultiline, TextGenerate, BatchImagesNode, ImageScaleToTotalPixels, CLIPLoader, PrimitiveStringMultiline, KSamplerSelect, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, QwenImage21Cache, ModelAttentionBackend, TextGenerate, LoraLoaderModelOnly, VAELoader, CLIPLoader, TextEncodeQwenImage21, ComfySwitchNode, SamplerCustom, ManualSigmas, EmptyLatentImage, PrimitiveBoolean, VAEDecode, PreviewAny, Any Switch (rgthree), CLIPLoader, PrimitiveInt, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1-turbo in 极速版 文生图图生图二合一_2110357009353756673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TextGenerate`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `PreviewAny`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（53/65）

**有卡**：`TextGenerate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`CLIPLoader`、`KSamplerSelect`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`ModelAttentionBackend`、`VAELoader`、`TextEncodeQwenImage21`、`SamplerCustom`、`ManualSigmas`、`EmptyLatentImage`、`PrimitiveBoolean`、`VAEDecode`、`LoadImage`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
