---
key: 视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json
name: Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json
hash: ca2b7954a7f825c5
coverage: 1
learned_at: 2026-10-15 22:31:27
nodes: [WanVideoSetBlockSwap, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, ImageResizeKJv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoDecode, SimpleMath+, SimpleMath+, WanVideoImageToVideoEncode, INTConstant, INTConstant, INTConstant, INTConstant, WanVideoSampler, GetImageSizeAndCount, WanVideoVAELoader, easy seed, VHS_VideoCombine, LoadImage, INTConstant, WanVideoTextEncode, easy positive, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频 KJ加速版（小优化）_1960986667224109058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960986667224109058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `easy seed`
- `VHS_VideoCombine`
- `LoadImage`
- `INTConstant`
- `WanVideoTextEncode`
- `easy positive`
- `LoadImage`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`easy seed`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`、`easy positive`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
