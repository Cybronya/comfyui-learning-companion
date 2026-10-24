---
key: 图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json
name: Flux1-Kontext 线稿 Controlnet_1968161672269561858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json
hash: f8cba7b38ff69714
coverage: 0.958333
learned_at: 2026-10-23 10:58:54
nodes: [LoadImage, VAEEncode, ReferenceLatent, SaveImage, FluxKontextImageScale, CLIPTextEncode, UNETLoader, SaveImage, Note, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, FluxGuidance, ConditioningZeroOut, VAELoader, Text Multiline, ControlNetLoader, AIO_Preprocessor, DualCLIPLoader, SetUnionControlNetType, ControlNetApplySD3, LoadImage, KSampler, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 92493012612895, "steps": 20}
---

# 图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 线稿 Controlnet_1968161672269561858.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `SaveImage`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `Note`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `Text Multiline`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `DualCLIPLoader`
- `SetUnionControlNetType`
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.8000000000000003`
- `seed` = `92493012612895`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`LoadImage`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`FluxKontextImageScale`、`CLIPTextEncode`、`UNETLoader`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`Text Multiline`、`ControlNetLoader`、`AIO_Preprocessor`、`DualCLIPLoader`、`SetUnionControlNetType`、`ControlNetApplySD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader
