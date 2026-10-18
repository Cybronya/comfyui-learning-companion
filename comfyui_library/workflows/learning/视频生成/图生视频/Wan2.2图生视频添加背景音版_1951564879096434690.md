---
key: 视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json
name: Wan2.2图生视频添加背景音版_1951564879096434690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json
hash: d5b1acdc08bde8de
coverage: 1
learned_at: 2026-10-15 22:30:58
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, LoadImage, LoadImage, WanVideoModelLoader, ImageResizeKJv2, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, MMAudioFeatureUtilsLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, easy cleanGpuUsed, CR Text, MMAudioSampler, WanVideoImageToVideoEncode, CLIPVisionLoader, WanVideoClipVisionEncode, MMAudioModelLoader, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951564879096434690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `MMAudioFeatureUtilsLoader`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `CR Text`
- `MMAudioSampler` ★核心
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `MMAudioModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`LoadImage`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`MMAudioFeatureUtilsLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CR Text`、`MMAudioSampler`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`MMAudioModelLoader`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
