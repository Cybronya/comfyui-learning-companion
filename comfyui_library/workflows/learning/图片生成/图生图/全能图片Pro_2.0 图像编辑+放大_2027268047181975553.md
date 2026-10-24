---
key: 图片生成/图生图/全能图片Pro_2.0 图像编辑+放大_2027268047181975553.json
name: 全能图片Pro_2.0 图像编辑+放大_2027268047181975553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能图片Pro_2.0 图像编辑+放大_2027268047181975553.json
hash: 42072597ba7a996b
coverage: 0.761905
learned_at: 2026-10-23 12:16:20
nodes: [KSamplerSelect, LoraLoader, TripleCLIPLoader, UNETLoader, VAELoader, LoraLoader, CLIPTextEncode, UpscaleModelLoader, Seed (rgthree), ModelSamplingFlux, BasicScheduler, DetailDaemonGraphSigmasNode, MultiplySigmas, Reroute, Image Comparer (rgthree), DetailDaemonSamplerNode, Image Comparer (rgthree), UltimateSDUpscaleCustomSample, Florence2ModelLoader, CLIPTextEncode, Florence2Run, SaveImage, Image Comparer (rgthree), Fast Groups Muter (rgthree), SaveImage, LoadImage, Image Comparer (rgthree), LoadImage, LoadImage, RH_Nano_Banana2_Gemini31Flash, LoadImage, LoadImage, SaveImage, RH_Nano_Banana2_Image2Image, easy int, easy int, easy int, Note, easy cleanGpuUsed, GetImageSize+, easy showAnything, easy showAnything, ImageResize+, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleBy, GetImageSize+, easy showAnything, easy showAnything, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageResize+, ImageCASharpening+, TTP_Image_Assy, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), PreviewImage, 图像缩放V2_孤海, Note, LoadImage, SaveImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "openflux1-v0.1.0-fast-lora.safetensors", "strength_clip": 1, "strength_model": 0.33000000000000007}
---

# 图片生成/图生图/全能图片Pro_2.0 图像编辑+放大_2027268047181975553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/全能图片Pro_2.0 图像编辑+放大_2027268047181975553.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（63 个）：
- `KSamplerSelect` ★核心
- `LoraLoader` ★核心
- `TripleCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `Seed (rgthree)`
- `ModelSamplingFlux`
- `BasicScheduler`
- `DetailDaemonGraphSigmasNode`
- `MultiplySigmas`
- `Reroute`
- `Image Comparer (rgthree)`
- `DetailDaemonSamplerNode` ★核心
- `Image Comparer (rgthree)`
- `UltimateSDUpscaleCustomSample`
- `Florence2ModelLoader`
- `CLIPTextEncode` ★核心
- `Florence2Run`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_Nano_Banana2_Image2Image`
- `easy int`
- `easy int`
- `easy int`
- `Note`
- `easy cleanGpuUsed`
- `GetImageSize+`
- `easy showAnything`
- `easy showAnything`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `GetImageSize+`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `图像缩放V2_孤海`
- `Note`
- `LoadImage`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `openflux1-v0.1.0-fast-lora.safetensors`
- `strength_model` = `0.33000000000000007`
- `strength_clip` = `1`

## 知识

覆盖率 **76%**（48/63）

**有卡**：`KSamplerSelect`、`LoraLoader`、`TripleCLIPLoader`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`UpscaleModelLoader`、`Seed (rgthree)`、`ModelSamplingFlux`、`BasicScheduler`、`DetailDaemonGraphSigmasNode`、`MultiplySigmas`、`DetailDaemonSamplerNode`、`UltimateSDUpscaleCustomSample`、`Florence2ModelLoader`、`Florence2Run`、`SaveImage`、`LoadImage`、`RH_Nano_Banana2_Gemini31Flash`、`RH_Nano_Banana2_Image2Image`、`easy int`、`easy cleanGpuUsed`、`GetImageSize+`、`ImageResize+`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageCASharpening+`、`TTP_Image_Assy`、`LayerUtility: ImageScaleByAspectRatio V2`、`图像缩放V2_孤海`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DetailDaemonSamplerNode、KSamplerSelect、SeedVR2LoadDiTModel
