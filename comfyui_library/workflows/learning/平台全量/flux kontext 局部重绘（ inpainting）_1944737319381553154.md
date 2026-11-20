---
key: 平台全量/flux kontext 局部重绘（ inpainting）_1944737319381553154.json
name: flux kontext 局部重绘（ inpainting）_1944737319381553154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux kontext 局部重绘（ inpainting）_1944737319381553154.json
hash: 88a870cacb9d1b2d
coverage: 1
learned_at: 2026-11-14 01:10:37
nodes: [Mask Fill Holes, UNETLoader, DualCLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SaveImage, KSampler, DifferentialDiffusion, ReferenceLatent, Kontext Inpainting Conditioning, VAEDecode, VAEEncode, LoadImage, CLIPTextEncode, FluxGuidance, ConditioningZeroOut]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 298737570935098, "steps": 20}
---

# 平台全量/flux kontext 局部重绘（ inpainting）_1944737319381553154.json

> 来源文件 `comfyui_library/workflows/平台全量/flux kontext 局部重绘（ inpainting）_1944737319381553154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `Mask Fill Holes`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SaveImage`
- `KSampler` ★核心
- `DifferentialDiffusion`
- `ReferenceLatent`
- `Kontext Inpainting Conditioning`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `298737570935098`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`Mask Fill Holes`、`UNETLoader`、`DualCLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`SaveImage`、`KSampler`、`DifferentialDiffusion`、`ReferenceLatent`、`Kontext Inpainting Conditioning`、`VAEDecode`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
