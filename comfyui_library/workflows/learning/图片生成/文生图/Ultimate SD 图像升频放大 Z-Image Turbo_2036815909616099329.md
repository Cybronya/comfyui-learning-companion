---
key: 图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json
name: Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json
hash: 525aad3b06bbacf8
coverage: 0.777778
learned_at: 2026-10-21 02:55:14
nodes: [EmptySD3LatentImage, ModelSamplingAuraFlow, Note, Image Comparer (rgthree), LoraLoaderModelOnly, VAELoader, VAEDecode, UltimateSDUpscale, PreviewImage, SaveImage, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, UNETLoader, CLIPTextEncode, KSampler, UpscaleModelLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 623721254340994, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `Note`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UltimateSDUpscale`
- `PreviewImage`
- `SaveImage`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UpscaleModelLoader`

## 关键参数

- `seed` = `623721254340994`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`VAELoader`、`VAEDecode`、`UltimateSDUpscale`、`SaveImage`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`KSampler`、`UpscaleModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、UltimateSDUpscale

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
