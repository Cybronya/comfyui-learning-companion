---
key: 视频生成/图生视频/wan2.x Palingenesis 图生视频_1975470690600136706.json
name: wan2.x Palingenesis 图生视频_1975470690600136706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975470690600136706.json
hash: 1a4391a684ddcc32
coverage: 0.904762
learned_at: 2026-10-15 22:32:08
nodes: [WanVideoLoraSelectMulti, INTConstant, CreateCFGScheduleFloatList, SetNode, INTConstant, WanVideoBlockSwap, WanVideoTorchCompileSettings, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy sleep, WanVideoDecode, easy cleanGpuUsed, GetImageSizeAndCount, DownloadAndLoadGIMMVFIModel, easy cleanGpuUsed, easy sleep, INTConstant, INTConstant, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetNode, WanVideoImageToVideoEncode, ShowText, RH_LLMAPI_NODE, WanVideoLoraSelectMulti, WanVideoTextEncode, INTConstant, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, GIMMVFI_interpolate, ImageResizeKJv2, SetNode, ImageConcanate, GetNode, VHS_VideoCombine, easy sleep, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.x Palingenesis 图生视频_1975470690600136706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975470690600136706.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `SetNode`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy sleep`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `DownloadAndLoadGIMMVFIModel`
- `easy cleanGpuUsed`
- `easy sleep`
- `INTConstant`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `ShowText`
- `RH_LLMAPI_NODE`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncode`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `SetNode`
- `ImageConcanate`
- `GetNode`
- `VHS_VideoCombine`
- `easy sleep`
- `LoadImage`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`WanVideoLoraSelectMulti`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`easy sleep`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`ShowText`、`RH_LLMAPI_NODE`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoSampler`、`GIMMVFI_interpolate`、`ImageResizeKJv2`、`ImageConcanate`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
