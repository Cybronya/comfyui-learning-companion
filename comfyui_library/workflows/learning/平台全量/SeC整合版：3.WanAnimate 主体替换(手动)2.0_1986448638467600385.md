---
key: 平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json
name: SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json
hash: a873d7a1c3cae100
coverage: 0.557143
learned_at: 2026-11-14 00:58:15
nodes: [INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPLoader, DrawMaskOnImage, WanVideoTextEmbedBridge, CLIPVisionLoader, WanVideoVAELoader, SetNode, GetNode, Note, Note, Note, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, DownloadAndLoadSAM2Model, WanVideoDecode, GetImageSizeAndCount, WanVideoAnimateEmbeds, Reroute, PixelPerfectResolution, GetNode, VHS_VideoCombine, Sam2Segmentation, GrowMask, SetNode, SetNode, BlockifyMask, SetNode, WanVideoLoraSelectMulti, DWPreprocessor, WanVideoBlockSwap, FaceMaskFromPoseKeypoints, WanVideoClipVisionEncode, WanVideoSetBlockSwap, GetNode, GetNode, GetNode, WanVideoSetLoRAs, GetNode, GetNode, GetNode, GetNode, GetNode, ImageCropByMaskAndResize, ImageConcatMulti, SetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, VHS_LoadVideo, LoadImage, WanVideoModelLoader, PointsEditor]
patterns: []
missing: []
---

# 平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json

> 来源文件 `comfyui_library/workflows/平台全量/SeC整合版：3.WanAnimate 主体替换(手动)2.0_1986448638467600385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（70 个）：
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPLoader`
- `DrawMaskOnImage`
- `WanVideoTextEmbedBridge`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `Reroute`
- `PixelPerfectResolution`
- `GetNode`
- `VHS_VideoCombine`
- `Sam2Segmentation`
- `GrowMask`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `DWPreprocessor`
- `WanVideoBlockSwap`
- `FaceMaskFromPoseKeypoints`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageConcatMulti`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `PointsEditor`

## 知识

覆盖率 **56%**（39/70）

**有卡**：`INTConstant`、`CLIPTextEncode`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPLoader`、`DrawMaskOnImage`、`WanVideoTextEmbedBridge`、`CLIPVisionLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`DownloadAndLoadSAM2Model`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`PixelPerfectResolution`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`WanVideoLoraSelectMulti`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageCropByMaskAndResize`、`ImageConcatMulti`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`PointsEditor`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoVAELoader、WanVideoLoraSelectMulti
