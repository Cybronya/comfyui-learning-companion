---
name: unknown_workflow_video_lora_sampler_83
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.420824
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchExtendWithOverlap, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, ReplaceVideoLatentFrames, SetNode, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LongCat-Video-Avatar大模型来了！上传1张照片+1段录音，轻松生成高质量数字人视频！_2004069109543411713.json, 视频生成/图生视频/LongCat-Video-Avatar数字人_2005920919849758721.json, 视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json, 视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json, 视频生成/图生视频/LongCatAvatar美团龙猫图片生成唱歌等数字人视频数字人图生视频_2003503610359103489.json, 视频生成/图生视频/LongCat龙猫数字人I2V_2003272885085118465.json, 视频生成/图生视频/LongcatAvata-龙猫数字人I2V工作流_2003002229281964033.json, 视频生成/图生视频/对口型·超强悍_2010972591602798593.json, 视频生成/图生视频/龙猫数字人I2V工作流-Aiwood_2002473515242647553.json, 视频生成/图生视频/龙猫数字人I2V工作流_2002963374075965441.json, 视频生成/图生视频/龙猫数字人i2V工作流-长视频_2002719274244423682.json, 视频生成/文生视频/LongCat Avatar 长视频工作流_2003655756962512897.json, 视频生成/文生视频/LongCat avatar龙猫数字人文生视频对口型版_2002695647604162562.json, 视频生成/文生视频/LongCat+文生视频数字人_2002936278276534273.json, 视频生成/文生视频/LongCat-Video-Avatar数字人图生视频长视频_2003091574424764418.json, 视频生成/文生视频/LongCat-Video-Avatar数字人文生视频长视频_2003091459949699074.json, 视频生成/文生视频/LongCatAvatar_长时数字人工作流_2004810996587921409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/LongCat-Video-Avatar大模型来了！上传1张照片+1段录音，轻松生成高质量数字人视频！_2004069109543411713.json、视频生成/图生视频/LongCat-Video-Avatar数字人_2005920919849758721.json、视频生成/图生视频/LongCatAvatar_audio_image_to_video_auto-extend_2004216271933767681.json、视频生成/图生视频/LongCatAvatar_audio_image_to_video_example_Kijai_2004028313129656322.json、视频生成/图生视频/LongCatAvatar美团龙猫图片生成唱歌等数字人视频数字人图生视频_2003503610359103489.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkWav2VecEmbeds`
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

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 16/17 个有
- `Wav2VecModelLoader` —— 16/17 个有
- `INTConstant` —— 15/17 个有
- `WanVideoTorchCompileSettings` —— 15/17 个有
- `ImageResizeKJv2` —— 14/17 个有
- `LoadImage` —— 14/17 个有
- `DownloadAndLoadWav2VecModel` —— 9/17 个有
- `EmptyLatentImage` —— 3/17 个有
- `GetLatentRangeFromBatch` —— 3/17 个有
- `Int` —— 3/17 个有
- `PreviewAudio` —— 3/17 个有
- `Text` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `Float` —— 1/17 个有
- `IndexTTS2Run` —— 1/17 个有
- `Label (rgthree)` —— 1/17 个有
- `LoadImageFromPath` —— 1/17 个有
- `MathExpression|pysssss` —— 1/17 个有
- `MemoryCleaner` —— 1/17 个有
- `MultiLinePromptIndex` —— 1/17 个有
- `PrimitiveFloat` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `SaveAudioMP3` —— 1/17 个有
- `easy forLoopEnd` —— 1/17 个有
- `easy forLoopStart` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
