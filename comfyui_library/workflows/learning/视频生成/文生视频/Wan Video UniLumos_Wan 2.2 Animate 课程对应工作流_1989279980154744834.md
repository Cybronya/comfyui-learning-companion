---
key: 视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json
name: Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json
hash: 7cfda0a604e62ce6
coverage: 0.413462
learned_at: 2026-10-10 23:06:20
nodes: [WanVideoSampler, MarkdownNote, WanVideoTextEncode, WanVideoEncode, WanVideoEncode, InvertMask, MarkdownNote, VHS_VideoCombine, ShowText|pysssss, DrawMaskOnImage, SetNode, SetNode, SetNode, BlockifyMask, DrawViTPose, PoseAndFaceDetection, easy cleanGpuUsed, DrawMaskOnImage, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoSampler, WanVideoDecode, WanVideoAnimateEmbeds, SetNode, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, ImageRemoveBackground+, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, WanVideoDecode, GetImageSizeAndCount, SetNode, OnnxDetectionModelLoader, MarkdownNote, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoLoraSelect, WanVideoVAELoader, GetNode, AILab_QwenVL_Advanced, GetNode, WanVideoModelLoader, LoadWanVideoT5TextEncoder, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, WanVideoUniLumosEmbeds, GetNode, PrimitiveInt, PrimitiveInt, ImageFromBatch+, ImageResizeKJv2, SetNode, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, PrimitiveInt, SetNode, SetNode, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, TransparentBGSession+, DrawMaskOnImage, DrawGaussianNoiseOnImage, VHS_VideoCombine, Note, VHS_LoadVideo, Note, Note, VHS_LoadVideo, VHS_VideoCombine, Note]
patterns: []
missing: [ImageFromBatch+, ImageRemoveBackground+, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, TransparentBGSession+, easy cleanGpuUsed]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
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

覆盖率 **41%**（43/104）

**有卡**：`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEncode`、`InvertMask`、`VHS_VideoCombine`、`DrawMaskOnImage`、`BlockifyMask`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`AILab_QwenVL_Advanced`、`LoadWanVideoT5TextEncoder`、`WanVideoUniLumosEmbeds`、`VHS_VideoInfoLoaded`、`DrawGaussianNoiseOnImage`、`VHS_LoadVideo`

**缺卡**（7）：`ImageFromBatch+`、`ImageRemoveBackground+`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`TransparentBGSession+`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageRemoveBackground+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `TransparentBGSession+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
