---
key: 视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json
name: Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json
hash: 7cfda0a604e62ce6
coverage: 0.480769
learned_at: 2026-10-15 22:47:06
nodes: [WanVideoSampler, MarkdownNote, WanVideoTextEncode, WanVideoEncode, WanVideoEncode, InvertMask, MarkdownNote, VHS_VideoCombine, ShowText|pysssss, DrawMaskOnImage, SetNode, SetNode, SetNode, BlockifyMask, DrawViTPose, PoseAndFaceDetection, easy cleanGpuUsed, DrawMaskOnImage, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSampler, WanVideoDecode, WanVideoAnimateEmbeds, SetNode, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, ImageRemoveBackground+, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, WanVideoDecode, GetImageSizeAndCount, SetNode, OnnxDetectionModelLoader, MarkdownNote, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoLoraSelect, WanVideoVAELoader, GetNode, AILab_QwenVL_Advanced, GetNode, WanVideoModelLoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, WanVideoUniLumosEmbeds, GetNode, PrimitiveInt, PrimitiveInt, ImageFromBatch+, ImageResizeKJv2, SetNode, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, PrimitiveInt, SetNode, SetNode, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, TransparentBGSession+, DrawMaskOnImage, DrawGaussianNoiseOnImage, VHS_VideoCombine, Note, VHS_LoadVideo, Note, Note, VHS_LoadVideo, VHS_VideoCombine, Note]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（104 个）：
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoEncode`
- `InvertMask`
- `MarkdownNote`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `DrawMaskOnImage`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `ImageRemoveBackground+`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `SetNode`
- `OnnxDetectionModelLoader`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `GetNode`
- `AILab_QwenVL_Advanced`
- `GetNode`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoUniLumosEmbeds`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `TransparentBGSession+`
- `DrawMaskOnImage`
- `DrawGaussianNoiseOnImage`
- `VHS_VideoCombine`
- `Note`
- `VHS_LoadVideo`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **48%**（50/104）

**有卡**：`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEncode`、`InvertMask`、`VHS_VideoCombine`、`DrawMaskOnImage`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`LayerUtility: PurgeVRAM`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`ImageRemoveBackground+`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`AILab_QwenVL_Advanced`、`LoadWanVideoT5TextEncoder`、`WanVideoUniLumosEmbeds`、`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`TransparentBGSession+`、`DrawGaussianNoiseOnImage`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
