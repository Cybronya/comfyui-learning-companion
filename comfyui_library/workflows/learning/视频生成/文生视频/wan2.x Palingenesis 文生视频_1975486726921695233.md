---
key: 视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json
name: wan2.x Palingenesis 文生视频_1975486726921695233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.x Palingenesis 文生视频_1975486726921695233.json
hash: ccf6459fa78f4aae
coverage: 0.717949
learned_at: 2026-10-10 23:09:51
nodes: [SetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy sleep, WanVideoDecode, easy cleanGpuUsed, GetImageSizeAndCount, DownloadAndLoadGIMMVFIModel, LoadWanVideoT5TextEncoder, GIMMVFI_interpolate, easy sleep, ShowText, INTConstant, INTConstant, INTConstant, WanVideoEmptyEmbeds, WanVideoTextEncode, easy sleep, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, easy cleanGpuUsed, RH_LLMAPI_NODE, WanVideoVAELoader, WanVideoModelLoader, INTConstant, WanVideoSigmaToStep, FloatConstant, WanVideoLoraSelectMulti, VHS_VideoCombine, WanVideoModelLoader, WanVideoScheduler, WanVideoLoraSelectMulti, WanVideoScheduler, CreateCFGScheduleFloatList, Primitive string multiline [Crystools]]
patterns: []
missing: [Primitive string multiline [Crystools], easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy sleep, easy sleep, easy sleep]
discoveries: [次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识, 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识, 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识]
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

覆盖率 **72%**（28/39）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoT5TextEncoder`、`GIMMVFI_interpolate`、`ShowText`、`INTConstant`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`WanVideoSampler`、`RH_LLMAPI_NODE`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSigmaToStep`、`FloatConstant`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`

**缺卡**（10）：`Primitive string multiline [Crystools]`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy sleep`、`easy sleep`、`easy sleep`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、GetImageSizeAndCount

## 学习发现

- 次要节点 `Primitive string multiline [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识
- 次要节点 `easy sleep` 知识库中没有该节点类型的任何知识
