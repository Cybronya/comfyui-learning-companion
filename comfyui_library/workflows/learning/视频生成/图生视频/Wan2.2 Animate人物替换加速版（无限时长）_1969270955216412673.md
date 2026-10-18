---
key: 视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json
name: Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json
hash: 4580d99dc50da022
coverage: 0.558824
learned_at: 2026-10-15 22:31:48
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, GetNode, SetNode, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, Sam2Segmentation, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, ImageCropByMaskAndResize, SetNode, GetNode, GetImageSizeAndCount, JWInteger, PrimitiveStringMultiline, DownloadAndLoadSAM2Model, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, ImageResizeKJv2, ImageConcatMulti, GetNode, SetNode, SetNode, JWInteger, WanVideoClipVisionEncode, SetNode, SetNode, LoadImage, VHS_VideoCombine, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM V2, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PointsEditor, LayerUtility: PurgeVRAM V2, WanVideoAnimateEmbeds, MarkdownNote, VHS_LoadVideo, easy int, WanVideoDecode, easy cleanGpuUsed, DWPreprocessor, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969270955216412673.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（68 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Sam2Segmentation`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `JWInteger`
- `PrimitiveStringMultiline`
- `DownloadAndLoadSAM2Model`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PointsEditor`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoAnimateEmbeds`
- `MarkdownNote`
- `VHS_LoadVideo`
- `easy int`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `DWPreprocessor`
- `WanVideoBlockSwap`

## 知识

覆盖率 **56%**（38/68）

**有卡**：`ImageConcatMulti`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Sam2Segmentation`、`DrawMaskOnImage`、`CLIPVisionLoader`、`ImageCropByMaskAndResize`、`GetImageSizeAndCount`、`JWInteger`、`DownloadAndLoadSAM2Model`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`LoadImage`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`、`PointsEditor`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`easy int`、`WanVideoDecode`、`easy cleanGpuUsed`、`DWPreprocessor`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
