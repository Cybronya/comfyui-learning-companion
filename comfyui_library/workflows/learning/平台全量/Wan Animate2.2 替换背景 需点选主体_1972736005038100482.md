---
key: 平台全量/Wan Animate2.2 替换背景 需点选主体_1972736005038100482.json
name: Wan Animate2.2 替换背景 需点选主体_1972736005038100482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2 替换背景 需点选主体_1972736005038100482.json
hash: 797055acfa95b65f
coverage: 0.5
learned_at: 2026-11-14 01:03:59
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, DWPreprocessor, SetNode, FaceMaskFromPoseKeypoints, PixelPerfectResolution, GetNode, SetNode, ImageCropByMaskAndResize, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoUni3C_embeds, GetNode, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, PreviewImage, SetNode, Manual XY Entry Info, PreviewImage, ImageFromBatch+, GetNode, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, WanVideoSampler, DownloadAndLoadSAM2Model, GetNode, Display Any (rgthree), WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, ImageConcatMulti, SetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, GetImageSizeAndCount, GetNode, LoadImage, VHS_LoadVideo, CR Prompt Text, VHS_LoadVideo, GetNode, GetNode, ImageResizeKJv2, JWInteger, JWInteger, GetNode, Sam2Segmentation, InvertMask, BlockifyMask, SetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, PointsEditor, JWInteger]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2 替换背景 需点选主体_1972736005038100482.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2 替换背景 需点选主体_1972736005038100482.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（92 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `GetNode`
- `Sam2Segmentation`
- `InvertMask`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `PointsEditor`
- `JWInteger`

## 知识

覆盖率 **50%**（46/92）

**有卡**：`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoUni3C_embeds`、`easy cleanGpuUsed`、`Manual XY Entry Info`、`ImageFromBatch+`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`DownloadAndLoadSAM2Model`、`Display Any (rgthree)`、`WanVideoAnimateEmbeds`、`ImageConcatMulti`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`LoadImage`、`VHS_LoadVideo`、`CR Prompt Text`、`JWInteger`、`Sam2Segmentation`、`InvertMask`、`BlockifyMask`、`DrawMaskOnImage`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
