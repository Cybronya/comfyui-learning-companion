---
key: 图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json
name: Wan2.2分块超清放大_1950844011227578369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json
hash: 4d27c11e628e42fd
coverage: 0.818182
learned_at: 2026-10-23 11:28:14
nodes: [PreviewImage, Note, ShowText|pysssss, easy imageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, UpscaleModelLoader, VAEEncode, VAEDecodeTiled, Florence2Run, easy imageBatchToImageList, Reroute, TTP_Image_Tile_Batch, TTP_Image_Assy, VAELoader, CLIPLoader, Reroute, LoraLoader, DownloadAndLoadFlorence2Model, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, CLIPTextEncode, CLIPTextEncode, CFGGuider, TTP_Tile_image_size, LoadImage, BasicScheduler, KSamplerSelect, Florence2ModelLoader, SaveImage, Image Comparer (rgthree), UNETLoader]
patterns: [lora]
missing: []
parameters: {"lora_name": "Gundam_RX78_Flux.safetensors", "strength_clip": 0.85, "strength_model": 0.85}
---

# 图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2分块超清放大_1950844011227578369.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `PreviewImage`
- `Note`
- `ShowText|pysssss`
- `easy imageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `Florence2Run`
- `easy imageBatchToImageList`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `VAELoader`
- `CLIPLoader`
- `Reroute`
- `LoraLoader` ★核心
- `DownloadAndLoadFlorence2Model`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `TTP_Tile_image_size`
- `LoadImage`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `Florence2ModelLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`easy imageListToImageBatch`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VAEEncode`、`VAEDecodeTiled`、`Florence2Run`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`VAELoader`、`CLIPLoader`、`LoraLoader`、`DownloadAndLoadFlorence2Model`、`ModelSamplingSD3`、`RandomNoise`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`CFGGuider`、`TTP_Tile_image_size`、`LoadImage`、`BasicScheduler`、`KSamplerSelect`、`Florence2ModelLoader`、`SaveImage`、`UNETLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
