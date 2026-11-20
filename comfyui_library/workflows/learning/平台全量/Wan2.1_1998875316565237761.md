---
key: 平台全量/Wan2.1_1998875316565237761.json
name: Wan2.1_1998875316565237761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_1998875316565237761.json
hash: 4f23cb05a7219f74
coverage: 0.467532
learned_at: 2026-11-14 01:04:41
nodes: [GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, GetNode, SetNode, VHS_VideoInfo, easy showAnything, SetNode, LayerUtility: PurgeVRAM, easy showAnything, ImageConcatMulti, LayerUtility: PurgeVRAM, PixelPerfectResolution, WanVideoSetLoRAs, WanVideoTorchCompileSettings, GetNode, WanVideoExperimentalArgs, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, GetImageSizeAndCount, GetNode, ImageConcatMulti, WanVideoDecode, GetNode, GetNode, WanVideoSampler, SetNode, SetNode, WanVideoVACEStartToEndFrame, GetNode, SetNode, WanVideoSLG, GetNode, GetNode, ImageBlend, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSetLoRAs, ImageFromBatch, GetNode, PreviewImage, GetNode, LayerUtility: PurgeVRAM, GetNode, CLIPVisionLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, ImageCropByMaskAndResize, GetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, DWPreprocessor, SetNode, GetNode, GetNode, SetNode, WanVideoSampler, easy imageSwitch, WanVideoAnimateEmbeds, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, VHS_VideoCombine, GetImageSizeAndCount, GetNode, GetNode, PrimitiveInt, LayerUtility: PurgeVRAM, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, WanVideoLoraSelectMulti, SetNode, GetNode, GetNode, SeCVideoSegmentation, GetNode, Note, GrowMask, WanVideoVACEEncode, GetNode, GetNode, Note, SetNode, GetNode, ImageResizeKJv2, GetNode, VHS_VideoCombine, VHS_VideoCombine, FaceMaskFromPoseKeypoints, Note, Note, SetNode, BlockifyMask, GetNode, DrawMaskOnImage, VHS_VideoCombine, GetNode, GetNode, DWPreprocessor, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetImageSizeAndCount, GetNode, GetNode, SetNode, LayerUtility: PurgeVRAM, SetNode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SeCModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoVAELoader, Fast Groups Bypasser (rgthree), WanVideoSetBlockSwap, SetNode, GetNode, VHS_VideoCombine, Int, Int, Int, PointsEditor, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.1_1998875316565237761.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_1998875316565237761.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（154 个）：
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `SetNode`
- `VHS_VideoInfo`
- `easy showAnything`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM`
- `PixelPerfectResolution`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `WanVideoExperimentalArgs`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `SetNode`
- `WanVideoSLG`
- `GetNode`
- `GetNode`
- `ImageBlend`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `ImageFromBatch`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `ImageCropByMaskAndResize`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `easy imageSwitch`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `SeCVideoSegmentation`
- `GetNode`
- `Note`
- `GrowMask`
- `WanVideoVACEEncode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FaceMaskFromPoseKeypoints`
- `Note`
- `Note`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `SeCModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoVAELoader`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `PointsEditor`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **47%**（72/154）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`ImageConcatMulti`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoExperimentalArgs`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVACEStartToEndFrame`、`WanVideoSLG`、`ImageBlend`、`WanVideoModelLoader`、`ImageFromBatch`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`easy imageSwitch`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoLoraSelectMulti`、`SeCVideoSegmentation`、`GrowMask`、`WanVideoVACEEncode`、`ImageResizeKJv2`、`FaceMaskFromPoseKeypoints`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoTextEncodeCached`、`SeCModelLoader`、`WanVideoVAELoader`、`Int`、`PointsEditor`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelectMulti
