---
key: 图片生成/图生图/SeedVR2.5 + SparkVSR 高清放大1080P视频工作流_2062189239034531842.json
name: SeedVR2.5 + SparkVSR 高清放大1080P视频工作流_2062189239034531842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5 + SparkVSR 高清放大1080P视频工作流_2062189239034531842.json
hash: 0e61d31f1bc702b8
coverage: 0.886364
learned_at: 2026-10-23 11:24:56
nodes: [Float, Video Slice, LayerUtility: NumberCalculatorV2, TTP_Tile_image_size, LayerUtility: NumberCalculatorV2, GetVideoComponents, TTP_Image_Tile_Batch, ImpactFloat, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, CreateVideo, CR Text, SparkVSR_SM_Model, SparkVSR_SM_SRModel, PreviewImage, ImageCASharpening+, TTP_Image_Assy, SeedVR2LoadVAEModel, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2VideoUpscaler, SaveImage, SeedVR2LoadDiTModel, easy showAnything, easy imageSize, ImpactMinMax, Fast Groups Bypasser (rgthree), ImageFromBatch+, LoadImage, LoadImage, ImageCASharpening+, LayerUtility: PurgeVRAM V2, SparkVSR_SM_PreRefer, PreviewImage, Float, LayerUtility: PurgeVRAM V2, GetVideoComponents, easy cleanGpuUsed, RunningHub Deepcleaner, SparkVSR_SM_KSampler, CreateVideo, SaveVideo, LoadVideo, ImpactInt, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 0, "denoise": 0, "sampler_name": "32x32", "scheduler": "0x0", "seed": 647960148, "steps": 8}
---

# 图片生成/图生图/SeedVR2.5 + SparkVSR 高清放大1080P视频工作流_2062189239034531842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5 + SparkVSR 高清放大1080P视频工作流_2062189239034531842.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（44 个）：
- `Float`
- `Video Slice`
- `LayerUtility: NumberCalculatorV2`
- `TTP_Tile_image_size`
- `LayerUtility: NumberCalculatorV2`
- `GetVideoComponents`
- `TTP_Image_Tile_Batch`
- `ImpactFloat`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateVideo`
- `CR Text`
- `SparkVSR_SM_Model`
- `SparkVSR_SM_SRModel`
- `PreviewImage`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `SeedVR2LoadVAEModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `easy showAnything`
- `easy imageSize`
- `ImpactMinMax`
- `Fast Groups Bypasser (rgthree)`
- `ImageFromBatch+`
- `LoadImage`
- `LoadImage`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `SparkVSR_SM_PreRefer`
- `PreviewImage`
- `Float`
- `LayerUtility: PurgeVRAM V2`
- `GetVideoComponents`
- `easy cleanGpuUsed`
- `RunningHub Deepcleaner`
- `SparkVSR_SM_KSampler` ★核心
- `CreateVideo`
- `SaveVideo`
- `LoadVideo`
- `ImpactInt`
- `MarkdownNote`

## 关键参数

- `seed` = `647960148`
- `steps` = `8`
- `cfg` = `0`
- `sampler_name` = `32x32`
- `scheduler` = `0x0`
- `denoise` = `0`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`Float`、`Video Slice`、`LayerUtility: NumberCalculatorV2`、`TTP_Tile_image_size`、`GetVideoComponents`、`TTP_Image_Tile_Batch`、`ImpactFloat`、`ImageScaleBy`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateVideo`、`CR Text`、`SparkVSR_SM_Model`、`SparkVSR_SM_SRModel`、`ImageCASharpening+`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`SeedVR2LoadDiTModel`、`easy imageSize`、`ImpactMinMax`、`ImageFromBatch+`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`SparkVSR_SM_PreRefer`、`easy cleanGpuUsed`、`RunningHub Deepcleaner`、`SparkVSR_SM_KSampler`、`SaveVideo`、`LoadVideo`、`ImpactInt`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SparkVSR_SM_KSampler、TTP_Tile_image_size、easy imageSize、SaveImage
