---
key: 平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json
name: 手动遮罩视频换装_WanAnimate2.2_1984074108189245442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json
hash: c83111c6694bba5a
coverage: 0.363636
learned_at: 2026-11-14 02:04:48
nodes: [MarkdownNote, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, SetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoLoraSelectMulti, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, VHS_VideoInfo, SetNode, GetNode, GetNode, SetNode, GetImageRangeFromBatch, SetNode, GetNode, GetNode, SeCModelLoader, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, DrawMaskOnImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, InvertMask, SetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, SetNode, JWInteger, Note, Note, JWInteger, GetNode, ImageConcatMulti, GetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, GrowMask, GetNode, BlockifyMask, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, GetNode, GetNode, SetNode, PixelPerfectResolution, GetNode, Reroute, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, VHS_VideoCombine, Int, WanVideoSampler, GetNode, Note, CR Prompt Text, SeCVideoSegmentation, PointsEditor, Int, Fast Groups Bypasser (rgthree), Note, VHS_VideoCombine, LoadImage, VHS_LoadVideo, VHS_LoadVideo, WanVideoDecode, GetNode, GetNode, GetImageRangeFromBatch, SetNode]
patterns: []
missing: []
---

# 平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json

> 来源文件 `comfyui_library/workflows/平台全量/手动遮罩视频换装_WanAnimate2.2_1984074108189245442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（121 个）：
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `InvertMask`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `JWInteger`
- `Note`
- `Note`
- `JWInteger`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GrowMask`
- `GetNode`
- `BlockifyMask`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PixelPerfectResolution`
- `GetNode`
- `Reroute`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `VHS_VideoCombine`
- `Int`
- `WanVideoSampler` ★核心
- `GetNode`
- `Note`
- `CR Prompt Text`
- `SeCVideoSegmentation`
- `PointsEditor`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`

## 知识

覆盖率 **36%**（44/121）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`SeCModelLoader`、`DrawMaskOnImage`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`InvertMask`、`VHS_VideoCombine`、`JWInteger`、`ImageConcatMulti`、`GrowMask`、`BlockifyMask`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`Int`、`WanVideoSampler`、`CR Prompt Text`、`SeCVideoSegmentation`、`PointsEditor`、`LoadImage`、`VHS_LoadVideo`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
