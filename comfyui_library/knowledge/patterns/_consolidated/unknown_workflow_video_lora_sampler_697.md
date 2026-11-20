---
name: unknown_workflow_video_lora_sampler_697
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.58825
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, Label (rgthree), LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/姿势迁移跳舞 支持不同身材—阿浩_2028718652761051138.json, 平台全量/🔥AI换人术新模型：SteadyDancer，把你变成魔术师表演“密室逃生”！_1996096106654318593.json, 视频生成/图生视频/跳舞 - SteadyDancer_2047836406218756098.json, 视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_697

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/姿势迁移跳舞 支持不同身材—阿浩_2028718652761051138.json、平台全量/🔥AI换人术新模型：SteadyDancer，把你变成魔术师表演“密室逃生”！_1996096106654318593.json、视频生成/图生视频/跳舞 - SteadyDancer_2047836406218756098.json、视频生成/文生视频/SteadyDancer 跳舞 支持不同身形比例_2019123719372808193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Label (rgthree)`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `PlaySound|pysssss` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `StringConcatenate` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `easy int` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `Bookmark (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
