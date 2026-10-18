---
key: 视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json
name: Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json
hash: befac912399d263a
coverage: 0.933333
learned_at: 2026-10-15 22:30:54
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, INTConstant, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, INTConstant, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, LoadImage, ImageResizeKJv2, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950204585861365762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `INTConstant`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
