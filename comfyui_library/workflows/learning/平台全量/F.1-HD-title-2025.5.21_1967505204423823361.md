---
key: 平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json
name: F.1-HD-title-2025.5.21_1967505204423823361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json
hash: 2de6bb8449f4900e
coverage: 0.657895
learned_at: 2026-11-14 00:24:02
nodes: [Anything Everywhere, TTP_Tile_image_size, VAEDecodeTiled, GetNode, KSamplerSelect, RandomNoise, VAEEncode, easy imageBatchToImageList, TTP_Image_Tile_Batch, ImageListToImageBatch, GetNode, GetNode, SetNode, SamplerCustomAdvanced, Reroute (rgthree), MarkdownNote, FluxGuidance, BasicGuider, Reroute (rgthree), Reroute (rgthree), Reroute (rgthree), Fast Groups Bypasser (rgthree), ImageResizeKJ, ImageScaleBy, ImageUpscaleWithModel, ImageSharpen, TTP_Image_Assy, SetNode, LoadImage, SaveImage, VAELoader, DualCLIPLoader, UpscaleModelLoader, LoraLoader, Image Comparer (rgthree), CLIPTextEncode, BasicScheduler, UNETLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "Flux Dev model 4 steps to draw LoRa._Flux Dev 4-step.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1-HD-title-2025.5.21_1967505204423823361.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Anything Everywhere`
- `TTP_Tile_image_size`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ImageListToImageBatch`
- `GetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute (rgthree)`
- `MarkdownNote`
- `FluxGuidance`
- `BasicGuider`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Reroute (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImageSharpen`
- `TTP_Image_Assy`
- `SetNode`
- `LoadImage`
- `SaveImage`
- `VAELoader`
- `DualCLIPLoader`
- `UpscaleModelLoader`
- `LoraLoader` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Flux Dev model 4 steps to draw LoRa._Flux Dev 4-step.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`TTP_Tile_image_size`、`VAEDecodeTiled`、`KSamplerSelect`、`RandomNoise`、`VAEEncode`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`SamplerCustomAdvanced`、`FluxGuidance`、`BasicGuider`、`ImageResizeKJ`、`ImageScaleBy`、`ImageUpscaleWithModel`、`ImageSharpen`、`TTP_Image_Assy`、`LoadImage`、`SaveImage`、`VAELoader`、`DualCLIPLoader`、`UpscaleModelLoader`、`LoraLoader`、`CLIPTextEncode`、`BasicScheduler`、`UNETLoader`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
