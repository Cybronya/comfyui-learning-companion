---
key: 平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 浮云1.7_2008750095314980866.json
name: 【角色替换】Wan2.2-Animate-视频换脸+换装 浮云1.7_2008750095314980866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 浮云1.7_2008750095314980866.json
hash: 96f6dc45aafd1561
coverage: 0.565217
learned_at: 2026-11-14 01:25:21
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, SetNode, ImpactInt, ImpactInt, easy showAnything, ImageResizeKJv2, easy promptConcat, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, DrawViTPose, Reroute, PoseAndFaceDetection, SetNode, OnnxDetectionModelLoader, SetNode, VHS_VideoCombine, GetImageSizeAndCount, RH_LLMAPI_NODE, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoModelLoader, GetNode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, EmptyImage, SimpleMath+, easy showAnything, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, BlockifyMask, GrowMask, LayerMask: SegmentAnythingUltra V3, LayerMask: LoadSegmentAnythingModels, SetNode, VHS_VideoCombine, VHS_LoadVideo, ImpactInt, WanVideoSampler, CR Text, LoadImage]
patterns: []
missing: []
---

# 平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 浮云1.7_2008750095314980866.json

> 来源文件 `comfyui_library/workflows/平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 浮云1.7_2008750095314980866.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（69 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImpactInt`
- `ImpactInt`
- `easy showAnything`
- `ImageResizeKJv2`
- `easy promptConcat`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `Reroute`
- `PoseAndFaceDetection`
- `SetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `RH_LLMAPI_NODE`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `EmptyImage`
- `SimpleMath+`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: LoadSegmentAnythingModels`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImpactInt`
- `WanVideoSampler` ★核心
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **57%**（39/69）

**有卡**：`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImpactInt`、`ImageResizeKJv2`、`easy promptConcat`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`RH_LLMAPI_NODE`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`ImageConcatMulti`、`EmptyImage`、`SimpleMath+`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`LayerMask: SegmentAnythingUltra V3`、`LayerMask: LoadSegmentAnythingModels`、`VHS_LoadVideo`、`WanVideoSampler`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
