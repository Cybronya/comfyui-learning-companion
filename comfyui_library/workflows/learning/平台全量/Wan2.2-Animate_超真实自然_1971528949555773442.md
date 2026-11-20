---
key: 平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json
name: Wan2.2-Animate_超真实自然_1971528949555773442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json
hash: 8c6ff6335b02c40a
coverage: 0.541667
learned_at: 2026-11-14 01:05:56
nodes: [WanVideoSampler, WanVideoVAELoader, GetImageSizeAndCount, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, ImageConcatMulti, WanVideoClipVisionEncode, CLIPVisionLoader, ImageConcatMulti, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, PoseRetargetPromptHelper, DrawViTPose, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, ImageResizeKJv2, Anything Everywhere, WanVideoModelLoader, WanVideoLoraSelectMulti, Note, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, GetNode, DrawMaskOnImage, BlockifyMask, GrowMask, GetNode, WanVideoDecode, easy showAnything, SetNode, GetNode, SetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, Anything Everywhere, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, WanVideoTextEncodeCached, Int, VHS_LoadVideo, LoadImage, PrimitiveStringMultiline, Int, Int, Int]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate_超真实自然_1971528949555773442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（72 个）：
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `ImageConcatMulti`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PoseRetargetPromptHelper`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `Anything Everywhere`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `GetNode`
- `WanVideoDecode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `Anything Everywhere`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `Int`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **54%**（39/72）

**有卡**：`WanVideoSampler`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`VHS_VideoCombine`、`PoseRetargetPromptHelper`、`DrawViTPose`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`WanVideoDecode`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`Int`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
