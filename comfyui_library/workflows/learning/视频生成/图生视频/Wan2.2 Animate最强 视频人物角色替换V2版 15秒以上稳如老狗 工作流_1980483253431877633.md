---
key: 视频生成/图生视频/Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json
name: Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json
hash: 3841766d08b9241e
coverage: 0.565217
learned_at: 2026-10-15 22:32:30
nodes: [GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, GetNode, GetNode, GetNode, SetNode, SimpleMath+, ImpactInt, ImpactInt, easy showAnything, ImageResizeKJv2, easy promptConcat, SetNode, SetNode, BlockifyMask, GetNode, SetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, GrowMask, VHS_VideoCombine, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, DrawViTPose, Reroute, PoseAndFaceDetection, SetNode, OnnxDetectionModelLoader, SetNode, VHS_VideoCombine, GetImageSizeAndCount, RH_LLMAPI_NODE, easy showAnything, WanVideoVAELoader, WanVideoLoraSelectMulti, WanVideoModelLoader, LoadImage, CR Text, VHS_LoadVideo, ImpactInt, GetNode, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, EmptyImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate最强 视频人物角色替换V2版 15秒以上稳如老狗 工作流_1980483253431877633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980483253431877633.json`

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
- `LoadImage`
- `CR Text`
- `VHS_LoadVideo`
- `ImpactInt`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `EmptyImage`

## 知识

覆盖率 **57%**（39/69）

**有卡**：`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SimpleMath+`、`ImpactInt`、`ImageResizeKJv2`、`easy promptConcat`、`BlockifyMask`、`DrawMaskOnImage`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`GrowMask`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`RH_LLMAPI_NODE`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`LoadImage`、`CR Text`、`VHS_LoadVideo`、`ImageConcatMulti`、`EmptyImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
