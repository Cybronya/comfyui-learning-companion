---
key: 图片生成/图生图/Wan2.2-AllInOne-V10-【洗图】（图生图）_1978271093335187457.json
name: Wan2.2-AllInOne-V10-【洗图】（图生图）_1978271093335187457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-AllInOne-V10-【洗图】（图生图）_1978271093335187457.json
hash: 6c1dc52a7bc34338
coverage: 1
learned_at: 2026-10-23 11:28:06
nodes: [LoadImage, ImageResizeKJv2, VAEDecode, LayerUtility: PurgeVRAM, CLIPTextEncode, Label (rgthree), Label (rgthree), SaveImage, KSampler, easy float, CLIPTextEncode, CheckpointLoaderSimple, ModelSamplingSD3, VAEEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 0.3500000000000001, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1111997458494631, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2-AllInOne-V10-【洗图】（图生图）_1978271093335187457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-AllInOne-V10-【洗图】（图生图）_1978271093335187457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LoadImage`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `easy float`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1111997458494631`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `0.3500000000000001`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`LoadImage`、`ImageResizeKJv2`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`Label (rgthree)`、`SaveImage`、`KSampler`、`easy float`、`CheckpointLoaderSimple`、`ModelSamplingSD3`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、ImageResizeKJv2、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
