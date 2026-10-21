---
name: text_to_image_video_lora_sampler_129
type: Text To Image
frequency: 5
level: strong
coverage: 0.8312
common_nodes: [AnySwitch, AudioConcat, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Bypasser (rgthree), GetImageRangeFromBatch, GetVideoComponents, Int, JjkText, KSampler, KSamplerSelect, LoadImage, LongTextToList, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3BlockCacheT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, Multi Text Merge, PreviewAny, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SDVN Any Show, SamplerCustomAdvanced, SaveVideo, String Replace (mtb), TTP_text_mix, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, solarL_SaveImagesToZip, string_util_StrLen, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3语音驱动数字人 VSA加速无限时长生成_2098299600871444481.json, 视频生成/图生视频/MiniMax-H3 ref2v无限长视频｜音频生成图生视频_2090433511164567553.json, 视频生成/图生视频/ref2v无限长视频｜MiniMax-H3音频图生视频生成_2090157020346413058.json, 视频生成/图生视频/ref2v无限长视频｜MiniMax-H3音频生成图生视频_2090535641066065922.json, 视频生成/图生视频/二采放大无限长视频生成 MiniMax H3 视频生视频图生视频_2094164202637320193.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3语音驱动数字人 VSA加速无限时长生成_2098299600871444481.json、视频生成/图生视频/MiniMax-H3 ref2v无限长视频｜音频生成图生视频_2090433511164567553.json、视频生成/图生视频/ref2v无限长视频｜MiniMax-H3音频图生视频生成_2090157020346413058.json、视频生成/图生视频/ref2v无限长视频｜MiniMax-H3音频生成图生视频_2090535641066065922.json、视频生成/图生视频/二采放大无限长视频生成 MiniMax H3 视频生视频图生视频_2094164202637320193.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `AnySwitch`
- `AudioConcat`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LongTextToList`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `Multi Text Merge`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SDVN Any Show`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `String Replace (mtb)`
- `TTP_text_mix`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `solarL_SaveImagesToZip`
- `string_util_StrLen`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `MiniMaxH3ImageToVideo` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `SpectrumApplyMiniMaxH3` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `Yuan_H3MotionContext` —— 4/5 个有
- `LoadVideo` —— 3/5 个有
- `MiniMaxH3ChainContext` —— 3/5 个有
- `MiniMaxH3ChainExternalVideo` —— 3/5 个有
- `Video Slice` —— 3/5 个有
- `Yuan_H3MotionContextTrim` —— 3/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `Krea2EditGroundedEncode` —— 1/5 个有
- `Krea2EditModelPatch` —— 1/5 个有
- `LTXVConcatAVLatent` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `MinimaxH3LatentUpscaler3D` —— 1/5 个有
- `Qwen3VL_Advanced` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `VRAM_Debug` —— 1/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
