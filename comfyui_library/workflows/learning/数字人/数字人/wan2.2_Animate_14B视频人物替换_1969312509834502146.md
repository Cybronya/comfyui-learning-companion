---
key: 数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json
name: wan2.2_Animate_14B视频人物替换_1969312509834502146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json
hash: 621b68f325a0ca83
coverage: 0.549296
learned_at: 2026-10-26 01:59:26
nodes: [ImageConcatMulti, GetNode, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Reroute, SetNode, ImageCropByMaskAndResize, SetNode, SetNode, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, INTConstant, INTConstant, DrawMaskOnImage, VHS_VideoCombine, GrowMask, BlockifyMask, Note, CLIPTextEncode, CLIPLoader, WanVideoTextEmbedBridge, WanVideoTextEncodeCached, CLIPVisionLoader, MarkdownNote, SetNode, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, PrimitiveNode, Note, WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, VHS_LoadVideo, SetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, WanVideoSampler, easy cleanGpuUsed, WanVideoBlockSwap, SetNode, InspyrenetRembgAdvanced, GetNode, SetNode, PreviewAnimation, LoadImage, ImageResizeKJv2, CLIPTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2_Animate_14B视频人物替换_1969312509834502146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（71 个）：
- `ImageConcatMulti`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `GrowMask`
- `BlockifyMask`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `WanVideoTextEmbedBridge`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `PrimitiveNode`
- `Note`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `SetNode`
- `InspyrenetRembgAdvanced`
- `GetNode`
- `SetNode`
- `PreviewAnimation`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **55%**（39/71）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`CLIPTextEncode`、`CLIPLoader`、`WanVideoTextEmbedBridge`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoBlockSwap`、`InspyrenetRembgAdvanced`、`PreviewAnimation`、`LoadImage`、`ImageResizeKJv2`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
