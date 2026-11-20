---
name: unknown_workflow_video_lora_sampler_606
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.66875
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/跳舞 - SteadyDancer_2047836406218756098.json, 视频生成/图生视频/（高精度版）SteadyDancer动作迁移_1999818280472899586.json, 视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json, 视频生成/文生视频/SteadyDancer一张人物照片 + 一段姿态（骨架） → 生成一个动作流畅、长得像、不抖的动画视频_1995759327522721794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_606

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/跳舞 - SteadyDancer_2047836406218756098.json、视频生成/图生视频/（高精度版）SteadyDancer动作迁移_1999818280472899586.json、视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json、视频生成/文生视频/SteadyDancer一张人物照片 + 一段姿态（骨架） → 生成一个动作流畅、长得像、不抖的动画视频_1995759327522721794.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `PrimitiveString` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `easy int` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `Bookmark (rgthree)` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
