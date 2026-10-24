---
name: unknown_workflow_video_lora_sampler_284
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.446143
common_nodes: [CLIPVisionLoader, FloatConstant, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, ReplaceVideoLatentFrames, SetNode, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [图片生成/图生图/LongCatAvatar_龙猫数字人-文生图_2002914137871118338.json, 图片生成/文生图/内部测试0001_2006740333874384898.json, 视频生成/图生视频/LongCat Video Avatar数字人图生视频V4_2002585439628345345.json, 视频生成/图生视频/LongCat+数字人对口型_2002677838857793538.json, 视频生成/图生视频/LongCat-Video-Avatar1.5多图分镜数字人_2059649854489583618.json, 视频生成/图生视频/LongCat-Video-Avatar1.5数字人视频_2059162387521032194.json, 视频生成/图生视频/内部测试0001_2006916502057918465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_284

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LongCatAvatar_龙猫数字人-文生图_2002914137871118338.json、图片生成/文生图/内部测试0001_2006740333874384898.json、视频生成/图生视频/LongCat Video Avatar数字人图生视频V4_2002585439628345345.json、视频生成/图生视频/LongCat+数字人对口型_2002677838857793538.json、视频生成/图生视频/LongCat-Video-Avatar1.5多图分镜数字人_2059649854489583618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `ReplaceVideoLatentFrames`
- `SetNode`
- `TrimAudioDuration`
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
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `DownloadAndLoadWav2VecModel` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `MultiTalkWav2VecEmbeds` —— 5/7 个有
- `Float` —— 4/7 个有
- `PreviewAudio` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `Int` —— 3/7 个有
- `ForLoopClose` —— 2/7 个有
- `ForLoopOpen` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `LongCatAvatarWhisperEmbeds` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `RH_Nano_Banana2_Image2Image` —— 2/7 个有
- `SaveAudio` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `Text Load Line From File` —— 2/7 个有
- `WhisperModelLoader` —— 2/7 个有
- `ZML_ImageSelectorNode` —— 2/7 个有
- `easy convertAnything` —— 2/7 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/7 个有
- `easy indexTTSGenerateSimple` —— 2/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `VHS_GetImageCount` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
