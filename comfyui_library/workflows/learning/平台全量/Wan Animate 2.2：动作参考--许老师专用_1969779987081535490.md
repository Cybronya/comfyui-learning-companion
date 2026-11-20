---
key: 平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json
name: Wan Animate 2.2：动作参考--许老师专用_1969779987081535490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json
hash: c36babc6706561e4
coverage: 0.409091
learned_at: 2026-11-14 01:03:52
nodes: [PixelPerfectResolution, GetNode, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, SetNode, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, SetNode, SetNode, SetNode, SetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, GetNode, GetNode, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoDecode, GetNode, SetNode, GetNode, GetNode, GetNode, RHHiddenNodes, SetNode, ImageConcatMulti, GetImageSizeAndCount, GetNode, JWInteger, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, WanVideoSampler, VHS_LoadVideo, JWInteger, GetNode, GetNode, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, SetNode, Text]
patterns: []
missing: []
---

# 平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `PixelPerfectResolution`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `SetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `GetNode`
- `JWInteger`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `JWInteger`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `Text`

## 知识

覆盖率 **41%**（27/66）

**有卡**：`PixelPerfectResolution`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`RHHiddenNodes`、`ImageConcatMulti`、`GetImageSizeAndCount`、`JWInteger`、`ImageResizeKJv2`、`WanVideoModelLoader`、`LoadImage`、`WanVideoSampler`、`VHS_LoadVideo`、`DWPreprocessor`、`VHS_VideoCombine`、`Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
