---
key: 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大_1938448782306508802.json
name: Wan2.1+Lightx2v图生视频放大_1938448782306508802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1+Lightx2v图生视频放大_1938448782306508802.json
hash: 05a19a2f3f83656d
coverage: 1
learned_at: 2026-10-15 22:30:31
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoTextEncode, JWInteger, JWInteger, ImageResizeKJv2, SimpleMath+, JWInteger, WanVideoSampler, Primitive integer [Crystools], LoadImage, Text Multiline, Primitive integer [Crystools], ImageUpscaleWithModel, UpscaleModelLoader, Primitive integer [Crystools], VHS_VideoCombine, RIFE VFI, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大_1938448782306508802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1938448782306508802.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `JWInteger`
- `JWInteger`
- `ImageResizeKJv2`
- `SimpleMath+`
- `JWInteger`
- `WanVideoSampler` ★核心
- `Primitive integer [Crystools]`
- `LoadImage`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `RIFE VFI`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoEnhanceAVideo`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`WanVideoTextEncode`、`JWInteger`、`ImageResizeKJv2`、`SimpleMath+`、`WanVideoSampler`、`Primitive integer [Crystools]`、`LoadImage`、`Text Multiline`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VHS_VideoCombine`、`RIFE VFI`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
