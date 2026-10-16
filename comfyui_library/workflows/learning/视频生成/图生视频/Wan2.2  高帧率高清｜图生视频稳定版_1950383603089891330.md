---
key: 视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json
name: Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950383603089891330.json
hash: 07060c0c296a710c
coverage: 1
learned_at: 2026-10-15 22:30:54
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, WanVideoSetLoRAs, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, INTConstant, WanVideoImageToVideoEncode, LoadImage, VHS_VideoCombine, ImageResizeKJv2, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950383603089891330.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（24 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`INTConstant`、`WanVideoImageToVideoEncode`、`LoadImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
