---
key: 图片生成/文生图/Testing Anima-Edit loras and IC-methods_2078374813801996290.json
name: Testing Anima-Edit loras and IC-methods_2078374813801996290
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Testing Anima-Edit loras and IC-methods_2078374813801996290.json
hash: 5748d9d377ef31c2
coverage: 0.788462
learned_at: 2026-10-20 00:20:09
nodes: [PreviewImage, InpaintModelConditioning, PreviewImage, ApplyCosmosReferenceLatent, CLIPTextEncode, VAEEncode, KSampler, KSampler, KSampler, CLIPTextEncode, VAEDecode, PreviewImage, PreviewImage, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, PreviewImage, StringReplace, PreviewAny, Crop Image TargetSize (JPS), VAEDecodeTiled, VAEDecode, SaveImage, AddLabel, AILab_ImageCompare, SaveImage, Seed (rgthree), Seed (rgthree), ApplyCosmosReferenceLatent, AddLabel, AddLabel, SaveImage, AILab_ICLoRAConcat, Seed (rgthree), SaveImage, AddLabel, ImageResize+, PrimitiveStringMultiline, MarkdownNote, XB_UNetNameBroadcaster, EnhancedLoadDiffusionModel, LoraLoaderModelOnly, PrimitiveStringMultiline, StringReplace, PreviewAny, VAELoader, CLIPLoader, Power Lora Loader (rgthree), AnimaLLLiteApply, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "simple", "seed": 668690767681962, "steps": 20}
---

# 图片生成/文生图/Testing Anima-Edit loras and IC-methods_2078374813801996290.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Testing Anima-Edit loras and IC-methods_2078374813801996290.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `PreviewImage`
- `InpaintModelConditioning`
- `PreviewImage`
- `ApplyCosmosReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PreviewImage`
- `StringReplace`
- `PreviewAny`
- `Crop Image TargetSize (JPS)`
- `VAEDecodeTiled` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `AILab_ImageCompare`
- `SaveImage`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `ApplyCosmosReferenceLatent`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `AILab_ICLoRAConcat`
- `Seed (rgthree)`
- `SaveImage`
- `AddLabel`
- `ImageResize+`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `XB_UNetNameBroadcaster`
- `EnhancedLoadDiffusionModel`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `StringReplace`
- `PreviewAny`
- `VAELoader`
- `CLIPLoader`
- `Power Lora Loader (rgthree)`
- `AnimaLLLiteApply`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `668690767681962`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`InpaintModelConditioning`、`ApplyCosmosReferenceLatent`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`VAEDecode`、`StringReplace`、`Crop Image TargetSize (JPS)`、`VAEDecodeTiled`、`SaveImage`、`AddLabel`、`AILab_ImageCompare`、`Seed (rgthree)`、`AILab_ICLoRAConcat`、`ImageResize+`、`XB_UNetNameBroadcaster`、`EnhancedLoadDiffusionModel`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`Power Lora Loader (rgthree)`、`AnimaLLLiteApply`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、Seed (rgthree)
