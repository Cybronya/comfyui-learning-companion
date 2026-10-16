---
key: 视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json
name: Wan2.2-KJ版本图生视频_1952541764970328066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952541764970328066.json
hash: 6173f49056f19a52
coverage: 1
learned_at: 2026-10-15 22:31:02
nodes: [WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, SimpleMath+, WanVideoTextEncode, ImageResizeKJv2, Int, Int, Int, Seed, LoadImage, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetRadialAttention, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoImageToVideoEncode, INTConstant, INTConstant, GetImageSizeAndCount, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-KJ版本图生视频_1952541764970328066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952541764970328066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `Int`
- `Seed`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetRadialAttention`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoDecode`、`SimpleMath+`、`WanVideoTextEncode`、`ImageResizeKJv2`、`Int`、`Seed`、`LoadImage`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`INTConstant`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed、Seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
