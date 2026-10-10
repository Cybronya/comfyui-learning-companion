---
key: 视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json
name: Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json
hash: 9e76c4dc80af090c
coverage: 0.891304
learned_at: 2026-10-10 22:53:59
nodes: [QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, EmptyLatentImage, TextGenerateLTX2Prompt, BatchImagesNode, ComfySwitchNode, VAEDecode, LoadImage, LoadImage, KSampler, VAELoader, CLIPLoader, UNETLoader, SaveImage, ResolutionSelector, JjkText, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `BatchImagesNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `ResolutionSelector`
- `JjkText`
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

覆盖率 **89%**（41/46）

**有卡**：`QwenImage21Cache`、`TextEncodeQwenImage21`、`CLIPLoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`VAEDecode`、`LoadImage`、`KSampler`、`VAELoader`、`UNETLoader`、`SaveImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
