---
key: 平台全量/Inpainting, VAE Encode + SetNoiseMak + T2I model_1868497326405992450.json
name: Inpainting, VAE Encode + SetNoiseMak + T2I model_1868497326405992450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Inpainting, VAE Encode + SetNoiseMak + T2I model_1868497326405992450.json
hash: 86af5dd5e502c578
coverage: 0.923077
learned_at: 2026-11-14 00:32:45
nodes: [VAEEncode, SetLatentNoiseMask, KSampler, PreviewMask_, CheckpointLoaderSimple, VAEDecode, SaveImage, InvertMask, LoadImageMask, CLIPTextEncode, CLIPTextEncode, LoadImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "realisticVisionV60B1_v51VAE.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 823962642715742, "steps": 50}
---

# 平台全量/Inpainting, VAE Encode + SetNoiseMak + T2I model_1868497326405992450.json

> 来源文件 `comfyui_library/workflows/平台全量/Inpainting, VAE Encode + SetNoiseMak + T2I model_1868497326405992450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `PreviewMask_`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `InvertMask`
- `LoadImageMask`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `823962642715742`
- `steps` = `50`
- `cfg` = `8`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `realisticVisionV60B1_v51VAE.safetensors`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`VAEEncode`、`SetLatentNoiseMask`、`KSampler`、`PreviewMask_`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`InvertMask`、`LoadImageMask`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SetLatentNoiseMask、VAEEncode、PreviewMask_
