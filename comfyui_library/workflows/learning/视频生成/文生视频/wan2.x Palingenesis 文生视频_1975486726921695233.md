---
key: 视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json
name: wan2.x Palingenesis 文生视频_1975486726921695233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json
hash: ccf6459fa78f4aae
coverage: 0.974359
learned_at: 2026-10-15 22:47:37
nodes: [SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy sleep, WanVideoDecode, easy cleanGpuUsed, GetImageSizeAndCount, DownloadAndLoadGIMMVFIModel, LoadWanVideoT5TextEncoder, GIMMVFI_interpolate, easy sleep, ShowText, INTConstant, INTConstant, INTConstant, WanVideoEmptyEmbeds, WanVideoTextEncode, easy sleep, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, easy cleanGpuUsed, RH_LLMAPI_NODE, WanVideoVAELoader, WanVideoModelLoader, INTConstant, WanVideoSigmaToStep, FloatConstant, WanVideoLoraSelectMulti, VHS_VideoCombine, WanVideoModelLoader, WanVideoScheduler, WanVideoLoraSelectMulti, WanVideoScheduler, CreateCFGScheduleFloatList, Primitive string multiline [Crystools]]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy sleep`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `DownloadAndLoadGIMMVFIModel`
- `LoadWanVideoT5TextEncoder`
- `GIMMVFI_interpolate`
- `easy sleep`
- `ShowText`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `easy sleep`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `INTConstant`
- `WanVideoSigmaToStep`
- `FloatConstant`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoScheduler`
- `WanVideoLoraSelectMulti`
- `WanVideoScheduler`
- `CreateCFGScheduleFloatList`
- `Primitive string multiline [Crystools]`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`easy sleep`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoT5TextEncoder`、`GIMMVFI_interpolate`、`ShowText`、`INTConstant`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`WanVideoSampler`、`RH_LLMAPI_NODE`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSigmaToStep`、`FloatConstant`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`Primitive string multiline [Crystools]`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount
