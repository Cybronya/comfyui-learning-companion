---
key: 视频生成/图生视频/Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json
name: Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1933759507254435841.json
hash: d8fcff0a854b1a61
coverage: 0.9375
learned_at: 2026-10-15 22:30:14
nodes: [LoadImage, WanVideoModelLoader, WanVideoBlockSwap, JWInteger, ImpactSwitch, ImageMirror, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoSampler, ImageFromBatch+, WanVideoExperimentalArgs, WanVideoSLG, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoDecode, ImpactSwitch, VHS_VideoCombine, DepthAnything_V2, JWInteger, WanVideoTextEncode, ImageFromBatch+, VHS_MergeImages, WanVideoVACEEncode, DownloadAndLoadDepthAnythingV2Model, WanVideoVAELoader, ImageResizeKJ, ImageRepeat, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, OpenposePreprocessor, CR Prompt Text, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933759507254435841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `JWInteger`
- `ImpactSwitch`
- `ImageMirror`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `ImageFromBatch+`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `DepthAnything_V2`
- `JWInteger`
- `WanVideoTextEncode`
- `ImageFromBatch+`
- `VHS_MergeImages`
- `WanVideoVACEEncode`
- `DownloadAndLoadDepthAnythingV2Model`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `ImageRepeat`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `OpenposePreprocessor`
- `CR Prompt Text`
- `VHS_LoadVideo`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`LoadImage`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`JWInteger`、`ImageMirror`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoSampler`、`ImageFromBatch+`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`DepthAnything_V2`、`WanVideoTextEncode`、`VHS_MergeImages`、`WanVideoVACEEncode`、`DownloadAndLoadDepthAnythingV2Model`、`WanVideoVAELoader`、`ImageResizeKJ`、`ImageRepeat`、`LayerUtility: ImageScaleByAspectRatio V2`、`OpenposePreprocessor`、`CR Prompt Text`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、OpenposePreprocessor、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode
