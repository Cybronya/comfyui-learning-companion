---
key: 数字人/数字人/AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362.json
name: AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362.json
hash: d5f2e38f0e076253
coverage: 0.555556
learned_at: 2026-10-26 01:53:43
nodes: [SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, SetNode, SetNode, PixelPerfectResolution, SetNode, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GrowMask, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, Note, SetNode, VHS_VideoCombine, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, GetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, INTConstant, INTConstant, Bjornulf_ShowInt, VHS_VideoCombine, LoadImage, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, GetNode, ImageResizeKJv2, PreviewImage, WanVideoDecode, Bjornulf_ShowInt, Note, DWPreprocessor, GetNode, GetNode, VHS_LoadVideo, PointsEditor, WanVideoTextEncodeCached, WanVideoSampler, VHS_VideoCombine, Label (rgthree), WanVideoAnimateEmbeds, GetImageSizeAndCount]
patterns: []
missing: []
---

# 数字人/数字人/AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI模仿mean girl表情打量别人，Wan-Animate数字人初体验_1969328742353039362.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（63 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `VHS_VideoCombine`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `Bjornulf_ShowInt`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoDecode`
- `Bjornulf_ShowInt`
- `Note`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PointsEditor`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `WanVideoAnimateEmbeds`
- `GetImageSizeAndCount`

## 知识

覆盖率 **56%**（35/63）

**有卡**：`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`INTConstant`、`Bjornulf_ShowInt`、`LoadImage`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoDecode`、`DWPreprocessor`、`VHS_LoadVideo`、`PointsEditor`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`Label (rgthree)`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
