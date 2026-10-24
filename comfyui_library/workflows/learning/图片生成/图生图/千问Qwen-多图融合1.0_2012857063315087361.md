---
key: 图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json
name: 千问Qwen-多图融合1.0_2012857063315087361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json
hash: 9b921de4b25f0f4e
coverage: 0.857143
learned_at: 2026-10-23 12:30:13
nodes: [Note, VAELoader, TextEncodeQwenImageEditPlus, CFGNorm, ModelSamplingAuraFlow, easy imageSize, RepeatLatentBatch, ImageScaleToTotalPixels, FluxKontextImageScale, KSampler, VAEEncode, CLIPLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, Note, Image Comparer (rgthree), VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 890854676435326, "steps": 25}
---

# 图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `Note`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `easy imageSize`
- `RepeatLatentBatch`
- `ImageScaleToTotalPixels`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `Note`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `890854676435326`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`ModelSamplingAuraFlow`、`easy imageSize`、`RepeatLatentBatch`、`ImageScaleToTotalPixels`、`FluxKontextImageScale`、`KSampler`、`VAEEncode`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
