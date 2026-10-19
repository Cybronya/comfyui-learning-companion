---
name: unknown_workflow_video_lora_sampler_689
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.598667
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2047836406218756098.json, 视频生成/图生视频/1999818280472899586.json, 视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_689

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2047836406218756098.json、视频生成/图生视频/1999818280472899586.json、视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
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
- `AddLabel` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PrimitiveString` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
