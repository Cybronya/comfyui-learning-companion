---
key: 视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json
name: HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json
hash: 85c61be5ea92c120
coverage: 0.96
learned_at: 2026-10-15 22:31:45
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, WanVideoSampler, INTConstant, WanVideoSetBlockSwap, WanVideoSetBlockSwap, INTConstant, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, LoadImage, WanVideoVAELoader, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/HeGenAI-N8N-Wan2.2图生视频加速版_1968577373975261186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968577373975261186.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoVAELoader`
- `MarkdownNote`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadImage`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
