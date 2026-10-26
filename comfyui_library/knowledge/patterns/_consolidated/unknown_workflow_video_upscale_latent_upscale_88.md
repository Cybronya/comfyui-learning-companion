---
name: unknown_workflow_video_upscale_latent_upscale_88
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.83375
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, PathchSageAttentionKJ, PreviewAudio, PrimitiveBoolean, RTXVideoSuperResolution, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/批量视频-测试_2080195859542798337.json, 数字人/数字人/数字人ltx2.5_2087564554460024834.json, 数字人/数字人/数字人稳定版LTX_2089442379878195202.json, 视频生成/图生视频/LTX 2.3真人数字人口播｜LongCat声音克隆_2080250787086819330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_88

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/批量视频-测试_2080195859542798337.json、数字人/数字人/数字人ltx2.5_2087564554460024834.json、数字人/数字人/数字人稳定版LTX_2089442379878195202.json、视频生成/图生视频/LTX 2.3真人数字人口播｜LongCat声音克隆_2080250787086819330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PrimitiveBoolean`
- `RTXVideoSuperResolution`
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
- `CheckpointLoaderSimple` —— 3/4 个有
- `LTXAVTextEncoderLoader` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `1hew_AudioDuration` —— 2/4 个有
- `AudioCrop` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `LongCatVoiceCloneTTS` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `NormalizeAudioLoudness` —— 2/4 个有
- `Qwen3ASRLoader` —— 2/4 个有
- `Qwen3ASRTranscribe` —— 2/4 个有
- `RH_GetAudioDuration` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `AudioBeforeAfterSilence` —— 1/4 个有
- `AudioConcat` —— 1/4 个有
- `CLIPLoader` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `HeartMuLa_Transcribe` —— 1/4 个有
- `PIP_StringConcatenation` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `Qwen3TTSModelLoader` —— 1/4 个有
- `Qwen3TTSVoiceClone` —— 1/4 个有
- `RegexReplace` —— 1/4 个有
- `ReroutePrimitive|pysssss` —— 1/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `VAELoader` —— 1/4 个有
- `WhisperSTT` —— 1/4 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/4 个有
- `easy indexTTSGenerateSimple` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.6 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.6，4 个样本，取值集中（一致性 81%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
