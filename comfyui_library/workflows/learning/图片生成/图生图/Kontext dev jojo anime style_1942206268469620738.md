---
key: 图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json
name: Kontext dev jojo anime style_1942206268469620738
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json
hash: 85fd002e4b66f6dc
coverage: 0.947368
learned_at: 2026-10-23 11:05:42
nodes: [ImageResize, FluxKontextImageScale, VAEEncode, FluxGuidance, ConditioningZeroOut, UNETLoader, RH_Translator, DualCLIPLoader, KSampler, VAEDecode, ImageConcatMulti, SaveImage, LoadImage, SaveImage, ReferenceLatent, CLIPTextEncode, VAELoader, Note, Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 274240840935721, "steps": 20}
---

# 图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext dev jojo anime style_1942206268469620738.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ImageResize`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `274240840935721`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`ImageResize`、`FluxKontextImageScale`、`VAEEncode`、`FluxGuidance`、`ConditioningZeroOut`、`UNETLoader`、`RH_Translator`、`DualCLIPLoader`、`KSampler`、`VAEDecode`、`ImageConcatMulti`、`SaveImage`、`LoadImage`、`ReferenceLatent`、`CLIPTextEncode`、`VAELoader`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
