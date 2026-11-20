---
key: 平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 最强+视频人物角色替换_1981598271481225217.json
name: 【角色替换】Wan2.2-Animate-视频换脸+换装 最强+视频人物角色替换_1981598271481225217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 最强+视频人物角色替换_1981598271481225217.json
hash: 4187463e7b060240
coverage: 0.565217
learned_at: 2026-11-14 01:25:20
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, SetNode, SimpleMath+, ImpactInt, ImpactInt, easy showAnything, ImageResizeKJv2, easy promptConcat, SetNode, SetNode, BlockifyMask, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, GrowMask, VHS_VideoCombine, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, DrawViTPose, Reroute, PoseAndFaceDetection, SetNode, OnnxDetectionModelLoader, SetNode, VHS_VideoCombine, GetImageSizeAndCount, RH_LLMAPI_NODE, easy showAnything, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoModelLoader, CR Text, ImpactInt, GetNode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, EmptyImage, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 最强+视频人物角色替换_1981598271481225217.json

> 来源文件 `comfyui_library/workflows/平台全量/【角色替换】Wan2.2-Animate-视频换脸+换装 最强+视频人物角色替换_1981598271481225217.json`

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
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `easy showAnything`
- `ImageResizeKJv2`
- `easy promptConcat`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `GrowMask`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
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
- `easy showAnything`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `CR Text`
- `ImpactInt`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `EmptyImage`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **57%**（39/69）

**有卡**：`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SimpleMath+`、`ImpactInt`、`ImageResizeKJv2`、`easy promptConcat`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`GrowMask`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`RH_LLMAPI_NODE`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`CR Text`、`ImageConcatMulti`、`EmptyImage`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
