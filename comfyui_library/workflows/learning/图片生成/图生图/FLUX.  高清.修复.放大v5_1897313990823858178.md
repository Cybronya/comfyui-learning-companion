---
key: 图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json
name: FLUX.  高清.修复.放大v5_1897313990823858178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json
hash: ed837c7c430de1f6
coverage: 0.777778
learned_at: 2026-10-23 10:53:58
nodes: [Joy_caption, Joy_caption_load, Reroute, easy showAnything, DualCLIPLoader, workflow/model, LoadImage, ImageResize+, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleToTotalPixels, PreviewImage, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, TTP_Image_Assy, ConditioningCombine, Reroute, StringFunction|pysssss, VAELoader, CLIPTextEncodeFlux, CLIPTextEncode, FluxGuidance, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, VAEEncode, SamplerCustomAdvanced, ImageListToImageBatch, PreviewImage, VAEDecodeTiled, PreviewImage, Image Comparer (rgthree), Reroute, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.  高清.修复.放大v5_1897313990823858178.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Joy_caption`
- `Joy_caption_load`
- `Reroute`
- `easy showAnything`
- `DualCLIPLoader`
- `workflow/model`
- `LoadImage`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `TTP_Image_Assy`
- `ConditioningCombine`
- `Reroute`
- `StringFunction|pysssss`
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageListToImageBatch`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `SaveImage`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`Joy_caption`、`Joy_caption_load`、`DualCLIPLoader`、`workflow/model`、`LoadImage`、`ImageResize+`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`TTP_Image_Assy`、`ConditioningCombine`、`StringFunction|pysssss`、`VAELoader`、`CLIPTextEncodeFlux`、`CLIPTextEncode`、`FluxGuidance`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEEncode`、`SamplerCustomAdvanced`、`ImageListToImageBatch`、`VAEDecodeTiled`、`SaveImage`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、CLIPTextEncodeFlux、VAEDecodeTiled
