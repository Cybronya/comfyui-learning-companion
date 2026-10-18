---
key: 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json
name: 通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json
hash: a399dbec54d8c6f9
coverage: 0.967742
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoSetBlockSwap, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, RIFE VFI, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetImageSizeAndCount, WanVideoDecode, Int, WanVideoBlockSwap, VHS_VideoCombine, Fast Groups Muter (rgthree), WanVideoTextEncode, WanVideoSampler, WanVideoSampler, ImageResizeKJv2, LoadImage, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, INTConstant, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952913426868858882.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSetBlockSwap`
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
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoDecode`、`Int`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSampler`、`ImageResizeKJv2`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`INTConstant`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
