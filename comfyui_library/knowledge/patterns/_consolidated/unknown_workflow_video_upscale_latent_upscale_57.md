---
name: unknown_workflow_video_upscale_latent_upscale_57
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.820667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json, 图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json, 数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json, 数字人/数字人/数字人ltx2.5_2087564554460024834.json, 数字人/数字人/数字人稳定版LTX_2089442379878195202.json, 视频生成/图生视频/LTX 2.3真人数字人口播｜LongCat声音克隆_2080250787086819330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_57

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json、图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json、数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json、数字人/数字人/数字人ltx2.5_2087564554460024834.json、数字人/数字人/数字人稳定版LTX_2089442379878195202.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage`
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
- `CheckpointLoaderSimple` —— 5/6 个有
- `LTXAVTextEncoderLoader` —— 5/6 个有
- `LTXVAudioVAELoader` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `PreviewAudio` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `RTXVideoSuperResolution` —— 3/6 个有
- `ResizeImageMaskNode` —— 3/6 个有
- `1hew_AudioDuration` —— 2/6 个有
- `ImageSharpen` —— 2/6 个有
- `RH_GetAudioDuration` —— 2/6 个有
- `AudioConcat` —— 1/6 个有
- `AudioCrop` —— 1/6 个有
- `AudioDuration_wan` —— 1/6 个有
- `AudioPad` —— 1/6 个有
- `CLIPLoader` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `IndexTTS2Run` —— 1/6 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/6 个有
- `LongCatVoiceCloneTTS` —— 1/6 个有
- `NormalizeAudioLoudness` —— 1/6 个有
- `PIP_StringConcatenation` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `Qwen3ASRLoader` —— 1/6 个有
- `Qwen3ASRTranscribe` —— 1/6 个有
- `RegexReplace` —— 1/6 个有
- `ReroutePrimitive|pysssss` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有
- `VHS_LoadAudioUpload` —— 1/6 个有
- `WhisperSTT` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.6 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.6，6 个样本，取值集中（一致性 83%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
