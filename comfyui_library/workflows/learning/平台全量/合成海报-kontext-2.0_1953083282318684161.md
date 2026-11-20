---
key: 平台全量/合成海报-kontext-2.0_1953083282318684161.json
name: 合成海报-kontext-2.0_1953083282318684161
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/合成海报-kontext-2.0_1953083282318684161.json
hash: 48c9993cd68bb0f3
coverage: 0.964286
learned_at: 2026-11-14 01:51:49
nodes: [LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, CLIPTextEncode, FastCanvasTool, ImageScaleToMegapixels, FluxKontextImageScale, ReferenceLatent, ConditioningZeroOut, FluxGuidance, KSampler, VAEDecode, easy cleanGpuUsed, ImageScaleToMegapixels, BiRefNet_Hugo, PreviewImage, LoadImage, TextCombinerTwo, CR Text, ImageScaleToMegapixels, VAEEncode, FastCanvas, SaveImage, CR Latent Batch Size, ChinesePrompt_Mix]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 20}
---

# 平台全量/合成海报-kontext-2.0_1953083282318684161.json

> 来源文件 `comfyui_library/workflows/平台全量/合成海报-kontext-2.0_1953083282318684161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `FastCanvasTool`
- `ImageScaleToMegapixels`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageScaleToMegapixels`
- `BiRefNet_Hugo`
- `PreviewImage`
- `LoadImage`
- `TextCombinerTwo`
- `CR Text`
- `ImageScaleToMegapixels`
- `VAEEncode` ★核心
- `FastCanvas`
- `SaveImage`
- `CR Latent Batch Size`
- `ChinesePrompt_Mix`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `999`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`FastCanvasTool`、`ImageScaleToMegapixels`、`FluxKontextImageScale`、`ReferenceLatent`、`ConditioningZeroOut`、`FluxGuidance`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`BiRefNet_Hugo`、`TextCombinerTwo`、`CR Text`、`VAEEncode`、`FastCanvas`、`SaveImage`、`CR Latent Batch Size`、`ChinesePrompt_Mix`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
