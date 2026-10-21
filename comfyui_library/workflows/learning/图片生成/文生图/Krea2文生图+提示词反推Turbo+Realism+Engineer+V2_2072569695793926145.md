---
key: 图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json
name: Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json
hash: 744755aa7917d0c7
coverage: 0.75
learned_at: 2026-10-19 23:41:36
nodes: [CLIPLoader, StringConcatenate, PreviewAny, TextGenerate, ResolutionSelector, LoraLoaderModelOnly, ConditioningZeroOut, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPTextEncode, VAELoader, UNETLoader, VAEDecode, KSampler, SaveImage, LoadImage, PreviewAny, RH_Captioner, Fast Groups Bypasser (rgthree), EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 39350455204775, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `StringConcatenate`
- `PreviewAny`
- `TextGenerate`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `RH_Captioner`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `39350455204775`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`CLIPLoader`、`StringConcatenate`、`TextGenerate`、`ResolutionSelector`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`LoadImage`、`RH_Captioner`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
