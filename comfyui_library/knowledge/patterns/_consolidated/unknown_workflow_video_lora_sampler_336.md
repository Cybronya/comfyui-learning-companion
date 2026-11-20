---
name: unknown_workflow_video_lora_sampler_336
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.443143
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FloatConstant, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, ReplaceVideoLatentFrames, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/LongCatAvatar_无限时长工作流_2006174789139959810.json, 数字人/数字人/LongCatAvatar丝滑全自动无限时长数字人_2021765346931249153.json, 数字人/数字人/LongCat数字人一键生成_2009171897438703617.json, 视频生成/图生视频/LongCat-Video-Avatar数字人_2005920919849758721.json, 视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json, 视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json, 视频生成/图生视频/LongCatAvatar美团龙猫图片生成唱歌等数字人视频数字人图生视频_2003503610359103489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_336

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/LongCatAvatar_无限时长工作流_2006174789139959810.json、数字人/数字人/LongCatAvatar丝滑全自动无限时长数字人_2021765346931249153.json、数字人/数字人/LongCat数字人一键生成_2009171897438703617.json、视频生成/图生视频/LongCat-Video-Avatar数字人_2005920919849758721.json、视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `ReplaceVideoLatentFrames`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `TrimAudioDuration` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `Wav2VecModelLoader` —— 4/7 个有
- `easy forLoopEnd` —— 4/7 个有
- `easy forLoopStart` —— 4/7 个有
- `Int` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `DF_Ceil` —— 1/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `Float` —— 1/7 个有
- `FloorNode` —— 1/7 个有
- `GetAudioDurationFromAudio` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy compare` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy isNone` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
