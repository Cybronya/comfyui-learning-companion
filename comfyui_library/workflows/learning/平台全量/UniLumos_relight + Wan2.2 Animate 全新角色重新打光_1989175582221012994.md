---
key: 平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json
name: UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json
hash: 40b519f00090f3c9
coverage: 0.490385
learned_at: 2026-11-14 01:02:03
nodes: [LoadWanVideoT5TextEncoder, WanVideoSampler, MarkdownNote, WanVideoTextEncode, WanVideoDecode, GetImageSizeAndCount, WanVideoUniLumosEmbeds, TransparentBGSession+, ImageRemoveBackground+, WanVideoEncode, WanVideoVAELoader, DrawMaskOnImage, InvertMask, WanVideoSetLoRAs, DrawGaussianNoiseOnImage, MarkdownNote, Note, VHS_VideoCombine, ShowText|pysssss, DrawMaskOnImage, SetNode, SetNode, SetNode, SetNode, BlockifyMask, DrawViTPose, PoseAndFaceDetection, easy cleanGpuUsed, DrawMaskOnImage, PrimitiveInt, PrimitiveInt, SetNode, SetNode, SetNode, PrimitiveInt, LayerUtility: PurgeVRAM, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageFromBatch+, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, CLIPVisionLoader, SetNode, MarkdownNote, GetNode, SetNode, GetNode, SetNode, SetNode, WanVideoDecode, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, SetNode, WanVideoTextEncode, GetNode, LayerUtility: PurgeVRAM, GetNode, LayerUtility: PurgeVRAM, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, OnnxDetectionModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, GetNode, GetNode, GetNode, GetNode, Float to Int, PrimitiveInt, AILab_QwenVL_Advanced, VHS_VideoInfoLoaded, VHS_VideoCombine, SetNode, ImageResizeKJv2, SetNode, SetNode, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, VHS_LoadVideo, VHS_VideoCombine, WanVideoEncode, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json

> 来源文件 `comfyui_library/workflows/平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（104 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoUniLumosEmbeds`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `DrawMaskOnImage`
- `InvertMask`
- `WanVideoSetLoRAs`
- `DrawGaussianNoiseOnImage`
- `MarkdownNote`
- `Note`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `DrawMaskOnImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `SetNode`
- `WanVideoTextEncode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `OnnxDetectionModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Float to Int`
- `PrimitiveInt`
- `AILab_QwenVL_Advanced`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **49%**（51/104）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoUniLumosEmbeds`、`TransparentBGSession+`、`ImageRemoveBackground+`、`WanVideoEncode`、`WanVideoVAELoader`、`DrawMaskOnImage`、`InvertMask`、`WanVideoSetLoRAs`、`DrawGaussianNoiseOnImage`、`VHS_VideoCombine`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`ImageFromBatch+`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`OnnxDetectionModelLoader`、`WanVideoLoraSelectMulti`、`Float to Int`、`AILab_QwenVL_Advanced`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
