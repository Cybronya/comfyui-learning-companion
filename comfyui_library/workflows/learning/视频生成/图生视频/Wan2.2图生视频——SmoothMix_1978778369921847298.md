---
key: 视频生成/图生视频/Wan2.2图生视频——SmoothMix_1978778369921847298.json
name: Wan2.2图生视频——SmoothMix_1978778369921847298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频——SmoothMix_1978778369921847298.json
hash: 0b2461971c976afd
coverage: 1
learned_at: 2026-10-15 22:32:20
nodes: [CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoSetRadialAttention, INTConstant, INTConstant, WanVideoBlockSwap, WanVideoSetRadialAttention, WanVideoDecode, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频——SmoothMix_1978778369921847298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978778369921847298.json`

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
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoSetRadialAttention`、`INTConstant`、`WanVideoBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、GetImageSizeAndCount
