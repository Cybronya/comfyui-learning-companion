---
key: 平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json
name: ✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json
hash: 8e6c50bb4f7ace39
coverage: 0.631579
learned_at: 2026-11-14 01:21:06
nodes: [ConditioningZeroOut, CLIPTextEncode, VAELoader, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, ShowText|pysssss, ConditioningAverage, SetNode, GetNode, VAEDecodeTiled, easy imageListToImageBatch, TTP_condtobatch, TTP_CoordinateSplitter, BasicGuider, SetNode, easy imageBatchToImageList, CLIPTextEncode, ImageUpscaleWithModel, TTP_condsetarea_merge, ImageResizeKJ, TTP_Image_Tile_Batch, TTP_Image_Assy, ImageSmartSharpen+, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Florence2Run, CR Text Concatenate, CR Text Concatenate, SetNode, Florence2Run, GetNode, GetNode, CR Text, ShowText|pysssss, FluxGuidance, SetNode, GetNode, GetNode, DetailDaemonSamplerNode, GetNode, BasicScheduler, RandomNoise, SamplerCustomAdvanced, GetNode, VAEEncode, InjectLatentNoise+, UpscaleModelLoader, DualCLIPLoader, EasyCache, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, PreviewImage, TTP_Tile_image_size, UNETLoader, FluxGuidance, Int, ImageScaleToTotalPixels, Float, Int, Florence2ModelLoader, KSamplerSelect, Image Comparer (rgthree), SaveImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json

> 来源文件 `comfyui_library/workflows/平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `ConditioningAverage`
- `SetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `TTP_condtobatch`
- `TTP_CoordinateSplitter`
- `BasicGuider`
- `SetNode`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `TTP_condsetarea_merge`
- `ImageResizeKJ`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `ImageSmartSharpen+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Florence2Run`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `SetNode`
- `Florence2Run`
- `GetNode`
- `GetNode`
- `CR Text`
- `ShowText|pysssss`
- `FluxGuidance`
- `SetNode`
- `GetNode`
- `GetNode`
- `DetailDaemonSamplerNode` ★核心
- `GetNode`
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `InjectLatentNoise+`
- `UpscaleModelLoader`
- `DualCLIPLoader`
- `EasyCache`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `TTP_Tile_image_size`
- `UNETLoader` ★核心
- `FluxGuidance`
- `Int`
- `ImageScaleToTotalPixels`
- `Float`
- `Int`
- `Florence2ModelLoader`
- `KSamplerSelect` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **63%**（48/76）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`ConditioningAverage`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`TTP_condtobatch`、`TTP_CoordinateSplitter`、`BasicGuider`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`TTP_condsetarea_merge`、`ImageResizeKJ`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`ImageSmartSharpen+`、`Florence2Run`、`CR Text Concatenate`、`CR Text`、`FluxGuidance`、`DetailDaemonSamplerNode`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEEncode`、`InjectLatentNoise+`、`UpscaleModelLoader`、`DualCLIPLoader`、`EasyCache`、`LoraLoaderModelOnly`、`UNETLoader`、`TTP_Tile_image_size`、`Int`、`ImageScaleToTotalPixels`、`Float`、`Florence2ModelLoader`、`KSamplerSelect`、`SaveImage`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、DetailDaemonSamplerNode、FluxGuidance
