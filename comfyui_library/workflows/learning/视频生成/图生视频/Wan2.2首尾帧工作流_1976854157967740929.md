---
key: 视频生成/图生视频/Wan2.2首尾帧工作流_1976854157967740929.json
name: Wan2.2首尾帧工作流_1976854157967740929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧工作流_1976854157967740929.json
hash: 9227b1a3c4bab7b0
coverage: 0.933333
learned_at: 2026-10-15 22:32:12
nodes: [WanVideoVAELoader, easy cleanGpuUsed, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, PrimitiveInt, PrimitiveInt, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, GetImageSizeAndCount, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, WanVideoSetLoRAs, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoLoraSelect, WanVideoSampler, LoadImage, LoadImage, CR Text, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧工作流_1976854157967740929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976854157967740929.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`WanVideoVAELoader`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoSampler`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
