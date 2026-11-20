---
key: 平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json
name: Wan Animate2.2 主体不变只变背景_1971803048211378177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json
hash: b9311bb77b62e974
coverage: 0.5
learned_at: 2026-11-14 01:03:57
nodes: [GetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, JWInteger, SetNode, JWInteger, SetNode, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, GetNode, SetNode, ImageCropByMaskAndResize, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, BlockifyMask, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoUni3C_embeds, GetNode, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, PreviewImage, SetNode, ImageResizeKJv2, GetNode, VHS_LoadVideo, VHS_VideoCombine, Manual XY Entry Info, PreviewImage, ImageFromBatch+, GetNode, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, WanVideoSampler, DownloadAndLoadSAM2Model, GetNode, JWInteger, VHS_LoadVideo, Display Any (rgthree), WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, ImageConcatMulti, SetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, GetImageSizeAndCount, LoadImage, PointsEditor, SetNode, Sam2Segmentation, InvertMask, CR Prompt Text, GetNode]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2 主体不变只变背景_1971803048211378177.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（92 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Manual XY Entry Info`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `JWInteger`
- `VHS_LoadVideo`
- `Display Any (rgthree)`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `LoadImage`
- `PointsEditor`
- `SetNode`
- `Sam2Segmentation`
- `InvertMask`
- `CR Prompt Text`
- `GetNode`

## 知识

覆盖率 **50%**（46/92）

**有卡**：`DrawMaskOnImage`、`JWInteger`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`BlockifyMask`、`WanVideoTextEncodeCached`、`WanVideoUni3C_embeds`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`VHS_LoadVideo`、`VHS_VideoCombine`、`Manual XY Entry Info`、`ImageFromBatch+`、`WanVideoDecode`、`WanVideoSampler`、`DownloadAndLoadSAM2Model`、`Display Any (rgthree)`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`GetImageSizeAndCount`、`LoadImage`、`PointsEditor`、`Sam2Segmentation`、`InvertMask`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
