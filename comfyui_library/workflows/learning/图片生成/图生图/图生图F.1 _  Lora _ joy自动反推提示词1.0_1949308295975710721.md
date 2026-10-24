---
key: 图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json
name: 图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json
hash: 8e16eb9b308b2866
coverage: 0.826087
learned_at: 2026-10-23 12:43:08
nodes: [ImageScaleBy, easy showAnything, easy showAnything, VAELoader, KSampler, ConditioningZeroOut, ConstrainImage|pysssss, Joy_caption_two, CLIPTextEncodeFlux, SaveImage, Note, LoadImage, SetNode, VAEEncode, VAEDecode, RepeatLatentBatch, DualCLIPLoader, Joy_caption_two_load, UNETLoader, easy imageSize, LoraLoader, LoraLoader, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.65, "lora_name": "CEN写真摄影系列_可爱的少女脸型Ⅵ_v1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 249407941309193, "steps": 20, "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图F.1 _  Lora _ joy自动反推提示词1.0_1949308295975710721.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ImageScaleBy`
- `easy showAnything`
- `easy showAnything`
- `VAELoader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `Joy_caption_two`
- `CLIPTextEncodeFlux` ★核心
- `SaveImage`
- `Note`
- `LoadImage`
- `SetNode`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `RepeatLatentBatch`
- `DualCLIPLoader`
- `Joy_caption_two_load`
- `UNETLoader` ★核心
- `easy imageSize`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `249407941309193`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.65`
- `lora_name` = `CEN写真摄影系列_可爱的少女脸型Ⅵ_v1.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`ImageScaleBy`、`VAELoader`、`KSampler`、`ConditioningZeroOut`、`ConstrainImage|pysssss`、`Joy_caption_two`、`CLIPTextEncodeFlux`、`SaveImage`、`LoadImage`、`VAEEncode`、`VAEDecode`、`RepeatLatentBatch`、`DualCLIPLoader`、`Joy_caption_two_load`、`UNETLoader`、`easy imageSize`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux、RepeatLatentBatch
