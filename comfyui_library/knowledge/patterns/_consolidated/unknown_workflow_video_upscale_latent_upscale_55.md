---
name: unknown_workflow_video_upscale_latent_upscale_55
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.822571
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json, 数字人/数字人/数字人ltx2.5_2087564554460024834.json, 数字人/数字人/数字人稳定版LTX_2089442379878195202.json, 视频生成/图生视频/2035354663842746370.json, 视频生成/图生视频/2080250787086819330.json, 视频生成/图生视频/2041707361903058945.json, 视频生成/图生视频/2080251768956608514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json、数字人/数字人/数字人ltx2.5_2087564554460024834.json、数字人/数字人/数字人稳定版LTX_2089442379878195202.json、视频生成/图生视频/2035354663842746370.json、视频生成/图生视频/2080250787086819330.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
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
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `LTXAVTextEncoderLoader` —— 6/7 个有
- `LTXVAudioVAELoader` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PreviewAudio` —— 6/7 个有
- `LTX2_NAG` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `RTXVideoSuperResolution` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `RH_GetAudioDuration` —— 3/7 个有
- `1hew_AudioDuration` —— 2/7 个有
- `ImageSharpen` —— 2/7 个有
- `Int` —— 2/7 个有
- `MelBandRoFormerModelLoader` —— 2/7 个有
- `MelBandRoFormerSampler` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `SoundFlow_GetLength` —— 2/7 个有
- `TrimAudioDuration` —— 2/7 个有
- `AudioConcat` —— 1/7 个有
- `AudioCrop` —— 1/7 个有
- `CLIPLoader` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `LongCatVoiceCloneTTS` —— 1/7 个有
- `NormalizeAudioLoudness` —— 1/7 个有
- `PIP_StringConcatenation` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `Qwen3ASRLoader` —— 1/7 个有
- `Qwen3ASRTranscribe` —— 1/7 个有
- `RegexReplace` —— 1/7 个有
- `ReroutePrimitive|pysssss` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `UNETLoader` —— 1/7 个有
- `VAELoader` —— 1/7 个有
- `WhisperSTT` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.6 | 7 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.6，7 个样本，取值集中（一致性 84%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
