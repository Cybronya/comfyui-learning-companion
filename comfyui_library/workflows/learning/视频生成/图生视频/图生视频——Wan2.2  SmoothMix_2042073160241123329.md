---
key: 视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2042073160241123329.json
name: 图生视频——Wan2.2  SmoothMix_2042073160241123329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042073160241123329.json
hash: 1f37ba80855d4abf
coverage: 1
learned_at: 2026-10-15 22:36:24
nodes: [CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoSetRadialAttention, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoSetRadialAttention, WanVideoDecode, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncodeCached, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2042073160241123329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042073160241123329.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（19 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetRadialAttention`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `WanVideoSetRadialAttention`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `LoadImage`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoSetRadialAttention`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、GetImageSizeAndCount
