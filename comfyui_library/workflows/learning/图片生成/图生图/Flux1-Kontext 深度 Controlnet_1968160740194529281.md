---
key: 图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json
name: Flux1-Kontext 深度 Controlnet_1968160740194529281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json
hash: b248f001225d7974
coverage: 0.958333
learned_at: 2026-10-23 10:58:54
nodes: [LoadImage, VAEEncode, ReferenceLatent, SaveImage, FluxKontextImageScale, DualCLIPLoader, UNETLoader, SaveImage, Note, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, FluxGuidance, ConditioningZeroOut, VAELoader, Text Multiline, LoadImage, AIO_Preprocessor, CLIPTextEncode, SetUnionControlNetType, ControlNetLoader, LoadImage, ControlNetApplySD3, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1054028322737332, "steps": 20}
---

# 图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 深度 Controlnet_1968160740194529281.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `SaveImage`
- `FluxKontextImageScale`
- `DualCLIPLoader`
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
- `LoadImage`
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心
- `SetUnionControlNetType`
- `ControlNetLoader`
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.8000000000000003`
- `seed` = `1054028322737332`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`LoadImage`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`FluxKontextImageScale`、`DualCLIPLoader`、`UNETLoader`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`Text Multiline`、`AIO_Preprocessor`、`CLIPTextEncode`、`SetUnionControlNetType`、`ControlNetLoader`、`ControlNetApplySD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader
