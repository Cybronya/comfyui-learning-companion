---
key: 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大补帧生成2K高清视频_1935685282568003585.json
name: Wan2.1+Lightx2v图生视频放大补帧生成2K高清视频_1935685282568003585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935685282568003585.json
hash: d716563046dda9ba
coverage: 1
learned_at: 2026-10-15 22:30:24
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, Text Multiline, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoSLG, WanVideoTextEncode, JWInteger, JWInteger, ImageResizeKJv2, LoadImage, SimpleMath+, JWInteger, VHS_VideoCombine, UpscaleModelLoader, ImageUpscaleWithModel, WanVideoDecode, WanVideoSampler, WanVideoMagCache, Primitive integer [Crystools], RIFE VFI, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大补帧生成2K高清视频_1935685282568003585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935685282568003585.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `Text Multiline`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `JWInteger`
- `JWInteger`
- `ImageResizeKJv2`
- `LoadImage`
- `SimpleMath+`
- `JWInteger`
- `VHS_VideoCombine`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoMagCache`
- `Primitive integer [Crystools]`
- `RIFE VFI`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`Text Multiline`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoEnhanceAVideo`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`WanVideoTextEncode`、`JWInteger`、`ImageResizeKJv2`、`LoadImage`、`SimpleMath+`、`VHS_VideoCombine`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoMagCache`、`Primitive integer [Crystools]`、`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
