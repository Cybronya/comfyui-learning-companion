---
key: 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json
name: Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json
hash: b7b392851d3ceeca
coverage: 0.854167
learned_at: 2026-10-10 20:48:10
nodes: [CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, SaveImageAdvanced, ComfySwitchNode, UNETLoader, LoadImage, TextEncodeQwenImage21, SaveImage, EmptyLatentImage, KSampler, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, PrimitiveStringMultiline, LoadImage, PreviewImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`
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

覆盖率 **85%**（41/48）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImageAdvanced`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
