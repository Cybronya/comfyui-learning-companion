---
key: 图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json
name: Wan2.2写实洗图工作流_1957018598755721218
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json
hash: 895aaa8c1c806f6a
coverage: 1
learned_at: 2026-10-23 11:28:13
nodes: [CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, ModelSamplingSD3, VAEEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, VAELoader, KSampler, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 9527, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `9527`
- `steps` = `6`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPTextEncode`、`LoadImage`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
