---
key: 图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json
name: 【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json
hash: c44633cb28e7eba4
coverage: 0.857143
learned_at: 2026-10-23 11:51:16
nodes: [VAEEncode, VAEEncode, ImageUpscaleWithModel, easy cleanGpuUsed, Image Comparer (rgthree), LayerUtility: PurgeVRAM, VAEDecode, UpscaleModelLoader, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, Anything Everywhere3, easy cleanGpuUsed, CLIPTextEncode, VAEDecode, easy seed, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, wanBlockSwap, LoraLoaderModelOnly, wanBlockSwap, ModelSamplingSD3, LayerUtility: PurgeVRAM, easy cleanGpuUsed, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, KSampler, CLIPTextEncode, Image Comparer (rgthree), KSampler, ImageResizeKJv2, RH_Captioner, LayerUtility: PurgeVRAM V2, JjkText, easy promptConcat, easy showAnything, easy int, Note, MathExpression|pysssss, easy int, LoadImage, ModelSamplingSD3, PreviewImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.35, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 666, "steps": 20}
---

# 图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `ImageResizeKJv2`
- `RH_Captioner`
- `LayerUtility: PurgeVRAM V2`
- `JjkText`
- `easy promptConcat`
- `easy showAnything`
- `easy int`
- `Note`
- `MathExpression|pysssss`
- `easy int`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `666`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `0.35`

## 知识

覆盖率 **86%**（42/49）

**有卡**：`VAEEncode`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`UpscaleModelLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`easy seed`、`wanBlockSwap`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ImageResizeKJv2`、`RH_Captioner`、`LayerUtility: PurgeVRAM V2`、`easy promptConcat`、`easy int`、`MathExpression|pysssss`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
