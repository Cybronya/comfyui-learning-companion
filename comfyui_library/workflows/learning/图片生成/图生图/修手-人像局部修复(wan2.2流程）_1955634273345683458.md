---
key: 图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json
name: 修手-人像局部修复(wan2.2流程）_1955634273345683458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json
hash: 172e1551db70742d
coverage: 0.90625
learned_at: 2026-10-23 12:12:35
nodes: [LoadImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingSD3, VAEEncode, SaveImage, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, Florence2Run, DownloadAndLoadFlorence2Model, InpaintModelConditioning, CLIPLoader, Image Comparer (rgthree), VAEDecode, VAELoader, UNETLoader, LoraLoader, CLIPTextEncode, VAEEncode, CLIPTextEncode, CFGZeroStarAndInit, VAEDecode, PreviewImage, Image Comparer (rgthree), LayerMask: MaskPreview, CR Text, LoraLoader, UNETLoader, KSampler, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 393864461197190, "steps": 10, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/修手-人像局部修复(wan2.2流程）_1955634273345683458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `SaveImage`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `InpaintModelConditioning`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerMask: MaskPreview`
- `CR Text`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `393864461197190`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEEncode`、`SaveImage`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`InpaintModelConditioning`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`UNETLoader`、`LoraLoader`、`CFGZeroStarAndInit`、`LayerMask: MaskPreview`、`CR Text`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
