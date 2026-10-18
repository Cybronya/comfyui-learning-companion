---
key: 视频生成/图生视频/AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json
name: AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json
hash: 00992b5925e836f1
coverage: 0.882353
learned_at: 2026-10-15 22:31:12
nodes: [WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, MarkdownNote, FantasyPortraitFaceDetector, ImageConcatMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageConcatMulti, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoLoraSelect, FantasyPortraitModelLoader, WanVideoAddFantasyPortrait, VHS_LoadVideo, WanVideoDecode, INTConstant, INTConstant, ImageResizeKJv2, INTConstant, WanVideoSampler, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, LoadImage, JWInteger, JWInteger, JWInteger, SetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956272186195673089.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `FantasyPortraitFaceDetector`
- `ImageConcatMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `FantasyPortraitModelLoader`
- `WanVideoAddFantasyPortrait`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`FantasyPortraitFaceDetector`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`FantasyPortraitModelLoader`、`WanVideoAddFantasyPortrait`、`VHS_LoadVideo`、`WanVideoDecode`、`INTConstant`、`ImageResizeKJv2`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`JWInteger`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
