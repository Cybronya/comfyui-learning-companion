---
name: unknown_workflow_video_sampler_clip_39
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.669846
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadAudio, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json, 数字人/数字人/LTX2.3数字人_2046490310024372225.json, 数字人/数字人/LTX2.3数字人【 超稳版 + 无字幕 】_2046462637571051521.json, 视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json, 视频生成/图生视频/LTX-2一键稳定生成数字人制作表情口型同步视频对口型对嘴型音频图片生成数字人视频_2014350317235736578.json, 视频生成/图生视频/LTX-2图生视频：上传歌曲MP3，一键生成MV音乐视频！_2013887364019527681.json, 视频生成/图生视频/LTX-2文生视频数字人说话唱歌音频加文本生成_2015583679321477122.json, 视频生成/图生视频/LTX-2高效数字人生成：一键创建实时口型同步视频，支持对嘴型音频图片视频数字人视频_2017463016526192641.json, 视频生成/图生视频/LTX2.3稳定版数字人（新版模型）_2043896242345877506.json, 视频生成/图生视频/LTX2.3稳定版数字人（新版模型）_2046132388467580929.json, 视频生成/图生视频/LTX2.3稳定版数字人（最新版模型）_2044579812215361538.json, 视频生成/图生视频/【阿良绘】LTX2.3数字人 _ 更新版本（高质版）_2044304245054246914.json, 视频生成/文生视频/Ltx-2蒸馏对口型_2018224320958439425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/LTX2.3-数字人-Distilled-1.1-蒸馏稳定版-避免字幕-数字人-对口型_2045492864917970946.json、数字人/数字人/LTX2.3数字人_2046490310024372225.json、数字人/数字人/LTX2.3数字人【 超稳版 + 无字幕 】_2046462637571051521.json、视频生成/图生视频/LTX-2.3首尾帧+语音数字人_2036654957595725826.json、视频生成/图生视频/LTX-2一键稳定生成数字人制作表情口型同步视频对口型对嘴型音频图片生成数字人视频_2014350317235736578.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 12/13 个有
- `GetNode` —— 12/13 个有
- `LTXVAudioVAEDecode` —— 12/13 个有
- `LTXVImgToVideoInplace` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `SimpleCalculatorKJ` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `INTConstant` —— 11/13 个有
- `LTXVEmptyLatentAudio` —— 11/13 个有
- `LTXVPreprocess` —— 11/13 个有
- `GetImageSize` —— 10/13 个有
- `LoraLoaderModelOnly` —— 10/13 个有
- `DualCLIPLoader` —— 9/13 个有
- `LTX2SamplingPreviewOverride` —— 8/13 个有
- `LTX2_NAG` —— 8/13 个有
- `CR Text` —— 7/13 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 7/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/13 个有
- `LTXVChunkFeedForward` —— 6/13 个有
- `LTXVLatentUpsampler` —— 6/13 个有
- `LTXVScheduler` —— 6/13 个有
- `LatentUpscaleModelLoader` —— 6/13 个有
- `SaveAudio` —— 6/13 个有
- `VAEDecodeTiled` —— 6/13 个有
- `DualCLIPLoaderGGUF` —— 5/13 个有
- `ImageResizeKJv2` —— 5/13 个有
- `ImageScaleBy` —— 5/13 个有
- `ResizeImagesByLongerEdge` —— 5/13 个有
- `SimpleMath+` —— 5/13 个有
- `UnetLoaderGGUF` —— 5/13 个有
- `PathchSageAttentionKJ` —— 4/13 个有
- `Int` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `Audio Duration (mtb)` —— 1/13 个有
- `AudioInfo` —— 1/13 个有
- `AudioInfoNode` —— 1/13 个有
- `CustomAddLabel` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `ImageConcatMulti` —— 1/13 个有
- `LTX2AudioLatentNormalizingSampling` —— 1/13 个有
- `LTXVImgToVideoInplaceKJ` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `ResizeImageMaskNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 11 | 94% |
| 高度 | 25 | 24 - 25 | 11 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，11 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 24 - 25，11 个样本，取值集中（一致性 98%）
