---
key: 图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json
name: Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json
hash: 3885764a567a5b7d
coverage: 0.925926
learned_at: 2026-10-23 10:56:23
nodes: [DualCLIPLoader, UNETLoader, FastCanvasTool, ConditioningZeroOut, VAEEncode, CLIPTextEncode, ReferenceLatent, ShowText|pysssss, FastCanvas, ImageScaleDownToSize, LoadImage, VAEDecode, RepeatLatentBatch, VAELoader, LoadImage, FluxKontextImageScale, PreviewImage, Image Rembg (Remove Background), SaveImage, FluxGuidance, GoogleTranslateTextNode, KSampler, Text Multiline, LoraLoaderModelOnly, Note Plus (mtb), LoadImageFromUrl, FastCanvas]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 702955660850553, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `FastCanvasTool`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ShowText|pysssss`
- `FastCanvas`
- `ImageScaleDownToSize`
- `LoadImage`
- `VAEDecode` ★核心
- `RepeatLatentBatch`
- `VAELoader`
- `LoadImage`
- `FluxKontextImageScale`
- `PreviewImage`
- `Image Rembg (Remove Background)`
- `SaveImage`
- `FluxGuidance`
- `GoogleTranslateTextNode`
- `KSampler` ★核心
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `FastCanvas`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `702955660850553`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`FastCanvasTool`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`FastCanvas`、`ImageScaleDownToSize`、`LoadImage`、`VAEDecode`、`RepeatLatentBatch`、`VAELoader`、`FluxKontextImageScale`、`Image Rembg (Remove Background)`、`SaveImage`、`FluxGuidance`、`GoogleTranslateTextNode`、`KSampler`、`Text Multiline`、`LoraLoaderModelOnly`、`Note Plus (mtb)`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
