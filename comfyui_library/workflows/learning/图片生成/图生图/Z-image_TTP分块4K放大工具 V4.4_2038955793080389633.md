---
key: 图片生成/图生图/Z-image_TTP分块4K放大工具 V4.4_2038955793080389633.json
name: Z-image_TTP分块4K放大工具 V4.4_2038955793080389633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image_TTP分块4K放大工具 V4.4_2038955793080389633.json
hash: 51788c22efde7eee
coverage: 0.782609
learned_at: 2026-10-23 11:31:13
nodes: [PreviewImage, easy imageSize, TTP_Image_Tile_Batch, Florence2Run, Any Switch (rgthree), TTP_condsetarea_merge, SaveImage, easy imageBatchToImageList, TTP_Image_Tile_Batch, ConditioningZeroOut, ShowText|pysssss, CLIPTextEncode, ShowText|pysssss, SeedVR2LoadVAEModel, Image Comparer (rgthree), easy imageSize, Note, DownloadAndLoadFlorence2Model, Florence2Run, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, TTP_condtobatch, CLIPTextEncode, TTP_Tile_image_size, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, PreviewImage, PreviewImage, easy imageSize, PreviewImage, Any Switch (rgthree), Note, ConditioningAverage, CLIPTextEncode, LayerUtility: PurgeVRAM V2, VAEEncodeTiled, VAEEncodeTiled, TTPlanet_TileSimple_Preprocessor, JWImageResizeByLongerSide, PreviewImage, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, easy imageListToImageBatch, VAEDecodeTiled, easy imageSize, VAEDecodeTiled, TTP_Tile_image_size, JWImageResizeByLongerSide, TTP_Image_Assy, easy imageColorMatch, ConditioningZeroOut, easy showAnything, LoadImagesFromDir //Inspire, Seed Generator, Fast Groups Muter (rgthree), LoadImage, CFGGuider, KSamplerSelect, Fast Groups Bypasser (rgthree), DetailDaemonSamplerNode, ModelSamplingAuraFlow, RandomNoise, Image Comparer (rgthree), SamplerCustomAdvanced, BasicScheduler, RandomNoise, Text Concatenate, JWStringMultiline, ModelSamplingAuraFlow, CFGGuider, CLIPLoader, UNETLoader, VAELoader, easy imageBatchToImageList, BasicScheduler, SimpleMathSlider+, easy imageSize, SamplerCustomAdvanced, DetailDaemonSamplerNode, KSamplerSelect, TTPlanet_TileSimple_Preprocessor, PreviewImage, ModelPatchLoader, QwenImageDiffsynthControlnet, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), Image Save, SaveImage, Image Save, easy imageColorMatch, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Z-image_TTP分块4K放大工具 V4.4_2038955793080389633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image_TTP分块4K放大工具 V4.4_2038955793080389633.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `PreviewImage`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `Florence2Run`
- `Any Switch (rgthree)`
- `TTP_condsetarea_merge`
- `SaveImage`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ConditioningZeroOut`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `easy imageSize`
- `Note`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `TTP_condtobatch`
- `CLIPTextEncode` ★核心
- `TTP_Tile_image_size`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `PreviewImage`
- `PreviewImage`
- `easy imageSize`
- `PreviewImage`
- `Any Switch (rgthree)`
- `Note`
- `ConditioningAverage`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `TTPlanet_TileSimple_Preprocessor`
- `JWImageResizeByLongerSide`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `easy imageListToImageBatch`
- `VAEDecodeTiled` ★核心
- `easy imageSize`
- `VAEDecodeTiled` ★核心
- `TTP_Tile_image_size`
- `JWImageResizeByLongerSide`
- `TTP_Image_Assy`
- `easy imageColorMatch`
- `ConditioningZeroOut`
- `easy showAnything`
- `LoadImagesFromDir //Inspire`
- `Seed Generator`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `DetailDaemonSamplerNode` ★核心
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `RandomNoise`
- `Text Concatenate`
- `JWStringMultiline`
- `ModelSamplingAuraFlow`
- `CFGGuider`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `easy imageBatchToImageList`
- `BasicScheduler`
- `SimpleMathSlider+`
- `easy imageSize`
- `SamplerCustomAdvanced` ★核心
- `DetailDaemonSamplerNode` ★核心
- `KSamplerSelect` ★核心
- `TTPlanet_TileSimple_Preprocessor`
- `PreviewImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `Image Save`
- `SaveImage`
- `Image Save`
- `easy imageColorMatch`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **78%**（72/92）

**有卡**：`easy imageSize`、`TTP_Image_Tile_Batch`、`Florence2Run`、`TTP_condsetarea_merge`、`SaveImage`、`easy imageBatchToImageList`、`ConditioningZeroOut`、`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`DownloadAndLoadFlorence2Model`、`LayerUtility: NumberCalculatorV2`、`TTP_condtobatch`、`TTP_Tile_image_size`、`ConditioningAverage`、`LayerUtility: PurgeVRAM V2`、`VAEEncodeTiled`、`TTPlanet_TileSimple_Preprocessor`、`JWImageResizeByLongerSide`、`easy imageListToImageBatch`、`VAEDecodeTiled`、`TTP_Image_Assy`、`easy imageColorMatch`、`LoadImagesFromDir //Inspire`、`Seed Generator`、`LoadImage`、`CFGGuider`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`ModelSamplingAuraFlow`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicScheduler`、`Text Concatenate`、`JWStringMultiline`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`SimpleMathSlider+`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`Image Save`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、QwenImageDiffsynthControlnet、CFGGuider
