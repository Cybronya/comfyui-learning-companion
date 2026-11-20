---
key: 平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json
name: Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json
hash: 622f0b4d1a079e2c
coverage: 0.558442
learned_at: 2026-11-14 01:04:00
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageConcatMulti, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, SetNode, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, Note, WanVideoModelLoader, WanVideoTextEncodeCached, Note, SetNode, SetNode, PixelPerfectResolution, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine, UltralyticsDetectorProvider, ImageResizeKJv2, DWPreprocessor, FaceMaskFromPoseKeypoints, Reroute, SetNode, easy showAnything, easy showAnything, GetImageSize, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, SetNode, ImageCropByMaskAndResize, WanVideoSampler, GetNode, CR Prompt Text, WanVideoVAELoader, easy ifElse, easy compare, PreviewImage, BboxDetectorSEGS, SegsToCombinedMask, easy imageCropFromMask, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, SetNode, SetNode, VHS_LoadVideo, JWInteger, JWInteger, ImageFromBatch+, DownloadAndLoadSAM2Model, VHS_VideoCombine, GetNode, GrowMask, SetNode, DrawMaskOnImage, SetNode, BlockifyMask, PointsEditor, Sam2Segmentation]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2主体迁移（自动裁剪脸部）v1_1969661416292687873.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `SetNode`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `Note`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `UltralyticsDetectorProvider`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `Reroute`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `GetImageSize`
- `WanVideoDecode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `GetNode`
- `CR Prompt Text`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy compare`
- `PreviewImage`
- `BboxDetectorSEGS`
- `SegsToCombinedMask`
- `easy imageCropFromMask`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `ImageFromBatch+`
- `DownloadAndLoadSAM2Model`
- `VHS_VideoCombine`
- `GetNode`
- `GrowMask`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `BlockifyMask`
- `PointsEditor`
- `Sam2Segmentation`

## 知识

覆盖率 **56%**（43/77）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`PixelPerfectResolution`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`UltralyticsDetectorProvider`、`ImageResizeKJv2`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`GetImageSize`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`CR Prompt Text`、`WanVideoVAELoader`、`easy compare`、`BboxDetectorSEGS`、`SegsToCombinedMask`、`easy imageCropFromMask`、`VHS_LoadVideo`、`JWInteger`、`ImageFromBatch+`、`DownloadAndLoadSAM2Model`、`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`PointsEditor`、`Sam2Segmentation`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
