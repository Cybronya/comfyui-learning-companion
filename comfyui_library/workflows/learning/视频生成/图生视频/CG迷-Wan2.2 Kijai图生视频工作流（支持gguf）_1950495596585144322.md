---
key: 视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json
name: CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950495596585144322.json
hash: 522fd9d651271098
coverage: 0.961538
learned_at: 2026-10-15 22:30:55
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, WanVideoSampler, INTConstant, INTConstant, MarkdownNote, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, INTConstant, WanVideoImageToVideoEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950495596585144322.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
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
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
