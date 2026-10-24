---
key: 图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json
name: 🐮老许Gary：WAN2.2分块超清放大_2017249178774151170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json
hash: d04eb0664cd5d699
coverage: 0.771429
learned_at: 2026-10-23 13:39:13
nodes: [ShowText|pysssss, ImageUpscaleWithModel, DownloadAndLoadFlorence2Model, SaveImage, TTP_Tile_image_size, CFGGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, Anything Everywhere3, ModelSamplingSD3, LoraLoader, CLIPTextEncode, CLIPTextEncode, SetNode, VAEEncode, easy imageBatchToImageList, Reroute, UpscaleModelLoader, ImageScaleToTotalPixels, GetNode, TTP_Image_Tile_Batch, VAEDecodeTiled, TTP_Image_Assy, easy imageListToImageBatch, PreviewImage, Image Comparer (rgthree), GetNode, LoadImage, UNETLoader, Florence2ModelLoader, Florence2Run]
patterns: [lora]
missing: []
parameters: {"lora_name": "Gundam_RX78_Flux.safetensors", "strength_clip": 0.85, "strength_model": 0.85}
---

# 图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🐮老许Gary：WAN2.2分块超清放大_2017249178774151170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ShowText|pysssss`
- `ImageUpscaleWithModel`
- `DownloadAndLoadFlorence2Model`
- `SaveImage`
- `TTP_Tile_image_size`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `ModelSamplingSD3`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `Reroute`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `GetNode`
- `TTP_Image_Tile_Batch`
- `VAEDecodeTiled` ★核心
- `TTP_Image_Assy`
- `easy imageListToImageBatch`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `Florence2ModelLoader`
- `Florence2Run`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`ImageUpscaleWithModel`、`DownloadAndLoadFlorence2Model`、`SaveImage`、`TTP_Tile_image_size`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoader`、`CLIPTextEncode`、`VAEEncode`、`easy imageBatchToImageList`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`TTP_Image_Tile_Batch`、`VAEDecodeTiled`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`LoadImage`、`UNETLoader`、`Florence2ModelLoader`、`Florence2Run`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
