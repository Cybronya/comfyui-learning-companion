---
key: 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json
name: 通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952709897437777921.json
hash: 6bee3a1ef578f8a2
coverage: 0.966667
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, RIFE VFI, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetImageSizeAndCount, WanVideoDecode, Int, WanVideoBlockSwap, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoTextEncode, WanVideoSampler, WanVideoSampler, ImageResizeKJv2, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952709897437777921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `Int`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoDecode`、`Int`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSampler`、`ImageResizeKJv2`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
