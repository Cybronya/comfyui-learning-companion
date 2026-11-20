---
key: 平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json
name: 【9成还原】wan2.1图像4K超清放大_1962886386615562242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json
hash: f736d1020083d0d8
coverage: 0.697674
learned_at: 2026-11-14 01:21:25
nodes: [easy int, easy int, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, Anything Everywhere3, Note, easy cleanGpuUsed, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, UpscaleModelLoader, ImageUpscaleWithModel, MathExpression|pysssss, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, Image Comparer (rgthree), JjkText, wanBlockSwap, SetNode, SaveImage, VAEDecode, PreviewImage, KSampler, VAEEncode, LayerUtility: PurgeVRAM, ModelSamplingSD3, Note, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, LayerUtility: PurgeVRAM, SetNode, RH_Captioner, easy promptConcat, LoadImage, LayerUtility: PurgeVRAM V2, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 912308638023186, "steps": 12}
---

# 平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json

> 来源文件 `comfyui_library/workflows/平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `easy int`
- `easy int`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `Note`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `MathExpression|pysssss`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `Image Comparer (rgthree)`
- `JjkText`
- `wanBlockSwap`
- `SetNode`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `RH_Captioner`
- `easy promptConcat`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `912308638023186`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `0.1`

## 知识

覆盖率 **70%**（30/43）

**有卡**：`easy int`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`wanBlockSwap`、`SaveImage`、`VAEDecode`、`KSampler`、`VAEEncode`、`ModelSamplingSD3`、`CLIPTextEncode`、`RH_Captioner`、`easy promptConcat`、`LoadImage`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
