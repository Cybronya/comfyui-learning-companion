---
key: 视频生成/图生视频/Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json
name: Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json
hash: 02cb64ad1038ec0c
coverage: 0.807692
learned_at: 2026-10-15 22:31:12
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, MarkdownNote, GetNode, FantasyPortraitFaceDetector, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadImage, WanVideoVAELoader, WanVideoAddFantasyPortrait, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoImageToVideoEncode, GetNode, WanVideoTextEncodeCached, StringToFloatList, FloatToSigmas, CR Prompt Text, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, ImageConcatMulti, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch+, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, FantasyPortraitModelLoader, VHS_VideoCombine, VHS_VideoCombine, JWInteger, JWInteger, INTConstant, JWInteger, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
patterns: []
missing: []
---

# 视频生成/图生视频/Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956253904029798402.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
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
- `FantasyPortraitFaceDetector`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoAddFantasyPortrait`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `StringToFloatList`
- `FloatToSigmas`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `ImageConcatMulti`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `FantasyPortraitModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `INTConstant`
- `JWInteger`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`FantasyPortraitFaceDetector`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoVAELoader`、`WanVideoAddFantasyPortrait`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeCached`、`StringToFloatList`、`FloatToSigmas`、`CR Prompt Text`、`WanVideoSampler`、`WanVideoModelLoader`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageFromBatch+`、`FantasyPortraitModelLoader`、`JWInteger`、`INTConstant`、`VHS_LoadVideo`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
