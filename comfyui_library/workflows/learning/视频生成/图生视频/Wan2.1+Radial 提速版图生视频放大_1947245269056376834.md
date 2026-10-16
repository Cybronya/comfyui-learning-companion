---
key: 视频生成/图生视频/Wan2.1+Radial 提速版图生视频放大_1947245269056376834.json
name: Wan2.1+Radial 提速版图生视频放大_1947245269056376834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1947245269056376834.json
hash: 10f51b7b870582f6
coverage: 1
learned_at: 2026-10-15 22:30:45
nodes: [WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoTextEncode, ImageResizeKJv2, SimpleMath+, JWInteger, Primitive integer [Crystools], Primitive integer [Crystools], ImageUpscaleWithModel, UpscaleModelLoader, Primitive integer [Crystools], WanVideoDecode, WanVideoSetRadialAttention, LoadImage, Text Multiline, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, JWInteger, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Radial 提速版图生视频放大_1947245269056376834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1947245269056376834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `SimpleMath+`
- `JWInteger`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `LoadImage`
- `Text Multiline`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoEnhanceAVideo`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`WanVideoTextEncode`、`ImageResizeKJv2`、`SimpleMath+`、`JWInteger`、`Primitive integer [Crystools]`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`WanVideoDecode`、`WanVideoSetRadialAttention`、`LoadImage`、`Text Multiline`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
