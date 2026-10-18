---
key: 视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json
name: Wan2.2图生视频（最新优化版）_1987880762861137921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json
hash: b251ad6a5341435c
coverage: 0.888889
learned_at: 2026-10-15 22:33:00
nodes: [easy cleanGpuUsed, WanVideoVAELoader, easy cleanGpuUsed, GetImageSizeAndCount, VHS_VideoCombine, WanVideoLoraSelect, WanVideoImageToVideoEncode, easy cleanGpuUsed, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoClipVisionEncode, ImageResizeKJv2, SimpleMath+, CM_IntToFloat, easy cleanGpuUsed, LoadImage, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, easy cleanGpuUsed, easy cleanGpuUsed, ShowText|pysssss, VHS_VideoCombine, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoBlockSwap, WanVideoModelLoader, AILab_MiniCPM_4_V_Advanced, easy int, easy int, CR Text, PrimitiveInt, PrimitiveInt, WanVideoModelLoader, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987880762861137921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `CM_IntToFloat`
- `easy cleanGpuUsed`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `AILab_MiniCPM_4_V_Advanced`
- `easy int`
- `easy int`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoModelLoader`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`easy cleanGpuUsed`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`SimpleMath+`、`CM_IntToFloat`、`LoadImage`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`AILab_MiniCPM_4_V_Advanced`、`easy int`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
