---
key: 视频生成/图生视频/Wan2.2运镜控制(KJ)_1957349808384176130.json
name: Wan2.2运镜控制(KJ)_1957349808384176130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2运镜控制(KJ)_1957349808384176130.json
hash: 7baa47a73485d766
coverage: 0.909091
learned_at: 2026-10-15 22:31:16
nodes: [easy cleanGpuUsed, WanVideoLoraSelect, easy cleanGpuUsed, WanVideoSetLoRAs, ImageResizeKJv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoTextEncode, WanVideoApplyNAG, WanVideoSampler, WanVideoSampler, WanVideoDecode, LoadImage, Note, WanVideoLoraSelect, WanVideoImageToVideoEncode, CR SDXL Aspect Ratio, WanVideoModelLoader, WanVideoModelLoader, CR Text, WanVideoFunCameraEmbeds, ADE_CameraPoseBasic, PrimitiveInt, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2运镜控制(KJ)_1957349808384176130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957349808384176130.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `easy cleanGpuUsed`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncode`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `LoadImage`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `CR SDXL Aspect Ratio`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CR Text`
- `WanVideoFunCameraEmbeds`
- `ADE_CameraPoseBasic`
- `PrimitiveInt`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`easy cleanGpuUsed`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoTextEncode`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`LoadImage`、`WanVideoImageToVideoEncode`、`CR SDXL Aspect Ratio`、`WanVideoModelLoader`、`CR Text`、`WanVideoFunCameraEmbeds`、`ADE_CameraPoseBasic`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
