---
key: 图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json
name: 图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json
hash: c7ac9467915edd58
coverage: 0.923077
learned_at: 2026-10-21 00:51:04
nodes: [SamplerCustomAdvanced, KSamplerSelect, RandomNoise, BasicGuider, FluxGuidance, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, ImageListToImageBatch, VAEDecodeTiled, TTP_Tile_image_size, TTP_Image_Tile_Batch, VAEEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, BasicScheduler, PreviewImage, CLIPTextEncode, LoadImage, LoraLoader, TTP_Image_Assy, SaveImage, DualCLIPLoader, easy imageBatchToImageList, VAELoader, UNETLoader, UpscaleModelLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageListToImageBatch`
- `VAEDecodeTiled` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `BasicScheduler`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoader` ★核心
- `TTP_Image_Assy`
- `SaveImage`
- `DualCLIPLoader`
- `easy imageBatchToImageList`
- `VAELoader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`FluxGuidance`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageListToImageBatch`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAEEncode`、`ImageScaleToTotalPixels`、`BasicScheduler`、`CLIPTextEncode`、`LoadImage`、`LoraLoader`、`TTP_Image_Assy`、`SaveImage`、`DualCLIPLoader`、`easy imageBatchToImageList`、`VAELoader`、`UNETLoader`、`UpscaleModelLoader`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
