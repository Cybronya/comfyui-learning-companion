---
key: 图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json
name: Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json
hash: e8fcb58404fb8bf3
coverage: 0.888889
learned_at: 2026-10-26 22:08:46
nodes: [EmptyLatentImage, easy showAnything, easy showAnything, ResolutionSelector, LoraLoaderModelOnly, QwenImage21Cache, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, VAEDecode, TextEncodeQwenImage21, SaveImage, SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 2048, "width": 1152}
---

# 图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-image2.1文生图超写实真人摄影风格_V2.0_2114635825890811906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `easy showAnything`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`

## 关键参数

- `width` = `1152`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`EmptyLatentImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImage21`、`SaveImage`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
