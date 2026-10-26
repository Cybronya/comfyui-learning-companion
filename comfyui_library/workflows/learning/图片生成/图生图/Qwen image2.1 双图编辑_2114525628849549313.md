---
key: 图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json
name: Qwen image2.1 双图编辑_2114525628849549313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json
hash: dfbfec55cefbbf96
coverage: 0.941176
learned_at: 2026-10-26 22:03:16
nodes: [VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, SaveImage, PrimitiveStringMultiline, StringConcatenate, CLIPLoader, TextGenerate, TextEncodeQwenImage21, LoadImage, LoadImage, UNETLoader, KSampler, LoraLoaderModelOnly, JjkShowText, ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 983177877145591, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1 双图编辑_2114525628849549313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `CLIPLoader`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkShowText`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `983177877145591`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`StringConcatenate`、`TextGenerate`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`JjkShowText`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
