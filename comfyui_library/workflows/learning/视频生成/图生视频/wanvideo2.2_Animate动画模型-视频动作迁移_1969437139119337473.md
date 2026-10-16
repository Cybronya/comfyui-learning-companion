---
key: 视频生成/图生视频/wanvideo2.2_Animate动画模型-视频动作迁移_1969437139119337473.json
name: wanvideo2.2_Animate动画模型-视频动作迁移_1969437139119337473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969437139119337473.json
hash: f710d5d1066a415e
coverage: 0.546875
learned_at: 2026-10-15 22:31:49
nodes: [ImageConcatMulti, DWPreprocessor, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, SetNode, SetNode, PixelPerfectResolution, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GrowMask, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, Note, SetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, WanVideoDecode, GetNode, GetImageSizeAndCount, WanVideoContextOptions, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoSampler, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, WanVideoAnimateEmbeds, VHS_VideoCombine, INTConstant, INTConstant, ImageConcatMulti, PointsEditor, GetNode, VHS_LoadVideo, LoadImage, ImageResizeKJv2, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo2.2_Animate动画模型-视频动作迁移_1969437139119337473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969437139119337473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `ImageConcatMulti`
- `DWPreprocessor`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `SetNode`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `ImageConcatMulti`
- `PointsEditor`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **55%**（35/64）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAnimateEmbeds`、`INTConstant`、`PointsEditor`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
