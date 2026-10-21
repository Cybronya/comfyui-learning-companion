---
key: 图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json
name: BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json
hash: a3a7be62fba521c4
coverage: 0.906977
learned_at: 2026-10-21 00:38:46
nodes: [VAELoader, VAEDecode, QwenImage21Cache, TextEncodeQwenImage21, KSampler, ComfySwitchNode, CLIPLoader, LoadImage, ResolutionSelector, CR Prompt Text, EmptyLatentImage, SaveImageAdvanced, UNETLoader, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心
- `SaveImageAdvanced`
- `UNETLoader` ★核心
- `SaveImage`
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

覆盖率 **91%**（39/43）

**有卡**：`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`CLIPLoader`、`LoadImage`、`ResolutionSelector`、`CR Prompt Text`、`EmptyLatentImage`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
