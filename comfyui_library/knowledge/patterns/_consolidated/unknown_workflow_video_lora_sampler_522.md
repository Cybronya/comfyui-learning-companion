---
name: unknown_workflow_video_lora_sampler_522
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.648
common_nodes: [DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json, 视频生成/图生视频/动作完美迁移-Wan Video_2009487877079568385.json, 视频生成/图生视频/最新SteadyDancer动作迁移美女跳舞_1995812205289410562.json, 视频生成/图生视频/（高精度版）SteadyDancer动作迁移_1999818280472899586.json, 视频生成/图生视频/💃人物跳舞专版优化 熊部_人物动态增强💃_2009443481458057217.json, 视频生成/文生视频/SteadyDancer一张人物照片 + 一段姿态（骨架） → 生成一个动作流畅、长得像、不抖的动画视频_1995759327522721794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_522

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/SteadyDancer视频动作迁移【1.0】_1995877090840961026.json、视频生成/图生视频/动作完美迁移-Wan Video_2009487877079568385.json、视频生成/图生视频/最新SteadyDancer动作迁移美女跳舞_1995812205289410562.json、视频生成/图生视频/（高精度版）SteadyDancer动作迁移_1999818280472899586.json、视频生成/图生视频/💃人物跳舞专版优化 熊部_人物动态增强💃_2009443481458057217.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `OnnxDetectionModelLoader` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `WanVideoBlockSwap` —— 4/6 个有
- `WanVideoSetBlockSwap` —— 4/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `easy int` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `Int` —— 2/6 个有
- `ImpactInt` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `VHS_VideoInfo` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `easy positive` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
