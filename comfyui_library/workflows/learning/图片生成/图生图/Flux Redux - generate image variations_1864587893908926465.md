---
key: 图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json
name: Flux Redux - generate image variations_1864587893908926465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json
hash: b02aa1d06ee0cbc9
coverage: 1
learned_at: 2026-10-23 10:58:03
nodes: [KSamplerSelect, RandomNoise, BasicScheduler, BasicGuider, DualCLIPLoader, VAELoader, CheckpointLoaderSimple, EmptyLatentImage, VAEDecode, SamplerCustomAdvanced, LoadImage, FluxGuidance, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, StyleModelApply, StyleModelLoader, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "pixelwave_flux1_dev_fp8_03.safetensors", "height": 1152, "width": 896}
---

# 图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Redux - generate image variations_1864587893908926465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `BasicGuider`
- `DualCLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelApply`
- `StyleModelLoader`
- `SaveImage`

## 关键参数

- `checkpoint` = `pixelwave_flux1_dev_fp8_03.safetensors`
- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`BasicGuider`、`DualCLIPLoader`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`、`FluxGuidance`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelApply`、`StyleModelLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect
