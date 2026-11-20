---
key: 平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json
name: Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json
hash: 7f616ed9d535443e
coverage: 0.457143
learned_at: 2026-11-14 01:05:06
nodes: [LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, SetNode, LayerUtility: PurgeVRAM, easy showAnything, PixelPerfectResolution, SetNode, SetNode, SetNode, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, DWPreprocessor, SetNode, GetNode, SetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, PrimitiveInt, LayerUtility: PurgeVRAM, ImageFromBatch, GetNode, GetNode, SetNode, GetNode, Note, VHS_VideoCombine, Note, GetNode, VHS_VideoCombine, GetNode, WanVideoVAELoader, GetNode, Note, WanVideoTextEncodeCached, Int, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoAnimateEmbeds, WanVideoBlockSwap, GetNode, LoadImage, ImageResizeKJv2, GetNode, GetNode, PreviewImage, SetNode, GetNode, WanVideoLoraSelectMulti, SetNode, SetNode, VHS_VideoInfo, LayerUtility: PurgeVRAM, SetNode, DWPreprocessor, GetNode, VHS_VideoCombine, SeCModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, Fast Groups Bypasser (rgthree), WanVideoSampler, easy imageSwitch, GetNode, GetNode, ImageFromBatch, PreviewImage, CLIPVisionLoader, GetNode, LayerUtility: PurgeVRAM, WanVideoDecode, LayerUtility: PurgeVRAM, Int, Int, DrawMaskOnImage, GrowMask, BlockifyMask, SetNode, GetNode, GetNode, PointsEditor, SeCVideoSegmentation, Note, VHS_VideoCombine, Note, GetNode, VHS_LoadVideo, VHS_VideoCombine, RIFE VFI, GetImageSizeAndCount, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate_Wan2.1 影视人物替换_2008805512766296066.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（105 个）：
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `PixelPerfectResolution`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoVAELoader`
- `GetNode`
- `Note`
- `WanVideoTextEncodeCached`
- `Int`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `GetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `DWPreprocessor`
- `GetNode`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSampler` ★核心
- `easy imageSwitch`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `CLIPVisionLoader`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `Int`
- `Int`
- `DrawMaskOnImage`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `SeCVideoSegmentation`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `RIFE VFI`
- `GetImageSizeAndCount`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **46%**（48/105）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`PixelPerfectResolution`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoClipVisionEncode`、`ImageFromBatch`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`Int`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`LoadImage`、`ImageResizeKJv2`、`WanVideoLoraSelectMulti`、`VHS_VideoInfo`、`SeCModelLoader`、`WanVideoSampler`、`easy imageSwitch`、`CLIPVisionLoader`、`WanVideoDecode`、`DrawMaskOnImage`、`GrowMask`、`BlockifyMask`、`PointsEditor`、`SeCVideoSegmentation`、`VHS_LoadVideo`、`RIFE VFI`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
