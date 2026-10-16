---
key: 视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json
name: CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952283809247080449.json
hash: 688245c0521d2d3e
coverage: 0.964286
learned_at: 2026-10-15 22:31:00
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoSampler, INTConstant, INTConstant, MarkdownNote, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, WanVideoTextEncode, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952283809247080449.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
