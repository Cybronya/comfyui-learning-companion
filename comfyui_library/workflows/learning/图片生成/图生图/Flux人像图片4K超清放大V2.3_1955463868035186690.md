---
key: 图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json
name: Flux人像图片4K超清放大V2.3_1955463868035186690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json
hash: 429c537459e78cdf
coverage: 0.888889
learned_at: 2026-10-23 11:01:55
nodes: [UNETLoader, VAELoader, UpscaleModelLoader, DualCLIPLoader, LoraLoader, StyleModelLoader, RandomNoise, BasicGuider, FluxGuidance, KSamplerSelect, BasicScheduler, Florence2ModelLoader, CR Text, Text Concatenate (JPS), CLIPTextEncode, Reroute, TTP_Tile_image_size, VAEEncode, CLIPVisionLoader, CLIPVisionEncode, VAEDecodeTiled, StyleModelApply, ImageListToImageBatch, easy imageBatchToImageList, TTP_Image_Tile_Batch, ImageScaleToTotalPixels, ImageUpscaleWithModel, Florence2Run, Note, LoadImage, ImageResizeKJ, TTP_Image_Assy, SamplerCustomAdvanced, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "Flux Dev模型4步出图lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux人像图片4K超清放大V2.3_1955463868035186690.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `UpscaleModelLoader`
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `StyleModelLoader`
- `RandomNoise`
- `BasicGuider`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Florence2ModelLoader`
- `CR Text`
- `Text Concatenate (JPS)`
- `CLIPTextEncode` ★核心
- `Reroute`
- `TTP_Tile_image_size`
- `VAEEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `VAEDecodeTiled` ★核心
- `StyleModelApply`
- `ImageListToImageBatch`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Florence2Run`
- `Note`
- `LoadImage`
- `ImageResizeKJ`
- `TTP_Image_Assy`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Flux Dev模型4步出图lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`UNETLoader`、`VAELoader`、`UpscaleModelLoader`、`DualCLIPLoader`、`LoraLoader`、`StyleModelLoader`、`RandomNoise`、`BasicGuider`、`FluxGuidance`、`KSamplerSelect`、`BasicScheduler`、`Florence2ModelLoader`、`CR Text`、`Text Concatenate (JPS)`、`CLIPTextEncode`、`TTP_Tile_image_size`、`VAEEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAEDecodeTiled`、`StyleModelApply`、`ImageListToImageBatch`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`Florence2Run`、`LoadImage`、`ImageResizeKJ`、`TTP_Image_Assy`、`SamplerCustomAdvanced`、`SaveImage`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
