---
key: 图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json
name: Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json
hash: f5e678cbfd2fb770
coverage: 0.923077
learned_at: 2026-10-23 10:56:23
nodes: [DualCLIPLoader, UNETLoader, FastCanvasTool, ConditioningZeroOut, VAEEncode, CLIPTextEncode, FluxGuidance, ReferenceLatent, GoogleTranslateTextNode, ShowText|pysssss, FastCanvas, Text Multiline, ImageScaleDownToSize, LoadImage, VAEDecode, RepeatLatentBatch, VAELoader, KSampler, LoadImage, LoraLoaderModelOnly, FluxKontextImageScale, PreviewImage, Image Rembg (Remove Background), SaveImage, Note Plus (mtb), FastCanvas]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 786635381202135, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `FastCanvasTool`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `GoogleTranslateTextNode`
- `ShowText|pysssss`
- `FastCanvas`
- `Text Multiline`
- `ImageScaleDownToSize`
- `LoadImage`
- `VAEDecode` ★核心
- `RepeatLatentBatch`
- `VAELoader`
- `KSampler` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `PreviewImage`
- `Image Rembg (Remove Background)`
- `SaveImage`
- `Note Plus (mtb)`
- `FastCanvas`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `786635381202135`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`FastCanvasTool`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`FluxGuidance`、`ReferenceLatent`、`GoogleTranslateTextNode`、`FastCanvas`、`Text Multiline`、`ImageScaleDownToSize`、`LoadImage`、`VAEDecode`、`RepeatLatentBatch`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`Image Rembg (Remove Background)`、`SaveImage`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
