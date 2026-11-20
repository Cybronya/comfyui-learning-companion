---
key: 平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json
name: Wan2.2 Animate 人物替换（背景保持）_2078709416081317890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json
hash: 3d5bb4e2419bff5d
coverage: 0.746479
learned_at: 2026-11-14 01:04:58
nodes: [ImageConcatMulti, GetNode, VHS_VideoCombine, GetNode, ImageConcatMulti, SimpleMath+, GetNode, GetImageSizeAndCount, Int, WanVideoBlockSwap, WanVideoSetLoRAs, RHHiddenNodes, Note, QwenVLDetection, Note, LayerMask: SAM2Ultra, Int, WanVideoSetBlockSwap, SetNode, Note, Note, CR Text, Note, ImageFromBatch, LayerUtility: PurgeVRAM, MaskPreview+, SeCModelLoader, SetNode, Reroute, LayerUtility: ImageScaleByAspectRatio V2, Int, Int, SetNode, SetNode, OnnxDetectionModelLoader, LayerUtility: PurgeVRAM, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, WanVideoTextEncodeCached, Reroute, Note, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoDecode, WanVideoSampler, GetNode, GetNode, LayerUtility: PurgeVRAM, WanVideoVAELoader, PoseAndFaceDetection, DrawViTPose, WanVideoAnimateEmbeds, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoModelLoader, DownloadAndLoadQwenModel, BBoxesToSAM2, LayerUtility: PurgeVRAM, CLIPVisionLoader, VHS_LoadVideo, WanVideoLoraSelectMulti, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM V2, SeCVideoSegmentation, RHHiddenNodes, LoadImage, GetNode, Int, CM_IntToFloat]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（71 个）：
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `SimpleMath+`
- `GetNode`
- `GetImageSizeAndCount`
- `Int`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `RHHiddenNodes`
- `Note`
- `QwenVLDetection`
- `Note`
- `LayerMask: SAM2Ultra`
- `Int`
- `WanVideoSetBlockSwap`
- `SetNode`
- `Note`
- `Note`
- `CR Text`
- `Note`
- `ImageFromBatch`
- `LayerUtility: PurgeVRAM`
- `MaskPreview+`
- `SeCModelLoader`
- `SetNode`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `Reroute`
- `Note`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `WanVideoAnimateEmbeds`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `DownloadAndLoadQwenModel`
- `BBoxesToSAM2`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionLoader`
- `VHS_LoadVideo`
- `WanVideoLoraSelectMulti`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM V2`
- `SeCVideoSegmentation`
- `RHHiddenNodes`
- `LoadImage`
- `GetNode`
- `Int`
- `CM_IntToFloat`

## 知识

覆盖率 **75%**（53/71）

**有卡**：`ImageConcatMulti`、`VHS_VideoCombine`、`SimpleMath+`、`GetImageSizeAndCount`、`Int`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`RHHiddenNodes`、`QwenVLDetection`、`LayerMask: SAM2Ultra`、`WanVideoSetBlockSwap`、`CR Text`、`ImageFromBatch`、`LayerUtility: PurgeVRAM`、`MaskPreview+`、`SeCModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoAnimateEmbeds`、`WanVideoModelLoader`、`DownloadAndLoadQwenModel`、`BBoxesToSAM2`、`CLIPVisionLoader`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`WanVideoClipVisionEncode`、`LayerUtility: PurgeVRAM V2`、`SeCVideoSegmentation`、`LoadImage`、`CM_IntToFloat`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
