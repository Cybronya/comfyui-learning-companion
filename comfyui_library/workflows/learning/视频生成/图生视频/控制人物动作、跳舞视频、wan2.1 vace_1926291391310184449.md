---
key: 视频生成/图生视频/控制人物动作、跳舞视频、wan2.1 vace_1926291391310184449.json
name: 控制人物动作、跳舞视频、wan2.1 vace_1926291391310184449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1926291391310184449.json
hash: 9fe06a88e23d64e0
coverage: 0.729167
learned_at: 2026-10-15 22:29:53
nodes: [SetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, AddLabel, WanVideoDecode, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, easy imageSize, GetNode, GetNode, easy imageSize, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, easy imageSize, AddLabel, GetNode, WanVideoVACEEncode, ImageConcatMulti, LayerMask: BiRefNetUltraV2, LayerUtility: ImageRemoveAlpha, LayerMask: LoadBiRefNetModelV2, SetNode, WanVideoVAELoader, WanVideoTorchCompileSettings, SetNode, DepthAnything_V2, GetNode, VHS_VideoCombine, SetNode, GetImageSizeAndCount, WanVideoVACEModelSelect, SetNode, WanVideoBlockSwap, DownloadAndLoadDepthAnythingV2Model, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, ImageResizeKJ, VHS_VideoCombine, LoadImage, Note _O, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/控制人物动作、跳舞视频、wan2.1 vace_1926291391310184449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1926291391310184449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `AddLabel`
- `WanVideoDecode`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `easy imageSize`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `easy imageSize`
- `AddLabel`
- `GetNode`
- `WanVideoVACEEncode`
- `ImageConcatMulti`
- `LayerMask: BiRefNetUltraV2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerMask: LoadBiRefNetModelV2`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `DepthAnything_V2`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoBlockSwap`
- `DownloadAndLoadDepthAnythingV2Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `LoadImage`
- `Note _O`
- `VHS_LoadVideo`

## 知识

覆盖率 **73%**（35/48）

**有卡**：`WanVideoSampler`、`AddLabel`、`WanVideoDecode`、`EmptyImage`、`GetImageSizeAndCount`、`ImageConcatMulti`、`easy imageSize`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoVACEEncode`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageRemoveAlpha`、`LayerMask: LoadBiRefNetModelV2`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`DepthAnything_V2`、`VHS_VideoCombine`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`DownloadAndLoadDepthAnythingV2Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`ImageResizeKJ`、`LoadImage`、`Note _O`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
