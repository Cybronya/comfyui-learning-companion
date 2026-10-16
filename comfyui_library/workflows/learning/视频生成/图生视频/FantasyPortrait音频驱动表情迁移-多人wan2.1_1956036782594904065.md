---
key: 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json
name: FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956036782594904065.json
hash: 2870be2d1774fca1
coverage: 0.72973
learned_at: 2026-10-15 22:31:11
nodes: [SetNode, SetNode, SetNode, SetNode, WanVideoImageToVideoEncode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, MarkdownNote, GetNode, GetNode, INTConstant, WanVideoSampler, FantasyPortraitFaceDetector, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoAddFantasyPortrait, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, FantasyPortraitModelLoader, WanVideoVAELoader, WanVideoLoraSelect, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoTextEncodeCached, Primitive integer [Crystools], Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956036782594904065.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `INTConstant`
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
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`INTConstant`、`WanVideoSampler`、`FantasyPortraitFaceDetector`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoAddFantasyPortrait`、`WanVideoDecode`、`VHS_VideoCombine`、`FantasyPortraitModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`Primitive integer [Crystools]`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
