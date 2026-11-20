---
name: unknown_workflow_video_lora_sampler_130
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.455071
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, ImageBatchExtendWithOverlap, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, ReplaceVideoLatentFrames, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/LongCat龙猫数字人I2V_2003272885085118465.json, 视频生成/图生视频/LongcatAvata-龙猫数字人I2V工作流_2003002229281964033.json, 视频生成/图生视频/内部测试0001_2006916502057918465.json, 视频生成/图生视频/对口型·超强悍_2010972591602798593.json, 视频生成/图生视频/龙猫数字人I2V工作流-Aiwood_2002473515242647553.json, 视频生成/图生视频/龙猫数字人I2V工作流_2002963374075965441.json, 视频生成/图生视频/龙猫数字人i2V工作流-长视频_2002719274244423682.json, 视频生成/文生视频/LongCat Avatar 长视频工作流_2003655756962512897.json, 视频生成/文生视频/LongCat avatar龙猫数字人文生视频对口型版_2002695647604162562.json, 视频生成/文生视频/LongCat+文生视频数字人_2002936278276534273.json, 视频生成/文生视频/LongCat-Video-Avatar数字人图生视频长视频_2003091574424764418.json, 视频生成/文生视频/LongCat-Video-Avatar数字人文生视频长视频_2003091459949699074.json, 视频生成/文生视频/LongCatAvatar_长时数字人工作流_2004810996587921409.json, 视频生成/文生视频/龙猫数字人文生视频对口型版（LongCat avatar 生产力版）_2009631986461188098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_130

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/LongCat龙猫数字人I2V_2003272885085118465.json、视频生成/图生视频/LongcatAvata-龙猫数字人I2V工作流_2003002229281964033.json、视频生成/图生视频/内部测试0001_2006916502057918465.json、视频生成/图生视频/对口型·超强悍_2010972591602798593.json、视频生成/图生视频/龙猫数字人I2V工作流-Aiwood_2002473515242647553.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageBatchExtendWithOverlap`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `ReplaceVideoLatentFrames`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 13/14 个有
- `GetNode` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `INTConstant` —— 12/14 个有
- `ImageResizeKJv2` —— 10/14 个有
- `LoadImage` —— 10/14 个有
- `PreviewAudio` —— 5/14 个有
- `DownloadAndLoadWav2VecModel` —— 4/14 个有
- `EmptyLatentImage` —— 4/14 个有
- `GetLatentRangeFromBatch` —— 4/14 个有
- `Int` —— 2/14 个有
- `Text` —— 2/14 个有
- `Float` —— 1/14 个有
- `LoadImageFromPath` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `RH_Nano_Banana2_Image2Image` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `ZML_ImageSelectorNode` —— 1/14 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/14 个有
- `easy indexTTSGenerateSimple` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
