---
key: 图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json
name: 香蕉  移除+seedvr2.5采样高清放大_1992060255425327105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json
hash: 4d6bd9945dfd2ea3
coverage: 0.85
learned_at: 2026-10-23 13:33:19
nodes: [LoraLoaderModelOnly, SaveImage, RH_Nano_Banana_Image2Image, SeedVR2BlockSwap, Image Comparer (rgthree), UNETLoader, TeaCache, DualCLIPLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, UpscaleModelLoader, UltimateSDUpscale, LayerColor: ColorAdapter, SaveImage, Image Comparer (rgthree), SeedVR2, Note, LoadImage, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), UNETLoader, TeaCache, DualCLIPLoader, CLIPTextEncode, VAELoader, UpscaleModelLoader, UltimateSDUpscale, LayerColor: ColorAdapter, SaveImage, LoadImage, RH_Nano_Banana_Image2Image, Note, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `RH_Nano_Banana_Image2Image`
- `SeedVR2BlockSwap`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `TeaCache`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `LayerColor: ColorAdapter`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2`
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `TeaCache`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `LayerColor: ColorAdapter`
- `SaveImage`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `Note`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LoraLoaderModelOnly`、`SaveImage`、`RH_Nano_Banana_Image2Image`、`SeedVR2BlockSwap`、`UNETLoader`、`TeaCache`、`DualCLIPLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`UpscaleModelLoader`、`UltimateSDUpscale`、`LayerColor: ColorAdapter`、`SeedVR2`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、SeedVR2、SeedVR2BlockSwap、SeedVR2LoadDiTModel
