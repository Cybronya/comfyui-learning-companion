---
key: 图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json
name: Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json
hash: 4c7897b16db3e9bd
coverage: 0.869565
learned_at: 2026-10-21 02:54:28
nodes: [TextEncodeQwenImage21, ResolutionSelector, QwenPERewriteT8, easy showAnything, UNETLoader, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, QwenImage21Cache, LoraLoaderModelOnly, CR Prompt Text, VAEDecode, SaveImage, Color Grading JK, LoraLoaderModelOnly, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `easy showAnything`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `VAEDecode` ★核心
- `SaveImage`
- `Color Grading JK`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
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

覆盖率 **87%**（40/46）

**有卡**：`TextEncodeQwenImage21`、`ResolutionSelector`、`QwenPERewriteT8`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`CR Prompt Text`、`VAEDecode`、`SaveImage`、`Color Grading JK`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
