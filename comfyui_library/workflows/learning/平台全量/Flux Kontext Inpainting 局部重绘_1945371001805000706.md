---
key: 平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json
name: Flux Kontext Inpainting 局部重绘_1945371001805000706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json
hash: f6740c98b7c2feee
coverage: 0.888889
learned_at: 2026-11-14 00:27:53
nodes: [VAELoader, UNETLoader, DualCLIPLoader, RH_Translator, CLIPTextEncode, FluxGuidance, KSampler, ConditioningZeroOut, Kontext Inpainting Conditioning, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), Anything Everywhere3, LayerMask: MaskPreview, Mask Fill Holes, LoadImage, GrowMaskWithBlur, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 99391530212060, "steps": 20}
---

# 平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Kontext Inpainting 局部重绘_1945371001805000706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `Kontext Inpainting Conditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `LayerMask: MaskPreview`
- `Mask Fill Holes`
- `LoadImage`
- `GrowMaskWithBlur`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `99391530212060`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`RH_Translator`、`CLIPTextEncode`、`FluxGuidance`、`KSampler`、`ConditioningZeroOut`、`Kontext Inpainting Conditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskPreview`、`Mask Fill Holes`、`LoadImage`、`GrowMaskWithBlur`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
