---
key: 视频生成/图生视频/Wan2.2首尾帧KJ版_1963509971877072897.json
name: Wan2.2首尾帧KJ版_1963509971877072897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963509971877072897.json
hash: 62183dc94a008877
coverage: 0.923077
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoSampler, WanVideoClipVisionEncode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, CR Text, PrimitiveInt, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧KJ版_1963509971877072897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963509971877072897.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CR Text`
- `PrimitiveInt`
- `SimpleMath+`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`CR Text`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
