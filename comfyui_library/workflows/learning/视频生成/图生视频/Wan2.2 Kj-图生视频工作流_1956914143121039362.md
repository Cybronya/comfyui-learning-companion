---
key: 视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json
name: Wan2.2 Kj-图生视频工作流_1956914143121039362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956914143121039362.json
hash: 5bcfe633b3cbbea7
coverage: 1
learned_at: 2026-10-15 22:31:15
nodes: [LayerUtility: ImageScaleByAspectRatio V2, INTConstant, WanVideoDecode, WanVideoModelLoader, INTConstant, LoadImage, WanVideoLoraSelect, WanVideoModelLoader, INTConstant, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoTextEncode, INTConstant, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetBlockSwap, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956914143121039362.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `INTConstant`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `INTConstant`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`WanVideoDecode`、`WanVideoModelLoader`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
