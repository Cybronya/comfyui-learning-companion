---
key: 平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json
name: Wan Animate2.2只替换人脸_1971453832461008897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json
hash: 75471a3582d5c118
coverage: 0.5
learned_at: 2026-11-14 01:04:02
nodes: [SetNode, SetNode, SetNode, DrawMaskOnImage, JWInteger, SetNode, JWInteger, SetNode, JWInteger, GetNode, GetNode, SetNode, PixelPerfectResolution, SetNode, ImageCropByMaskAndResize, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, WanVideoAnimateEmbeds, VHS_LoadVideo, CR Prompt Text, Manual XY Entry Info, VHS_LoadVideo, PreviewImage, VHS_VideoCombine, WanVideoSampler, PreviewImage, ImageFromBatch+, GetNode, LayerMask: MaskPreview, SetNode, GetNode, GetNode, FaceMaskFromPoseKeypoints, GetNode, GetNode, DWPreprocessor, APersonMaskGenerator, BlockifyMask, GetNode, GetNode, GetNode, FaceProcessorLoader, LoadImage, ImageResizeKJv2, SetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, ApplyFaceProcessor, PreviewImage, ImageConcatMulti, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, PreviewImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（92 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `SetNode`
- `PixelPerfectResolution`
- `SetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `Manual XY Entry Info`
- `VHS_LoadVideo`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `APersonMaskGenerator`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceProcessorLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `ApplyFaceProcessor`
- `PreviewImage`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **50%**（46/92）

**有卡**：`DrawMaskOnImage`、`JWInteger`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`CR Prompt Text`、`Manual XY Entry Info`、`VHS_VideoCombine`、`WanVideoSampler`、`ImageFromBatch+`、`LayerMask: MaskPreview`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`APersonMaskGenerator`、`BlockifyMask`、`FaceProcessorLoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ApplyFaceProcessor`、`ImageConcatMulti`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
