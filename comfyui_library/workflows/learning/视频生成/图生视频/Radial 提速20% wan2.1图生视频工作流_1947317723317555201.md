---
key: 视频生成/图生视频/Radial 提速20% wan2.1图生视频工作流_1947317723317555201.json
name: Radial 提速20% wan2.1图生视频工作流_1947317723317555201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1947317723317555201.json
hash: fad20cfc12fd7844
coverage: 0.947368
learned_at: 2026-10-15 22:30:45
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, LoadImage, WanVideoDecode, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoSetRadialAttention, WanVideoModelLoader, VHS_VideoCombine, WanVideoVAELoader, ImageResizeKJ, CR Upscale Image, VHS_VideoCombine, WanVideoImageToVideoEncode, PreviewImage, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Radial 提速20% wan2.1图生视频工作流_1947317723317555201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947317723317555201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（19 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `LoadImage`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetRadialAttention`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `ImageResizeKJ`
- `CR Upscale Image`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`LoadImage`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoSetRadialAttention`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoVAELoader`、`ImageResizeKJ`、`CR Upscale Image`、`WanVideoImageToVideoEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
