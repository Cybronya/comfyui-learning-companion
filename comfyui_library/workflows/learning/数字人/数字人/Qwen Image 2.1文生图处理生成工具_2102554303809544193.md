---
key: 数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json
name: Qwen Image 2.1文生图处理生成工具_2102554303809544193
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json
hash: b79cdfce929a098d
coverage: 0.840909
learned_at: 2026-10-19 00:19:13
nodes: [UNETLoader, CLIPLoader, VAELoader, easy showAnything, EmptyLatentImage, TextGenerateLTX2Prompt, TextEncodeQwenImage21, CLIPLoader, VAEDecode, PreviewImage, SaveImage, ResolutionSelector, KSampler, JjkText, FastGroupsBypassSwitch, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（44 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `ResolutionSelector`
- `KSampler` ★核心
- `JjkText`
- `FastGroupsBypassSwitch`
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

覆盖率 **84%**（37/44）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`KSampler`、`FastGroupsBypassSwitch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
