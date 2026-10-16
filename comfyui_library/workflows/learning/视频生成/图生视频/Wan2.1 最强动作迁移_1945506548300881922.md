---
key: 视频生成/图生视频/Wan2.1 最强动作迁移_1945506548300881922.json
name: Wan2.1 最强动作迁移_1945506548300881922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1945506548300881922.json
hash: b96ee5616eb3763f
coverage: 0.72
learned_at: 2026-10-15 22:30:42
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSLG, WanVideoSampler, WanVideoExperimentalArgs, WanVideoVACEEncode, SetNode, WanVideoBlockSwap, SetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoVAELoader, SetNode, WanVideoModelLoader, DownloadAndLoadDepthAnythingV2Model, easy imageSize, DepthAnything_V2, AIO_Preprocessor, Blend, Note, ImpactSwitch, RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, CR Text Concatenate, JjkText, GetImageSizeAndCount, WanVideoTextEncode, AddLabel, LoadImage, ImageResizeKJ, MathExpression|pysssss, VHS_VideoInfoSource, VHS_LoadVideo, ShowText, EmptyImage, ImageConcatMulti, AddLabel, WanVideoTorchCompileSettings, VHS_VideoCombine, PreviewImage, Int, easy cleanGpuUsed, GetNode, WanVideoDecode, ColorMatch, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 最强动作迁移_1945506548300881922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1945506548300881922.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoVACEEncode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoModelLoader`
- `DownloadAndLoadDepthAnythingV2Model`
- `easy imageSize`
- `DepthAnything_V2`
- `AIO_Preprocessor`
- `Blend`
- `Note`
- `ImpactSwitch`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text Concatenate`
- `JjkText`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `AddLabel`
- `LoadImage`
- `ImageResizeKJ`
- `MathExpression|pysssss`
- `VHS_VideoInfoSource`
- `VHS_LoadVideo`
- `ShowText`
- `EmptyImage`
- `ImageConcatMulti`
- `AddLabel`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `PreviewImage`
- `Int`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `ColorMatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **72%**（36/50）

**有卡**：`WanVideoSLG`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`DownloadAndLoadDepthAnythingV2Model`、`easy imageSize`、`DepthAnything_V2`、`AIO_Preprocessor`、`Blend`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text Concatenate`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`AddLabel`、`LoadImage`、`ImageResizeKJ`、`MathExpression|pysssss`、`VHS_VideoInfoSource`、`VHS_LoadVideo`、`ShowText`、`EmptyImage`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`Int`、`easy cleanGpuUsed`、`WanVideoDecode`、`ColorMatch`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
