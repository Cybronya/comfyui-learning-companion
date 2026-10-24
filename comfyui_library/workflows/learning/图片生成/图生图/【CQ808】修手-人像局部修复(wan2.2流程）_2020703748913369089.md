---
key: 图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json
name: 【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json
hash: 0d7a37ee7e151fa6
coverage: 0.952381
learned_at: 2026-10-23 11:48:26
nodes: [CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingSD3, VAEEncode, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, Florence2Run, DownloadAndLoadFlorence2Model, CLIPLoader, Image Comparer (rgthree), VAEDecode, VAELoader, LayerMask: MaskPreview, UNETLoader, KSampler, LoadImage, InpaintModelConditioning, RepeatLatentBatch, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 955524097782391, "steps": 10}
---

# 图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【CQ808】修手-人像局部修复(wan2.2流程）_2020703748913369089.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAELoader`
- `LayerMask: MaskPreview`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `InpaintModelConditioning`
- `RepeatLatentBatch`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `955524097782391`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEEncode`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`LayerMask: MaskPreview`、`UNETLoader`、`KSampler`、`LoadImage`、`InpaintModelConditioning`、`RepeatLatentBatch`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
