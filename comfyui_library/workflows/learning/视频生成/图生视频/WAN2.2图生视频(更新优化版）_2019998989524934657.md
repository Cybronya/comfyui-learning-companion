---
key: 视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json
name: WAN2.2图生视频(更新优化版）_2019998989524934657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json
hash: 2fa40d163f8e6bb4
coverage: 0.914286
learned_at: 2026-10-15 22:35:05
nodes: [WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSetBlockSwap, ImageResizeKJv2, CLIPVisionLoader, easy cleanGpuUsed, GetImageSizeAndCount, WanVideoLoraSelect, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler, WanVideoSampler, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, WanVideoImageToVideoEncode, ShowText|pysssss, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoTextEncode, LoadImage, AILab_QwenVL, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2019998989524934657.json`

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
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `ShowText|pysssss`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `LoadImage`
- `AILab_QwenVL`
- `CR Text`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`ImageResizeKJv2`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`LoadImage`、`AILab_QwenVL`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
