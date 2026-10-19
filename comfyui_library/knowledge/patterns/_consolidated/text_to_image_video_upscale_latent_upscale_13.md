---
name: text_to_image_video_upscale_latent_upscale_13
type: Text To Image
frequency: 5
level: strong
coverage: 0.833
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json, 数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json, 数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json, 视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json, 视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json、数字人/数字人/ltx2.5数字人生成工作流音频驱动对口型_2088197298856751105.json、数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json、视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json、视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `LTXAVTextEncoderLoader` —— 4/5 个有
- `LTXVAudioVAELoader` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `ResizeImagesByLongerEdge` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `Int` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `RH_GetAudioDuration` —— 2/5 个有
- `1hew_AudioDuration` —— 1/5 个有
- `AudioDuration_wan` —— 1/5 个有
- `AudioPad` —— 1/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `DF_Int_to_Float` —— 1/5 个有
- `ImageAndMaskResizeNode` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImageSharpen` —— 1/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `LTXVAudioVAEDecode` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `MelBandRoFormerModelLoader` —— 1/5 个有
- `MelBandRoFormerSampler` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `SoundFlow_GetLength` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
