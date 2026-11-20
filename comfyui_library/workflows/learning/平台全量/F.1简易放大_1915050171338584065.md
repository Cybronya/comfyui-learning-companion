---
key: 平台全量/F.1简易放大_1915050171338584065.json
name: F.1简易放大_1915050171338584065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1简易放大_1915050171338584065.json
hash: c38a8b0f51aaf4f3
coverage: 0.810811
learned_at: 2026-11-14 00:24:04
nodes: [BasicGuider, KSamplerSelect, VAEEncode, Reroute, SamplerCustomAdvanced, RandomNoise, Reroute, ImageUpscaleWithModel, UpscaleModelLoader, easy cleanGpuUsed, PreviewImage, ImageScaleToTotalPixels, UNETLoader, DualCLIPLoader, LoraLoader, ImageListToImageBatch, TTP_Image_Tile_Batch, easy imageBatchToImageList, LoraLoader, FluxGuidance, TTP_Tile_image_size, VAELoader, Reroute, LoadImage, Image Comparer (rgthree), SaveImage, ShowText|pysssss, ImageResize+, Textbox, CLIPTextEncode, RH_Captioner, CR Text Concatenate, TTP_Image_Assy, PreviewImage, easy cleanGpuUsed, VAEDecodeTiled, BasicScheduler]
patterns: [lora]
missing: []
parameters: {"lora_name": "Jojo's style.safetensors", "strength_clip": 1, "strength_model": 0.8}
---

# 平台全量/F.1简易放大_1915050171338584065.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1简易放大_1915050171338584065.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Reroute`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `ImageListToImageBatch`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `LoraLoader` ★核心
- `FluxGuidance`
- `TTP_Tile_image_size`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ShowText|pysssss`
- `ImageResize+`
- `Textbox`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `CR Text Concatenate`
- `TTP_Image_Assy`
- `PreviewImage`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `BasicScheduler`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Jojo's style.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEEncode`、`SamplerCustomAdvanced`、`RandomNoise`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`ImageListToImageBatch`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`FluxGuidance`、`TTP_Tile_image_size`、`VAELoader`、`LoadImage`、`SaveImage`、`ImageResize+`、`Textbox`、`CLIPTextEncode`、`RH_Captioner`、`CR Text Concatenate`、`TTP_Image_Assy`、`VAEDecodeTiled`、`BasicScheduler`

**用到的条目**：VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
