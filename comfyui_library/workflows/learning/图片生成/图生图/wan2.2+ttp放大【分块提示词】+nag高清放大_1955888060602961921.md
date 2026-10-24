---
key: 图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json
name: wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json
hash: 7f331c66ace246a3
coverage: 0.597222
learned_at: 2026-10-23 11:45:58
nodes: [SetNode, SetNode, CLIPTextEncode, SetNode, TTP_condtobatch, TTP_CoordinateSplitter, easy imageBatchToImageList, ImageResizeKJ, TTP_Image_Tile_Batch, ImageSmartSharpen+, Florence2Run, Florence2Run, GetNode, GetNode, ImageScaleToTotalPixels, easy cleanGpuUsed, TTP_Tile_image_size, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, CLIPLoader, SetNode, SetNode, VAELoader, CLIPTextEncode, UpscaleModelLoader, ConditioningAverage, GetNode, NAGGuider, SamplerCustomAdvanced, GetNode, GetNode, VAEEncode, RandomNoise, KSamplerSelect, ModelSamplingSD3, ShowText|pysssss, ShowText|pysssss, CR Text Concatenate, CR Text Concatenate, CR Text, SetNode, BasicScheduler, CR Text, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, Florence2ModelLoader, PreviewImage, ImageUpscaleWithModel, CLIPTextEncode, TTP_condsetarea_merge, GetNode, easy imageListToImageBatch, TTP_Image_Assy, GetNode, VAEDecodeTiled, SetNode, GetNode, GetNode, SaveImage, Image Comparer (rgthree), SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, SetNode, GetNode]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `TTP_condtobatch`
- `TTP_CoordinateSplitter`
- `easy imageBatchToImageList`
- `ImageResizeKJ`
- `TTP_Image_Tile_Batch`
- `ImageSmartSharpen+`
- `Florence2Run`
- `Florence2Run`
- `GetNode`
- `GetNode`
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
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `ConditioningAverage`
- `GetNode`
- `NAGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `SetNode`
- `BasicScheduler`
- `CR Text`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Florence2ModelLoader`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `TTP_condsetarea_merge`
- `GetNode`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **60%**（43/72）

**有卡**：`CLIPTextEncode`、`TTP_condtobatch`、`TTP_CoordinateSplitter`、`easy imageBatchToImageList`、`ImageResizeKJ`、`TTP_Image_Tile_Batch`、`ImageSmartSharpen+`、`Florence2Run`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`TTP_Tile_image_size`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`ConditioningAverage`、`NAGGuider`、`SamplerCustomAdvanced`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`ModelSamplingSD3`、`CR Text Concatenate`、`CR Text`、`BasicScheduler`、`Manual XY Entry Info`、`Florence2ModelLoader`、`ImageUpscaleWithModel`、`TTP_condsetarea_merge`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`VAEDecodeTiled`、`SaveImage`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
