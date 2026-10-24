---
key: 图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json
name: Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json
hash: c391e5d03ad2fb2c
coverage: 0.928571
learned_at: 2026-10-23 11:28:12
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEEncode, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, Image Comparer (rgthree), CLIPTextEncode, LoadImage, KSampler, CLIPTextEncode, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 863564964469897, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2低噪模型洗图工作流-官方版-自用_1966463928635174913.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `863564964469897`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
