---
key: 平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json
name: SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json
hash: d37622889950ca59
coverage: 0.558824
learned_at: 2026-11-14 00:58:16
nodes: [CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, ImageResizeKJv2, CLIPLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEmbedBridge, BlockifyMask, SetNode, SetNode, GrowMask, Sam2Segmentation, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, SetNode, GrowMaskWithBlur, WanVideoDecode, DrawViTPose, DownloadAndLoadSAM2Model, OnnxDetectionModelLoader, SetNode, SetNode, SetNode, SetNode, PoseAndFaceDetection, SetNode, WanVideoSetBlockSwap, VHS_VideoCombine, Note, ImpactInt, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, WanVideoVAELoader, GetNode, GetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSampler, GetNode, GetNode, GetNode, ImageFromBatch, WanVideoBlockSwap, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, DrawMaskOnImage, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, CLIPTextEncode, LoadImage, VHS_LoadVideo, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json

> 来源文件 `comfyui_library/workflows/平台全量/SeC整合版：4.WanAnimate 主体替换(自动)2.0_1986448672231718914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（68 个）：
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `CLIPLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEmbedBridge`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `GrowMask`
- `Sam2Segmentation`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `GrowMaskWithBlur`
- `WanVideoDecode`
- `DrawViTPose`
- `DownloadAndLoadSAM2Model`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `Note`
- `ImpactInt`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`

## 知识

覆盖率 **56%**（38/68）

**有卡**：`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`CLIPLoader`、`VHS_VideoCombine`、`WanVideoTextEmbedBridge`、`BlockifyMask`、`GrowMask`、`Sam2Segmentation`、`ImageConcatMulti`、`GrowMaskWithBlur`、`WanVideoDecode`、`DrawViTPose`、`DownloadAndLoadSAM2Model`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoSetBlockSwap`、`ImpactInt`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSampler`、`ImageFromBatch`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`

**用到的条目**：CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoVAELoader
