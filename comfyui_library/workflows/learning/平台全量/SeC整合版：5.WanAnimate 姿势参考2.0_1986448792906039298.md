---
key: 平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json
name: SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json
hash: f11213f03c830732
coverage: 0.553571
learned_at: 2026-11-14 00:58:17
nodes: [ImpactInt, Note, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, ImageResizeKJv2, WanVideoTextEmbedBridge, CLIPVisionLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, CLIPLoader, WanVideoTorchCompileSettings, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoLoraSelectMulti, ImageConcatMulti, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, DrawViTPose, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, WanVideoSetLoRAs, SetNode, VHS_VideoCombine, PoseAndFaceDetection, WanVideoSampler, SetNode, SetNode, GetNode, SetNode, ImageFromBatch, GetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VHS_LoadVideo, LoadImage, WanVideoModelLoader]
patterns: []
missing: []
---

# 平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json

> 来源文件 `comfyui_library/workflows/平台全量/SeC整合版：5.WanAnimate 姿势参考2.0_1986448792906039298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（56 个）：
- `ImpactInt`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoTextEmbedBridge`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `CLIPLoader`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `DrawViTPose`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`

## 知识

覆盖率 **55%**（31/56）

**有卡**：`ImpactInt`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`WanVideoTextEmbedBridge`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoVAELoader`、`CLIPLoader`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`ImageConcatMulti`、`WanVideoDecode`、`DrawViTPose`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`PoseAndFaceDetection`、`WanVideoSampler`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoVAELoader
