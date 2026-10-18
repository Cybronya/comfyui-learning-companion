---
key: 视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json
name: VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json
hash: 7845084d66efaeb2
coverage: 0.813953
learned_at: 2026-10-15 22:29:50
nodes: [Note Plus (mtb), WanVideoVAELoader, DownloadAndLoadDepthAnythingV2Model, Note, Note, JWInteger, WanVideoExperimentalArgs, PreviewImage, PreviewImage, DepthAnything_V2, Blend, Note, Note, OpenposePreprocessor, ImageMirror, JWInteger, VHS_VideoCombine, LoadWanVideoT5TextEncoder, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_MergeImages, WanVideoEnhanceAVideo, WanVideoSLG, Note, VHS_LoadVideo, DF_Integer, ImageFromBatch+, WanVideoDecode, ImageFromBatch+, ImageConcatMulti, WanVideoTextEncode, WanVideoVACEEncode, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, ImageRepeat, ImageResizeKJ, WanVideoBlockSwap, LoadImage, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1924678755254456322.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `Note Plus (mtb)`
- `WanVideoVAELoader`
- `DownloadAndLoadDepthAnythingV2Model`
- `Note`
- `Note`
- `JWInteger`
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `PreviewImage`
- `DepthAnything_V2`
- `Blend`
- `Note`
- `Note`
- `OpenposePreprocessor`
- `ImageMirror`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_MergeImages`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `Note`
- `VHS_LoadVideo`
- `DF_Integer`
- `ImageFromBatch+`
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`
- `ImageRepeat`
- `ImageResizeKJ`
- `WanVideoBlockSwap`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **81%**（35/43）

**有卡**：`Note Plus (mtb)`、`WanVideoVAELoader`、`DownloadAndLoadDepthAnythingV2Model`、`JWInteger`、`WanVideoExperimentalArgs`、`DepthAnything_V2`、`Blend`、`OpenposePreprocessor`、`ImageMirror`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`VHS_MergeImages`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`VHS_LoadVideo`、`DF_Integer`、`ImageFromBatch+`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageRepeat`、`ImageResizeKJ`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、OpenposePreprocessor、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode
