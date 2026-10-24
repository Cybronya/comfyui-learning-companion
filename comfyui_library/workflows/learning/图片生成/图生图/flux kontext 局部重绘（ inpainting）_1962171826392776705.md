---
key: 图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json
name: flux kontext 局部重绘（ inpainting）_1962171826392776705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json
hash: ee901b5b01eb49f9
coverage: 1
learned_at: 2026-10-23 11:35:09
nodes: [UNETLoader, Kontext Inpainting Conditioning, DualCLIPLoader, ConditioningZeroOut, FluxGuidance, ReferenceLatent, DifferentialDiffusion, KSampler, SaveImage, VAEDecode, VAELoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, MaskBlur+, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 1035302542720232, "steps": 20}
---

# 图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `Kontext Inpainting Conditioning`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `MaskBlur+`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1035302542720232`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`UNETLoader`、`Kontext Inpainting Conditioning`、`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`DifferentialDiffusion`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`MaskBlur+`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
