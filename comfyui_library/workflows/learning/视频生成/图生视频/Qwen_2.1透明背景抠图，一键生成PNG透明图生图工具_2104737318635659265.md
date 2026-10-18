---
key: 视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json
name: Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json
hash: 17880dfa6c0cc9c6
coverage: 0.816327
learned_at: 2026-10-17 22:18:52
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, SetNode, CLIPLoader, UNETLoader, PreviewImage, FastGroupsBypassSwitch, ResolutionSelector, JjkText, SaveImage, GetNode, easy showAnything, LoadImage, EmptyLatentImage, TextEncodeQwenImage21, TextCombinerTwo, KSampler, VAEDecode, JjkText, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_2.1透明背景抠图，一键生成PNG透明图生图工具_2104737318635659265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `JjkText`
- `SaveImage`
- `GetNode`
- `easy showAnything`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextCombinerTwo`
- `KSampler` ★核心
- `VAEDecode` ★核心
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

覆盖率 **82%**（40/49）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`UNETLoader`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`SaveImage`、`LoadImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextCombinerTwo`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
