---
key: 视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json
name: Wan Animate2.2人物融合_2073212185333026818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json
hash: 03e035043e2be3f2
coverage: 0.5
learned_at: 2026-10-15 22:41:01
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, ImageConcatMulti, GetNode, DWPreprocessor, GetNode, VHS_VideoCombine, WanVideoTextEncodeCached, Note, Note, Note, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, CR Prompt Text, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, PixelPerfectResolution, ImageCropByMaskAndResize, Reroute, SetNode, SetNode, GetNode, Note, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds, WanVideoBlockSwap, GetNode, MarkdownNote, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, GetNode, WanVideoClipVisionEncode, GetNode, SetNode, ImageResizeKJv2, VHS_LoadVideo, JWInteger, JWInteger, VHS_VideoCombine, GetNode, SetNode, GetNode, GetNode, PointsEditor, LoadImage, WanVideoModelLoader, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073212185333026818.json`

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
- `WanVideoBlockSwap`
- `GetNode`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
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
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **50%**（37/74）

**有卡**：`FaceMaskFromPoseKeypoints`、`ImageConcatMulti`、`DWPreprocessor`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`CLIPVisionLoader`、`CR Prompt Text`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`VHS_LoadVideo`、`JWInteger`、`PointsEditor`、`LoadImage`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
