---
key: 平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json
name: Wan2.2 Animate高质量多人测试_1988538984588558337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json
hash: e8a6ea02a4a391df
coverage: 0.575472
learned_at: 2026-11-14 01:05:27
nodes: [GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, SetNode, WanVideoModelLoader, WanVideoVAELoader, GetNode, ImageConcatMulti, VHS_VideoCombine, WanVideoTextEncodeCached, ImageResizeKJv2, GrowMask, Int, Note, Note, ImageConcatMulti, WanVideoClipVisionEncode, CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, GetNode, RepeatImageBatch, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoUni3C_embeds, WanVideoLoraSelectMulti, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, BlockifyMask, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, Note, LayerUtility: PurgeVRAM V2, SetNode, SetNode, Note, SetNode, SetNode, SetNode, DrawMaskOnImage, Note, Note, Sam2VideoSegmentation, MaskToImage, Note, ImageBatchGet, Note, PoseAndFaceDetection, VHS_VideoCombine, WanVideoSampler, WanVideoLoraSelectMulti, QwenVLDetection, BBoxesToSAM2, LayerMask: SAM2VideoUltra, PreviewImage, CR Text, DownloadAndLoadQwenModel, VHS_VideoCombine, GetNode, GetNode, LoadImage, VHS_LoadVideo, JWInteger, JWInteger, PointsEditor, GetNode, SeCVideoSegmentation, GrowMask, BlockifyMask, GetNode, Note, SetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, SeCModelLoader, SetNode, DrawViTPose, GetImageSizeAndCount, OnnxDetectionModelLoader, Reroute, PoseRetargetPromptHelper, Reroute, PixelPerfectResolution, VHS_VideoCombine, SetNode, FaceMaskFromPoseKeypoints, GetNode, SetNode, DWPreprocessor, ImageCropByMaskAndResize, VHS_VideoCombine, easy showAnything, easy showAnything]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（106 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `GrowMask`
- `Int`
- `Note`
- `Note`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetNode`
- `RepeatImageBatch`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `Note`
- `Note`
- `Sam2VideoSegmentation`
- `MaskToImage`
- `Note`
- `ImageBatchGet`
- `Note`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `QwenVLDetection`
- `BBoxesToSAM2`
- `LayerMask: SAM2VideoUltra`
- `PreviewImage`
- `CR Text`
- `DownloadAndLoadQwenModel`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `PointsEditor`
- `GetNode`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `GetNode`
- `Note`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `SetNode`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `Reroute`
- `PoseRetargetPromptHelper`
- `Reroute`
- `PixelPerfectResolution`
- `VHS_VideoCombine`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `SetNode`
- `DWPreprocessor`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy showAnything`

## 知识

覆盖率 **58%**（61/106）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`GrowMask`、`Int`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`RepeatImageBatch`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`BlockifyMask`、`WanVideoAnimateEmbeds`、`LayerUtility: PurgeVRAM V2`、`DrawMaskOnImage`、`Sam2VideoSegmentation`、`MaskToImage`、`ImageBatchGet`、`PoseAndFaceDetection`、`WanVideoSampler`、`QwenVLDetection`、`BBoxesToSAM2`、`LayerMask: SAM2VideoUltra`、`CR Text`、`DownloadAndLoadQwenModel`、`LoadImage`、`VHS_LoadVideo`、`JWInteger`、`PointsEditor`、`SeCVideoSegmentation`、`SeCModelLoader`、`DrawViTPose`、`OnnxDetectionModelLoader`、`PoseRetargetPromptHelper`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`ImageCropByMaskAndResize`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
