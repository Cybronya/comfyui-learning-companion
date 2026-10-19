---
name: unknown_workflow_video_lora_sampler_686
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.579
common_nodes: [BlockifyMask, CLIPVisionLoader, CR Text, DrawMaskOnImage, EmptyImage, GetImageSizeAndCount, GetNode, GrowMask, ImageConcatMulti, ImageResizeKJv2, ImpactInt, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1975554150689845250.json, 视频生成/图生视频/1975078914978656258.json, 视频生成/图生视频/1969652122914594818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_686

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1975554150689845250.json、视频生成/图生视频/1975078914978656258.json、视频生成/图生视频/1969652122914594818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Text`
- `DrawMaskOnImage`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactInt`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `OnnxDetectionModelLoader` —— 2/3 个有
- `PoseAndFaceDetection` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DownloadAndLoadWav2VecModel` —— 1/3 个有
- `FaceMaskFromPoseKeypoints` —— 1/3 个有
- `ImageCropByMaskAndResize` —— 1/3 个有
- `MultiTalkModelLoader` —— 1/3 个有
- `MultiTalkWav2VecEmbeds` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
