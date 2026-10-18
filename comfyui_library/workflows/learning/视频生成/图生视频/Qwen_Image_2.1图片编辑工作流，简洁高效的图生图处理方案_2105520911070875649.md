---
key: 视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json
name: Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json
hash: 93e2cc3a1055b92a
coverage: 0.896552
learned_at: 2026-10-17 22:18:56
nodes: [UNETLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, TextGenerateLTX2Prompt, easy showAnything, CLIPLoader, QwenImage21Cache, KSampler, VAEDecode, SaveImageAdvanced, ComfySwitchNode, ResolutionSelector, TextInput_, SaveImage, BatchImagesNode, EmptyLatentImage, LoadImage, GetImageSize, TextEncodeQwenImage21, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `CLIPLoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `ResolutionSelector`
- `TextInput_`
- `SaveImage`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `GetImageSize`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
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

覆盖率 **90%**（52/58）

**有卡**：`UNETLoader`、`VAELoader`、`LoadImage`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`ResolutionSelector`、`TextInput_`、`SaveImage`、`BatchImagesNode`、`EmptyLatentImage`、`GetImageSize`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
