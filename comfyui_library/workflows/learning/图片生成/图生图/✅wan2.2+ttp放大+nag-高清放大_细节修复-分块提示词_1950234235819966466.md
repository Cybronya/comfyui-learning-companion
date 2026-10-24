---
key: 图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json
name: ✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json
hash: 73c2fd21926ea8a3
coverage: 0.597222
learned_at: 2026-10-23 11:47:43
nodes: [SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, SetNode, VAEDecodeTiled, easy imageListToImageBatch, TTP_condtobatch, TTP_CoordinateSplitter, SetNode, easy imageBatchToImageList, CLIPTextEncode, ImageUpscaleWithModel, ImageResizeKJ, TTP_Image_Tile_Batch, TTP_Image_Assy, PreviewImage, ImageSmartSharpen+, SetNode, GetNode, GetNode, GetNode, GetNode, Florence2Run, Florence2Run, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, ImageScaleToTotalPixels, easy cleanGpuUsed, TTP_Tile_image_size, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, CLIPLoader, SetNode, SetNode, VAELoader, TTP_condsetarea_merge, SaveImage, Image Comparer (rgthree), CLIPTextEncode, UpscaleModelLoader, ConditioningAverage, GetNode, GetNode, NAGGuider, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEEncode, RandomNoise, KSamplerSelect, ModelSamplingSD3, ShowText|pysssss, ShowText|pysssss, Florence2ModelLoader, CR Text Concatenate, CR Text Concatenate, CR Text, SetNode, SetNode, BasicScheduler, CR Text, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info]
patterns: []
missing: []
---

# 图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `TTP_condtobatch`
- `TTP_CoordinateSplitter`
- `SetNode`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageResizeKJ`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `PreviewImage`
- `ImageSmartSharpen+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Florence2Run`
- `Florence2Run`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `TTP_Tile_image_size`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `TTP_condsetarea_merge`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ConditioningAverage`
- `GetNode`
- `GetNode`
- `NAGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Florence2ModelLoader`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `CR Text`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Manual XY Entry Info`

## 知识

覆盖率 **60%**（43/72）

**有卡**：`CLIPTextEncode`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`TTP_condtobatch`、`TTP_CoordinateSplitter`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`ImageSmartSharpen+`、`Florence2Run`、`LoadImage`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TTP_condsetarea_merge`、`SaveImage`、`UpscaleModelLoader`、`ConditioningAverage`、`NAGGuider`、`SamplerCustomAdvanced`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`ModelSamplingSD3`、`Florence2ModelLoader`、`CR Text Concatenate`、`CR Text`、`BasicScheduler`、`Manual XY Entry Info`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
