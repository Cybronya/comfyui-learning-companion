---
key: 视频生成/图生视频/Wan2.2图生视频（优化版）_2067174890066763778.json
name: Wan2.2图生视频（优化版）_2067174890066763778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067174890066763778.json
hash: 4c238cb02cd6fc6d
coverage: 0.914286
learned_at: 2026-10-15 22:39:57
nodes: [WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSetBlockSwap, ImageResizeKJv2, CLIPVisionLoader, easy cleanGpuUsed, GetImageSizeAndCount, WanVideoLoraSelect, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoImageToVideoEncode, ShowText|pysssss, WanVideoTorchCompileSettings, WanVideoTextEncode, AILab_MiniCPM_4_V_Advanced, LoadImage, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频（优化版）_2067174890066763778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067174890066763778.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `ShowText|pysssss`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `AILab_MiniCPM_4_V_Advanced`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `CR Text`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`AILab_MiniCPM_4_V_Advanced`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
