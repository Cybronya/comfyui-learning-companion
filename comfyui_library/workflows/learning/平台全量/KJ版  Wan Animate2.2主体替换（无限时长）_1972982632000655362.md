---
key: 平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json
name: KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json
hash: 66c5e60cb446ab45
coverage: 0.546875
learned_at: 2026-11-14 00:33:15
nodes: [GetNode, GetNode, MarkdownNote, Sam2Segmentation, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, WanVideoDecode, CR Prompt Text, ImageResizeKJv2, SetNode, SetNode, GrowMask, BlockifyMask, SetNode, GetNode, DownloadAndLoadSAM2Model, SetNode, Note, DrawMaskOnImage, PixelPerfectResolution, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, Note, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetImageSizeAndCount, VHS_VideoCombine, DWPreprocessor, Note, Note, SetNode, SetNode, WanVideoBlockSwap, JWInteger, JWInteger, SetNode, SetNode, GetNode, LoadImage, VHS_LoadVideo, JWInteger, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSampler, VHS_VideoCombine, PointsEditor, Note]
patterns: []
missing: []
---

# 平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json

> 来源文件 `comfyui_library/workflows/平台全量/KJ版  Wan Animate2.2主体替换（无限时长）_1972982632000655362.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `Sam2Segmentation`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `Note`
- `DrawMaskOnImage`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Note`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `JWInteger`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `PointsEditor`
- `Note`

## 知识

覆盖率 **55%**（35/64）

**有卡**：`Sam2Segmentation`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoDecode`、`CR Prompt Text`、`ImageResizeKJv2`、`GrowMask`、`BlockifyMask`、`DownloadAndLoadSAM2Model`、`DrawMaskOnImage`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`DWPreprocessor`、`WanVideoBlockSwap`、`JWInteger`、`LoadImage`、`VHS_LoadVideo`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSampler`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
