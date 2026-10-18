---
key: 视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json
name: Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json
hash: b736b84611656c98
coverage: 0.474576
learned_at: 2026-10-15 22:32:04
nodes: [WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, SetNode, SetNode, GetNode, GetNode, PixelPerfectResolution, GetNode, DWPreprocessor, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, SetNode, SetNode, Anything Everywhere, VHS_VideoInfo, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, ImageResizeKJv2, GetNode, ImageConcatMulti, GetNode, GetNode, ImageConcatMulti, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, Text, WanVideoTextEncodeCached, Note, GetNode, GetNode, ImageResizeKJv2, SetNode, VHS_LoadVideo, JWInteger, JWInteger, Note, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Best_Wan2.2_图片跳舞指定动作_1973849425091104769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973849425091104769.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `GetNode`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `VHS_VideoInfo`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageResizeKJv2`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Text`
- `WanVideoTextEncodeCached`
- `Note`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `Note`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **47%**（28/59）

**有卡**：`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`VHS_VideoInfo`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageResizeKJv2`、`ImageConcatMulti`、`VHS_VideoCombine`、`Text`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
