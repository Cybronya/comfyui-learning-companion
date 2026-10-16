---
key: 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json
name: FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956045555967381505.json
hash: 6d2c055c8b3cb293
coverage: 0.72973
learned_at: 2026-10-15 22:31:11
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, MarkdownNote, GetNode, GetNode, WanVideoSampler, FantasyPortraitFaceDetector, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoAddFantasyPortrait, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, FantasyPortraitModelLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], LoadImage, Primitive integer [Crystools], WanVideoTextEncodeCached, WanVideoImageToVideoEncode, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956045555967381505.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `MarkdownNote`
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
- `LoadImage`
- `Primitive integer [Crystools]`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoEncode`
- `VHS_LoadVideo`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`FantasyPortraitFaceDetector`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoAddFantasyPortrait`、`WanVideoDecode`、`VHS_VideoCombine`、`FantasyPortraitModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`LoadImage`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoEncode`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
