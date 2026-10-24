---
key: 图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json
name: Flux2.0单图编辑（GGUF加速版）_1993841057280573442
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json
hash: fa92bedfd26b2af6
coverage: 1
learned_at: 2026-10-23 11:00:51
nodes: [VAELoader, CLIPLoader, FluxGuidance, ReferenceLatent, VAEEncode, VAEDecode, SaveImage, KSampler, CLIPTextEncode, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 109836370202295, "steps": 20}
---

# 图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.0单图编辑（GGUF加速版）_1993841057280573442.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `VAELoader`
- `CLIPLoader`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `109836370202295`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAELoader`、`CLIPLoader`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`VAEDecode`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、ReferenceLatent
