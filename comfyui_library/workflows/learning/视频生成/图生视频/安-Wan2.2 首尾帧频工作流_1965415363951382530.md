---
key: 视频生成/图生视频/安-Wan2.2 首尾帧频工作流_1965415363951382530.json
name: 安-Wan2.2 首尾帧频工作流_1965415363951382530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965415363951382530.json
hash: e3f32e2b287cb80b
coverage: 1
learned_at: 2026-10-15 22:31:37
nodes: [WanVideoDecode, GetImageSizeAndCount, INTConstant, LoadImage, LoadImage, LoadWanVideoT5TextEncoder, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, WanVideoSetLoRAs, CreateCFGScheduleFloatList, INTConstant, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSampler, INTConstant, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, INTConstant, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/安-Wan2.2 首尾帧频工作流_1965415363951382530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965415363951382530.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `INTConstant`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`INTConstant`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
