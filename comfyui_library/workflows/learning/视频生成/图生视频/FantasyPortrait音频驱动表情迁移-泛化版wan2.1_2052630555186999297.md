---
key: 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json
name: FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052630555186999297.json
hash: d370c0b5992c38db
coverage: 0.75
learned_at: 2026-10-15 22:37:30
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, GetNode, GetNode, WanVideoSampler, FantasyPortraitFaceDetector, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoAddFantasyPortrait, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, FantasyPortraitModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoTextEncodeCached, WanVideoImageToVideoEncode, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052630555186999297.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `FantasyPortraitFaceDetector`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoAddFantasyPortrait`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FantasyPortraitModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoEncode`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`FantasyPortraitFaceDetector`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoAddFantasyPortrait`、`WanVideoDecode`、`VHS_VideoCombine`、`FantasyPortraitModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoEncode`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
