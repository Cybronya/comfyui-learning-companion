---
name: unknown_workflow_video_lora_sampler_795
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.717
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Prompt Text, CastAnyToIntStringFloat, ConditioningZeroOut, FB_Qwen3TTSVoiceClone, GetImageSizeAndCount, ImageFromBatch+, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, RH_GetAudioDuration, SaveAudio, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WhisperSTT, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/03-10-14-WAN2.1-数字人-QwenTTS+InfiniteTal-V2V_2019338953819693058.json, 数字人/数字人/跨模态Qwen3 TTS+Infinite Talk脸部参考V2V数字人V1_2017494205395898369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_795

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/03-10-14-WAN2.1-数字人-QwenTTS+InfiniteTal-V2V_2019338953819693058.json、数字人/数字人/跨模态Qwen3 TTS+Infinite Talk脸部参考V2V数字人V1_2017494205395898369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CastAnyToIntStringFloat`
- `ConditioningZeroOut`
- `FB_Qwen3TTSVoiceClone`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `RH_GetAudioDuration`
- `SaveAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WhisperSTT`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Int` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SoulXPodcastGenerate` —— 1/2 个有
- `SoulXPodcastInputParser` —— 1/2 个有
- `SoulXPodcastLoader` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | dpmpp_sde | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
