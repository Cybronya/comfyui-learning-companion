---
key: 平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json
name: Kontext老照片修复_V1.0版本_1950795927500038145
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json
hash: 1347b160ff5aca61
coverage: 0.947368
learned_at: 2026-11-14 00:35:57
nodes: [FluxKontextImageScale, ImageStitch, ReferenceLatent, FluxGuidance, ConditioningZeroOut, VAEEncode, CLIPTextEncode, ImageConcatMulti, VAEDecode, KSampler, Text Multiline, ShowText|pysssss, SaveImage, SaveImage, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 119086219385358, "steps": 20}
---

# 平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext老照片修复_V1.0版本_1950795927500038145.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `FluxKontextImageScale`
- `ImageStitch`
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Text Multiline`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `119086219385358`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`FluxKontextImageScale`、`ImageStitch`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`ImageConcatMulti`、`VAEDecode`、`KSampler`、`Text Multiline`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
