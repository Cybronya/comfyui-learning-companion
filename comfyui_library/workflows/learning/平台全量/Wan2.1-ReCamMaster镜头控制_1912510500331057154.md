---
key: 平台全量/Wan2.1-ReCamMaster镜头控制_1912510500331057154.json
name: Wan2.1-ReCamMaster镜头控制_1912510500331057154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1-ReCamMaster镜头控制_1912510500331057154.json
hash: bb3651218809ab76
coverage: 0.666667
learned_at: 2026-11-14 01:04:39
nodes: [WanVideoBlockSwap, GetImageSizeAndCount, PreviewImage, LayerUtility: PurgeVRAM, SetNode, GetNode, PreviewImage, WanVideoSampler, SetNode, WanVideoTeaCache, SetNode, SetNode, GetNode, GetNode, ReCamMasterPoseVisualizer, GetNode, GetNode, SetNode, Florence2ModelLoader, GetImageRangeFromBatch, Florence2Run, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSLG, ImageResizeKJ, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, VHS_LoadVideo, ShowText|pysssss, ReActorFaceSwap, ReActorFaceBoost, WanVideoReCamMasterCameraEmbed, WanVideoEncode, WanVideoReCamMasterDefaultCamera]
patterns: []
missing: []
---

# 平台全量/Wan2.1-ReCamMaster镜头控制_1912510500331057154.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1-ReCamMaster镜头控制_1912510500331057154.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoTeaCache`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ReCamMasterPoseVisualizer`
- `GetNode`
- `GetNode`
- `SetNode`
- `Florence2ModelLoader`
- `GetImageRangeFromBatch`
- `Florence2Run`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `ShowText|pysssss`
- `ReActorFaceSwap`
- `ReActorFaceBoost`
- `WanVideoReCamMasterCameraEmbed`
- `WanVideoEncode`
- `WanVideoReCamMasterDefaultCamera`

## 知识

覆盖率 **67%**（26/39）

**有卡**：`WanVideoBlockSwap`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoTeaCache`、`ReCamMasterPoseVisualizer`、`Florence2ModelLoader`、`GetImageRangeFromBatch`、`Florence2Run`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_LoadVideo`、`ReActorFaceSwap`、`ReActorFaceBoost`、`WanVideoReCamMasterCameraEmbed`、`WanVideoEncode`、`WanVideoReCamMasterDefaultCamera`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、GetImageSizeAndCount、ImageResizeKJ
