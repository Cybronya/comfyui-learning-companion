---
key: 平台全量/视频ReCamMaster运镜控制(wan2.1)_1911114894563864578.json
name: 视频ReCamMaster运镜控制(wan2.1)_1911114894563864578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频ReCamMaster运镜控制(wan2.1)_1911114894563864578.json
hash: 33b125813c04b6e7
coverage: 0.642857
learned_at: 2026-11-14 02:34:51
nodes: [CLIPLoader, Note, CLIPTextEncode, CLIPTextEncode, SetNode, WanVideoTextEncode, GetNode, SetNode, WanVideoExperimentalArgs, GetNode, GetNode, WanVideoTextEmbedBridge, GetNode, WanVideoSampler, WanVideoTeaCache, SetNode, PreviewImage, ReCamMasterPoseVisualizer, ImageResizeKJ, GetImageSizeAndCount, WanVideoEncode, SetNode, GetImageRangeFromBatch, RH_Captioner, SetNode, WanVideoDecode, ShowText|pysssss, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine, AddLabel, PreviewImage, VHS_VideoCombine, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_LoadVideo, Note, WanVideoReCamMasterDefaultCamera, GetNode, WanVideoReCamMasterCameraEmbed, WidgetToString]
patterns: []
missing: []
---

# 平台全量/视频ReCamMaster运镜控制(wan2.1)_1911114894563864578.json

> 来源文件 `comfyui_library/workflows/平台全量/视频ReCamMaster运镜控制(wan2.1)_1911114894563864578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `SetNode`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `WanVideoTextEmbedBridge`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `SetNode`
- `PreviewImage`
- `ReCamMasterPoseVisualizer`
- `ImageResizeKJ`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `SetNode`
- `GetImageRangeFromBatch`
- `RH_Captioner`
- `SetNode`
- `WanVideoDecode`
- `ShowText|pysssss`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `AddLabel`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `Note`
- `WanVideoReCamMasterDefaultCamera`
- `GetNode`
- `WanVideoReCamMasterCameraEmbed`
- `WidgetToString`

## 知识

覆盖率 **64%**（27/42）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`WanVideoTextEncode`、`WanVideoExperimentalArgs`、`WanVideoTextEmbedBridge`、`WanVideoSampler`、`WanVideoTeaCache`、`ReCamMasterPoseVisualizer`、`ImageResizeKJ`、`GetImageSizeAndCount`、`WanVideoEncode`、`GetImageRangeFromBatch`、`RH_Captioner`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`AddLabel`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`WanVideoReCamMasterDefaultCamera`、`WanVideoReCamMasterCameraEmbed`、`WidgetToString`

**用到的条目**：CLIPLoader、CLIPTextEncode、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader
