---
key: 平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json
name: Wan Animate2.2替换主体和背景_1971588251523936257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json
hash: a6fb9bc728c0fbbf
coverage: 0.5
learned_at: 2026-11-14 01:04:05
nodes: [SetNode, SetNode, SetNode, JWInteger, SetNode, JWInteger, SetNode, JWInteger, GetNode, GetNode, GetNode, GetNode, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, SetNode, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, WanVideoAnimateEmbeds, PreviewImage, SetNode, ImageResizeKJv2, Manual XY Entry Info, VHS_LoadVideo, PreviewImage, ImageFromBatch+, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, PreviewImage, LoadImage, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, CR Prompt Text, ImageConcatMulti, VHS_LoadVideo, DWPreprocessor, ImageCropByMaskAndResize, VHS_VideoCombine, VHS_VideoCombine, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `SetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `Manual XY Entry Info`
- `VHS_LoadVideo`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Prompt Text`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **50%**（39/78）

**有卡**：`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`Manual XY Entry Info`、`VHS_LoadVideo`、`ImageFromBatch+`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageConcatMulti`、`LoadImage`、`WanVideoSampler`、`CR Prompt Text`、`DWPreprocessor`、`ImageCropByMaskAndResize`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
