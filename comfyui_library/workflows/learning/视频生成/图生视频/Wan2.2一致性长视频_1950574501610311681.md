---
key: 视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json
name: Wan2.2一致性长视频_1950574501610311681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json
hash: c7234da0c7f02367
coverage: 0.933333
learned_at: 2026-10-15 22:30:55
nodes: [CLIPTextEncode, CLIPLoader, Note, CLIPTextEncode, WanVideoTextEmbedBridge, Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoDecode, INTConstant, WanVideoSetLoRAs, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, INTConstant, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, VHS_VideoCombine, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, LoadImage, ImageResizeKJv2, WanVideoTextEncode, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950574501610311681.json`

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
- `VHS_VideoCombine`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoDecode`、`INTConstant`、`GetImageSizeAndCount`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJv2`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
