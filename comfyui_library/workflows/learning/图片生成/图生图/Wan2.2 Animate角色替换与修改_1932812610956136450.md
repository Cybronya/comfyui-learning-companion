---
key: 图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json
name: Wan2.2 Animate角色替换与修改_1932812610956136450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json
hash: d82cec36164cc374
coverage: 0.53125
learned_at: 2026-10-23 11:27:59
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, GetNode, SetNode, SetNode, Reroute, PixelPerfectResolution, SetNode, WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, MarkdownNote, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, GetNode, GetImageSizeAndCount, BlockifyMask, GetNode, SetNode, GetNode, SetNode, Note, Sam2Segmentation, DownloadAndLoadSAM2Model, DrawMaskOnImage, SetNode, VHS_VideoCombine, DWPreprocessor, SetNode, WanVideoLoraSelectMulti, INTConstant, INTConstant, VHS_LoadVideo, PointsEditor, GrowMask, LoadImage, ImageResizeKJv2, VHS_VideoCombine, WanVideoModelLoader, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `GetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `PixelPerfectResolution`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `BlockifyMask`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Note`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `PointsEditor`
- `GrowMask`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **53%**（34/64）

**有卡**：`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`BlockifyMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`DrawMaskOnImage`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoLoraSelectMulti`、`INTConstant`、`VHS_LoadVideo`、`PointsEditor`、`GrowMask`、`LoadImage`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
