---
key: 视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json
name: WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949391348926971905.json
hash: 87ae79bd0437fa7f
coverage: 0.92
learned_at: 2026-10-15 22:30:49
nodes: [WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoModelLoader, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSampler, GetImageSizeAndCount, WanVideoDecode, LoadImage, WanVideoImageToVideoEncode, ImageResizeKJv2, WanVideoTextEncode, WanVideoSampler, Note, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949391348926971905.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`LoadImage`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
