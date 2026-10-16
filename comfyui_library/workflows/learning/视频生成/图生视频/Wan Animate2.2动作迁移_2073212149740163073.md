---
key: 视频生成/图生视频/Wan Animate2.2动作迁移_2073212149740163073.json
name: Wan Animate2.2动作迁移_2073212149740163073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073212149740163073.json
hash: 155c3485a5579e8f
coverage: 0.5
learned_at: 2026-10-15 22:41:01
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, ImageConcatMulti, GetNode, DWPreprocessor, GetNode, VHS_VideoCombine, WanVideoTextEncodeCached, Note, Note, Note, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, CR Prompt Text, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, PixelPerfectResolution, ImageCropByMaskAndResize, Reroute, SetNode, SetNode, GetNode, Note, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoModelLoader, WanVideoBlockSwap, GetNode, MarkdownNote, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, GetNode, WanVideoClipVisionEncode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageResizeKJv2, VHS_LoadVideo, JWInteger, JWInteger, VHS_VideoCombine, GetNode, SetNode, GetNode, GetNode, PointsEditor, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2动作迁移_2073212149740163073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073212149740163073.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageConcatMulti`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `Note`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `CR Prompt Text`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `Reroute`
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `GetNode`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `LoadImage`

## 知识

覆盖率 **50%**（37/74）

**有卡**：`FaceMaskFromPoseKeypoints`、`ImageConcatMulti`、`DWPreprocessor`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`CR Prompt Text`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`VHS_LoadVideo`、`JWInteger`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
