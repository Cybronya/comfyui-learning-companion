---
key: 图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json
name: Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json
hash: d3f79b93931d5e60
coverage: 0.818182
learned_at: 2026-10-07 02:22:13
nodes: [CLIPLoader, VAELoader, ImpactInt, ImpactInt, TextEncodeQwenImage21, GetNode, EmptyLatentImage, SetNode, GetNode, SetNode, VAEDecode, KSampler, SaveImage, UNETLoader, Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1空间折叠流太虚生成，简洁连线文生图傻瓜操作方案_2103612146377641986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
- `TextEncodeQwenImage21`
- `GetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `Text`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **82%**（36/44）

**有卡**：`CLIPLoader`、`VAELoader`、`ImpactInt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`UNETLoader`、`Text`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
