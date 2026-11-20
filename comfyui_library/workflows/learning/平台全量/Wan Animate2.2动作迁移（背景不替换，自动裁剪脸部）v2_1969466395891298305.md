---
key: 平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json
name: Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json
hash: 272ec91756d164fc
coverage: 0.553846
learned_at: 2026-11-14 01:04:01
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageConcatMulti, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GetNode, GetNode, SetNode, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, GetNode, Note, WanVideoModelLoader, WanVideoTextEncodeCached, Note, SetNode, JWInteger, JWInteger, VHS_LoadVideo, SetNode, PixelPerfectResolution, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine, UltralyticsDetectorProvider, ImageResizeKJv2, DWPreprocessor, FaceMaskFromPoseKeypoints, Reroute, SetNode, easy showAnything, easy showAnything, GetImageSize, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, SetNode, ImageCropByMaskAndResize, WanVideoSampler, GetNode, CR Prompt Text, WanVideoVAELoader, easy ifElse, easy compare, PreviewImage, BboxDetectorSEGS, SegsToCombinedMask, ImageFromBatch+, easy imageCropFromMask]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2动作迁移（背景不替换，自动裁剪脸部）v2_1969466395891298305.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（65 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
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
- `SetNode`
- `GetNode`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `Note`
- `SetNode`
- `JWInteger`
- `JWInteger`
- `VHS_LoadVideo`
- `SetNode`
- `PixelPerfectResolution`
- `VHS_VideoCombine`
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
- `ImageFromBatch+`
- `easy imageCropFromMask`

## 知识

覆盖率 **55%**（36/65）

**有卡**：`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`JWInteger`、`VHS_LoadVideo`、`PixelPerfectResolution`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`UltralyticsDetectorProvider`、`ImageResizeKJv2`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`GetImageSize`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`CR Prompt Text`、`WanVideoVAELoader`、`easy compare`、`BboxDetectorSEGS`、`SegsToCombinedMask`、`ImageFromBatch+`、`easy imageCropFromMask`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
