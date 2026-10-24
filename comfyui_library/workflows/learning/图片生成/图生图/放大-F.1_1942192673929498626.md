---
key: 图片生成/图生图/放大-F.1_1942192673929498626.json
name: 放大-F.1_1942192673929498626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/放大-F.1_1942192673929498626.json
hash: 4bd1ba909f54fa96
coverage: 0.84375
learned_at: 2026-10-23 13:03:09
nodes: [BasicGuider, KSamplerSelect, VAEEncode, VAELoader, Reroute, SamplerCustomAdvanced, VAEDecodeTiled, RandomNoise, BasicScheduler, TTP_Tile_image_size, easy imageBatchToImageList, TTP_Image_Tile_Batch, Reroute, PreviewImage, UNETLoader, DualCLIPLoader, ImageResize+, ImageListToImageBatch, UpscaleModelLoader, CLIPTextEncode, LoraLoader, LoraLoader, ImageScaleToTotalPixels, FluxGuidance, Reroute, Image Comparer (rgthree), ImageUpscaleWithModel, easy cleanGpuUsed, TTP_Image_Assy, easy cleanGpuUsed, SaveImage, LoadImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "AWPortrait CN_1.0.safetensors", "strength_clip": 1, "strength_model": 0.8}
---

# 图片生成/图生图/放大-F.1_1942192673929498626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/放大-F.1_1942192673929498626.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `BasicScheduler`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `Reroute`
- `PreviewImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ImageResize+`
- `ImageListToImageBatch`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `ImageScaleToTotalPixels`
- `FluxGuidance`
- `Reroute`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `TTP_Image_Assy`
- `easy cleanGpuUsed`
- `SaveImage`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `AWPortrait CN_1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **84%**（27/32）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEEncode`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`RandomNoise`、`BasicScheduler`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`UNETLoader`、`DualCLIPLoader`、`ImageResize+`、`ImageListToImageBatch`、`UpscaleModelLoader`、`CLIPTextEncode`、`LoraLoader`、`ImageScaleToTotalPixels`、`FluxGuidance`、`ImageUpscaleWithModel`、`easy cleanGpuUsed`、`TTP_Image_Assy`、`SaveImage`、`LoadImage`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
