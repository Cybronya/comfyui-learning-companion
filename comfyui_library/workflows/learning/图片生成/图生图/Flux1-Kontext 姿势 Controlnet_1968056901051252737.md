---
key: 图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json
name: Flux1-Kontext 姿势 Controlnet_1968056901051252737
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json
hash: 9005e6fc87208f3a
coverage: 0.92
learned_at: 2026-10-23 10:58:53
nodes: [LoadImage, VAEEncode, SaveImage, FluxKontextImageScale, DualCLIPLoader, UNETLoader, SaveImage, Note, ImageConcatMulti, VAEDecode, FluxGuidance, ConditioningZeroOut, VAELoader, Text Multiline, OpenposePreprocessor, ReferenceLatent, CLIPTextEncode, ControlNetLoader, SetUnionControlNetType, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, ControlNetApplySD3, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.8000000000000003, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 518881005686264, "steps": 20}
---

# 图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux1-Kontext 姿势 Controlnet_1968056901051252737.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `LoadImage`
- `VAEEncode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `Note`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `Text Multiline`
- `OpenposePreprocessor`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `518881005686264`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.8000000000000003`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`LoadImage`、`VAEEncode`、`SaveImage`、`FluxKontextImageScale`、`DualCLIPLoader`、`UNETLoader`、`ImageConcatMulti`、`VAEDecode`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`Text Multiline`、`OpenposePreprocessor`、`ReferenceLatent`、`CLIPTextEncode`、`ControlNetLoader`、`SetUnionControlNetType`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetLoader
