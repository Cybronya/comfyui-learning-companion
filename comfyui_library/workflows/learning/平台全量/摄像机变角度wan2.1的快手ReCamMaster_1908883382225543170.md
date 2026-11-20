---
key: 平台全量/摄像机变角度wan2.1的快手ReCamMaster_1908883382225543170.json
name: 摄像机变角度wan2.1的快手ReCamMaster_1908883382225543170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/摄像机变角度wan2.1的快手ReCamMaster_1908883382225543170.json
hash: 9aabba2fbf63c8d8
coverage: 0.9
learned_at: 2026-11-14 02:10:14
nodes: [WanVideoSampler, WanVideoExperimentalArgs, ReCamMasterPoseVisualizer, WanVideoTeaCache, WanVideoReCamMasterCameraEmbed, GetImageRangeFromBatch, DownloadAndLoadFlorence2Model, WanVideoTextEncode, WanVideoVAELoader, PreviewImage, LoadWanVideoT5TextEncoder, Florence2Run, VHS_LoadVideo, ImageResizeKJ, PreviewImage, WanVideoModelLoader, WanVideoDecode, VHS_VideoCombine, WanVideoEncode, WanVideoReCamMasterDefaultCamera]
patterns: []
missing: []
---

# 平台全量/摄像机变角度wan2.1的快手ReCamMaster_1908883382225543170.json

> 来源文件 `comfyui_library/workflows/平台全量/摄像机变角度wan2.1的快手ReCamMaster_1908883382225543170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（20 个）：
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `ReCamMasterPoseVisualizer`
- `WanVideoTeaCache`
- `WanVideoReCamMasterCameraEmbed`
- `GetImageRangeFromBatch`
- `DownloadAndLoadFlorence2Model`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `PreviewImage`
- `LoadWanVideoT5TextEncoder`
- `Florence2Run`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `WanVideoReCamMasterDefaultCamera`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`WanVideoSampler`、`WanVideoExperimentalArgs`、`ReCamMasterPoseVisualizer`、`WanVideoTeaCache`、`WanVideoReCamMasterCameraEmbed`、`GetImageRangeFromBatch`、`DownloadAndLoadFlorence2Model`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`Florence2Run`、`VHS_LoadVideo`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoReCamMasterDefaultCamera`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ、DownloadAndLoadFlorence2Model
