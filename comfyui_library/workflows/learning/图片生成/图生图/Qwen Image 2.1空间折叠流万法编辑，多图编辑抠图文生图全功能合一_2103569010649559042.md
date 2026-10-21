---
key: 图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json
name: Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json
hash: 615f831d10391c83
coverage: 0.636364
learned_at: 2026-10-21 00:42:43
nodes: [SetNode, SetNode, SetNode, LoadImage, GetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, VAELoader, GetNode, LoadImage, UNETLoader, CLIPLoader, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, SetNode, GetNode, SetNode, GetNode, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, VAEDecode, SaveImage, SetNode, SetNode, LoadImage, Text, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `VAELoader`
- `GetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `Text`
- `ResolutionSelector`
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

覆盖率 **64%**（42/66）

**有卡**：`LoadImage`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`Text`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
