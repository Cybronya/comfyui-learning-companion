---
key: 图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json
name: FLUX.1_ipadapter_1880962162222067713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json
hash: 81ebf9965aa6f652
coverage: 1
learned_at: 2026-10-07 03:05:01
nodes: [UNETLoader, DualCLIPLoader, VAELoader, KSampler, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, EmptyLatentImage, IPAdapterFluxLoader, ApplyIPAdapterFlux, SaveImage, VAEDecode, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.76, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 90424892955213, "steps": 20, "width": 768}
---

# 图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1_ipadapter_1880962162222067713.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `IPAdapterFluxLoader`
- `ApplyIPAdapterFlux`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `90424892955213`
- `steps` = `20`
- `cfg` = `1.76`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`EmptyLatentImage`、`IPAdapterFluxLoader`、`ApplyIPAdapterFlux`、`SaveImage`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
