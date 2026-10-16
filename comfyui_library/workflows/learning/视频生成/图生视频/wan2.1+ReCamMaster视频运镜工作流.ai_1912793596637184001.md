---
key: 视频生成/图生视频/wan2.1+ReCamMaster视频运镜工作流.ai_1912793596637184001.json
name: wan2.1+ReCamMaster视频运镜工作流.ai_1912793596637184001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1912793596637184001.json
hash: 7ad204fbc9c9fd9f
coverage: 0.884615
learned_at: 2026-10-15 22:29:32
nodes: [WanVideoTorchCompileSettings, GetImageRangeFromBatch, DownloadAndLoadFlorence2Model, Florence2Run, ImageResizeKJ, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ReCamMasterPoseVisualizer, WanVideoModelLoader, WanVideoTextEncode, Note Plus (mtb), WanVideoBlockSwap, WanVideoSampler, AddLabel, WanVideoDecode, WanVideoExperimentalArgs, PreviewImage, WanVideoTeaCache, PreviewImage, Note, VHS_LoadVideo, VHS_VideoCombine, WanVideoReCamMasterCameraEmbed, WanVideoEncode, WidgetToString, WanVideoReCamMasterDefaultCamera]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1+ReCamMaster视频运镜工作流.ai_1912793596637184001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912793596637184001.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `WanVideoTorchCompileSettings`
- `GetImageRangeFromBatch`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `ImageResizeKJ`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ReCamMasterPoseVisualizer`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Note Plus (mtb)`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `AddLabel`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `WanVideoTeaCache`
- `PreviewImage`
- `Note`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoReCamMasterCameraEmbed`
- `WanVideoEncode`
- `WidgetToString`
- `WanVideoReCamMasterDefaultCamera`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`WanVideoTorchCompileSettings`、`GetImageRangeFromBatch`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`ImageResizeKJ`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ReCamMasterPoseVisualizer`、`WanVideoModelLoader`、`WanVideoTextEncode`、`Note Plus (mtb)`、`WanVideoBlockSwap`、`WanVideoSampler`、`AddLabel`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoReCamMasterCameraEmbed`、`WanVideoEncode`、`WidgetToString`、`WanVideoReCamMasterDefaultCamera`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、ImageResizeKJ、AddLabel
