---
name: unknown_workflow_video_lora_sampler_821
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.655
common_nodes: [AdaptiveWanVideoAnimateEmbeds, CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Muter (rgthree), Flux2Scheduler, GetImageSize, GetImageSizeAndCount, GetNode, ImageResizeKJv2, ImageScaleToTotalPixels, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SaveImage, SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2027375031759671298.json, 视频生成/图生视频/2017236160619220993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_821

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2027375031759671298.json、视频生成/图生视频/2017236160619220993.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AdaptiveWanVideoAnimateEmbeds`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Muter (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
