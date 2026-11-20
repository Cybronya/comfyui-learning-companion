---
key: 平台全量/wan2.1 ReCamMaster视频运镜工作流-StarAI_1911402610878836738.json
name: wan2.1 ReCamMaster视频运镜工作流-StarAI_1911402610878836738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1 ReCamMaster视频运镜工作流-StarAI_1911402610878836738.json
hash: 51fffba77789edea
coverage: 0.884615
learned_at: 2026-11-14 01:19:03
nodes: [WanVideoTorchCompileSettings, GetImageRangeFromBatch, DownloadAndLoadFlorence2Model, Florence2Run, ImageResizeKJ, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ReCamMasterPoseVisualizer, WanVideoModelLoader, VHS_VideoCombine, WanVideoTextEncode, Note Plus (mtb), WanVideoBlockSwap, VHS_LoadVideo, WanVideoReCamMasterCameraEmbed, WanVideoSampler, AddLabel, WanVideoDecode, WanVideoExperimentalArgs, PreviewImage, WanVideoTeaCache, PreviewImage, Note, WanVideoReCamMasterDefaultCamera, WanVideoEncode, WidgetToString]
patterns: []
missing: []
---

# 平台全量/wan2.1 ReCamMaster视频运镜工作流-StarAI_1911402610878836738.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1 ReCamMaster视频运镜工作流-StarAI_1911402610878836738.json`

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
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `Note Plus (mtb)`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `WanVideoReCamMasterCameraEmbed`
- `WanVideoSampler` ★核心
- `AddLabel`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `WanVideoTeaCache`
- `PreviewImage`
- `Note`
- `WanVideoReCamMasterDefaultCamera`
- `WanVideoEncode`
- `WidgetToString`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`WanVideoTorchCompileSettings`、`GetImageRangeFromBatch`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`ImageResizeKJ`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ReCamMasterPoseVisualizer`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`Note Plus (mtb)`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoReCamMasterCameraEmbed`、`WanVideoSampler`、`AddLabel`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoReCamMasterDefaultCamera`、`WanVideoEncode`、`WidgetToString`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ、AddLabel
