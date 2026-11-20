---
key: 平台全量/最强Wan2.2写实人像高清放大工作流_1959429572523667458.json
name: 最强Wan2.2写实人像高清放大工作流_1959429572523667458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强Wan2.2写实人像高清放大工作流_1959429572523667458.json
hash: 2fbc94b7fac7a3b6
coverage: 0.961538
learned_at: 2026-11-14 02:14:08
nodes: [ModelSamplingSD3, VAELoader, CLIPLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, LoraLoaderModelOnly, Image Comparer (rgthree), CLIPTextEncode, KSampler, KSampler, ImageScaleBy, SUPIR_conditioner, SUPIR_first_stage, SUPIR_encode, SUPIR_sample, SUPIR_decode, SaveImage, SUPIR_model_loader_v2, CheckpointLoaderSimple, VAEDecode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "checkpoint": "XL真人写实摄影_V1.safetensors", "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 123, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/最强Wan2.2写实人像高清放大工作流_1959429572523667458.json

> 来源文件 `comfyui_library/workflows/平台全量/最强Wan2.2写实人像高清放大工作流_1959429572523667458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageScaleBy`
- `SUPIR_conditioner`
- `SUPIR_first_stage`
- `SUPIR_encode`
- `SUPIR_sample`
- `SUPIR_decode`
- `SaveImage`
- `SUPIR_model_loader_v2`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `123`
- `steps` = `6`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`
- `checkpoint` = `XL真人写实摄影_V1.safetensors`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ImageScaleBy`、`SUPIR_conditioner`、`SUPIR_first_stage`、`SUPIR_encode`、`SUPIR_sample`、`SUPIR_decode`、`SaveImage`、`SUPIR_model_loader_v2`、`CheckpointLoaderSimple`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
