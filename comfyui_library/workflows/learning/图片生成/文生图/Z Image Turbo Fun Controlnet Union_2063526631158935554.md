---
key: 图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json
name: Z Image Turbo Fun Controlnet Union_2063526631158935554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json
hash: f2b61739f83d95be
coverage: 0.888889
learned_at: 2026-10-19 23:02:51
nodes: [CLIPLoader, VAELoader, KSampler, PreviewImage, CLIPTextEncode, UNETLoader, VAEDecode, SaveImage, ModelSamplingAuraFlow, EmptySD3LatentImage, GetImageSize, CLIPTextEncode, QwenImageDiffsynthControlnet, ModelPatchLoader, AIO_Preprocessor, LoadImage, Text, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 731587987110327, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z Image Turbo Fun Controlnet Union_2063526631158935554.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `Text`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `731587987110327`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`SaveImage`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`GetImageSize`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`AIO_Preprocessor`、`LoadImage`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
