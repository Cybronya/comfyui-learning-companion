---
key: 视频生成/图生视频/Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json
name: Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json
hash: 90b3fd211cc9a289
coverage: 0.513514
learned_at: 2026-10-15 22:32:38
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoContextOptions, WanVideoSampler, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, DWPreprocessor, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, Note, VHS_VideoCombine, MarkdownNote, Note, INTConstant, INTConstant, SetNode, INTConstant, SetNode, ImageResizeKJv2, SetNode, VHS_LoadVideo, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, GetNode, SetNode, Note, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoTextEncodeCached, PointsEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981706242731196418.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PixelPerfectResolution`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `DWPreprocessor`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `Note`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_LoadVideo`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `PointsEditor`

## 知识

覆盖率 **51%**（38/74）

**有卡**：`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`DWPreprocessor`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`INTConstant`、`ImageResizeKJv2`、`VHS_LoadVideo`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`LoadImage`、`WanVideoTextEncodeCached`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
