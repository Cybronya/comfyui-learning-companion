---
name: unknown_workflow_video_lora_sampler_819
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.551
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageResizeKJv2, Int, LoadImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, Primitive integer [Crystools], SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoVAELoader, ZML_AnyTypeSwitchFive, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, easy sam3VideoSegmentation]
problems: []
missing: []
members: [视频生成/图生视频/2048980034509086721.json, 视频生成/图生视频/2067889293686820865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_819

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2048980034509086721.json、视频生成/图生视频/2067889293686820865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `ZML_AnyTypeSwitchFive`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `easy sam3VideoSegmentation`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有
- `YOLOModelLoader` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy sam3GetObjectIds` —— 1/2 个有
- `easy sam3Visualization` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
