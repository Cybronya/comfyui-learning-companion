---
key: 视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json
name: Wan2.2 图生视频一键工作流_2032825101573431298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032825101573431298.json
hash: dae617f17377e72e
coverage: 1
learned_at: 2026-10-15 22:35:37
nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoImageToVideoEncode, INTConstant, INTConstant, VHS_VideoCombine, INTConstant, LoadImage, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032825101573431298.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `INTConstant`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`CreateCFGScheduleFloatList`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`INTConstant`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
