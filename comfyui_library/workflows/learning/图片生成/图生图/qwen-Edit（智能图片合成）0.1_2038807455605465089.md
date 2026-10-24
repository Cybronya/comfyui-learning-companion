---
key: 图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json
name: qwen-Edit（智能图片合成）0.1_2038807455605465089
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json
hash: 7e9c2574cdee95b4
coverage: 1
learned_at: 2026-10-23 11:42:19
nodes: [SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, LoadImage, LoadImage, KSampler, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 739008269422556, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-Edit（智能图片合成）0.1_2038807455605465089.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（11 个）：
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `739008269422556`
- `steps` = `9`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`SaveImage`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`VAEEncode`、`LoadImage`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImageEditPlus、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
