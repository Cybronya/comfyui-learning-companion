---
key: 图片生成/图生图/Flux1 Kontext put it v4.2_1971140729403805698.json
name: Flux1 Kontext put it v4.2_1971140729403805698
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux1 Kontext put it v4.2_1971140729403805698.json
hash: c6cbcab5ff1caae3
coverage: 0.928571
learned_at: 2026-10-23 10:58:53
nodes: [LoadImage, VAEEncode, FluxGuidance, ReferenceLatent, SaveImage, KSampler, ShowText|pysssss, FluxKontextImageScale, CLIPTextEncode, DualCLIPLoader, VAELoader, ConditioningZeroOut, VAEDecode, SaveImage, Note, TeaCache, UNETLoader, LoraLoaderModelOnly, ImageConcatMulti, Text Multiline, RH_Translator, FastCanvasTool, LayerMask: PersonMaskUltra V2, FastCanvas, LoadImage, LoadImage, ImageConcatMulti, UnetLoaderGGUF]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 271313331253712, "steps": 20}
---

# 图片生成/图生图/Flux1 Kontext put it v4.2_1971140729403805698.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux1 Kontext put it v4.2_1971140729403805698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LoadImage`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `SaveImage`
- `KSampler` ★核心
- `ShowText|pysssss`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `TeaCache`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcatMulti`
- `Text Multiline`
- `RH_Translator`
- `FastCanvasTool`
- `LayerMask: PersonMaskUltra V2`
- `FastCanvas`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `UnetLoaderGGUF` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `271313331253712`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`LoadImage`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`SaveImage`、`KSampler`、`FluxKontextImageScale`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`TeaCache`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`Text Multiline`、`RH_Translator`、`FastCanvasTool`、`LayerMask: PersonMaskUltra V2`、`FastCanvas`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
