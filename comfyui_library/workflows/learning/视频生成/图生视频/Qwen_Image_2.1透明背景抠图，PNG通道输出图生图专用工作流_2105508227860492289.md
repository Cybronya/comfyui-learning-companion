---
key: 视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json
name: Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json
hash: 35db1c21ee5aca1f
coverage: 0.862745
learned_at: 2026-10-17 22:18:57
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, VAEDecode, ImageConcatMulti, SaveImageAdvanced, ImageConcatMulti, SaveImageAdvanced, SaveImage, easy cleanGpuUsed, TextCombinerTwo, easy showAnything, ResolutionSelector, JjkText, JjkText, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `SaveImage`
- `easy cleanGpuUsed`
- `TextCombinerTwo`
- `easy showAnything`
- `ResolutionSelector`
- `JjkText`
- `JjkText`
- `LoadImage`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **86%**（44/51）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`ImageConcatMulti`、`SaveImageAdvanced`、`SaveImage`、`easy cleanGpuUsed`、`TextCombinerTwo`、`ResolutionSelector`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
