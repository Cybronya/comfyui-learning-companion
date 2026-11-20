---
key: 平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json
name: SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json
hash: e35e2b51d34d9d63
coverage: 0.567568
learned_at: 2026-11-14 00:58:20
nodes: [INTConstant, INTConstant, SetNode, SetNode, WanVideoTextEncodeCached, ImageResizeKJv2, GrowMask, SetNode, SetNode, SetNode, ImageCropByMaskAndResize, GetNode, VHS_VideoCombine, VHS_VideoCombine, Sam2Segmentation, SetNode, Reroute, PixelPerfectResolution, BlockifyMask, DWPreprocessor, SetNode, SetNode, DrawMaskOnImage, FaceMaskFromPoseKeypoints, SetNode, MarkdownNote, WanVideoVAELoader, SetNode, CLIPVisionLoader, Reroute, PixelPerfectResolution, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, VHS_VideoCombine, FaceMaskFromPoseKeypoints, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, DWPreprocessor, GetNode, WanVideoClipVisionEncode, ImageCropByMaskAndResize, WanVideoContextOptions, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, DownloadAndLoadSAM2Model, VHS_VideoCombine, WanVideoSampler, PointsEditor, VHS_LoadVideo, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json

> 来源文件 `comfyui_library/workflows/平台全量/SeC整合版：6.WanAnimate 人物A的动作+B的表情混合迁移_1986448840238759938.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `GrowMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Sam2Segmentation`
- `SetNode`
- `Reroute`
- `PixelPerfectResolution`
- `BlockifyMask`
- `DWPreprocessor`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `MarkdownNote`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `PixelPerfectResolution`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `WanVideoClipVisionEncode`
- `ImageCropByMaskAndResize`
- `WanVideoContextOptions`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `DownloadAndLoadSAM2Model`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `PointsEditor`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **57%**（42/74）

**有卡**：`INTConstant`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`GrowMask`、`ImageCropByMaskAndResize`、`VHS_VideoCombine`、`Sam2Segmentation`、`PixelPerfectResolution`、`BlockifyMask`、`DWPreprocessor`、`DrawMaskOnImage`、`FaceMaskFromPoseKeypoints`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoAnimateEmbeds`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`PointsEditor`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
