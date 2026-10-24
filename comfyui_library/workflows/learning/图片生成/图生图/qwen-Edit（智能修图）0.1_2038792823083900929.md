---
key: 图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json
name: qwen-Edit（智能修图）0.1_2038792823083900929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json
hash: 2f2ec8583d48ede9
coverage: 1
learned_at: 2026-10-23 11:42:18
nodes: [SaveImage, ModelSamplingAuraFlow, VAEDecode, TextEncodeQwenImageEditPlus, CLIPLoader, VAELoader, VAEEncode, LoadImage, TextEncodeQwenImageEditPlus, KSampler, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 46161607931667, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-Edit（智能修图）0.1_2038792823083900929.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（11 个）：
- `SaveImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `46161607931667`
- `steps` = `9`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`SaveImage`、`ModelSamplingAuraFlow`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`LoadImage`、`KSampler`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
