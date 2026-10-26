---
name: unknown_workflow_video_lora_sampler_796
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6925
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Prompt Text, CastAnyToIntStringFloat, ConditioningZeroOut, FB_Qwen3TTSVoiceClone, GetImageSizeAndCount, INTConstant, ImageFromBatch+, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, RH_GetAudioDuration, SaveAudio, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_Unbatch, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoMagCache, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, WhisperSTT, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/03-10-15-WAN2.1-数字人-多参融合-skyreels+infineteTalk_2019304591753482241.json, 视频生成/图生视频/多参跨模态音画同步脸部参考图生视频V1（全自动版）_2017489851356028929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_796

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/03-10-15-WAN2.1-数字人-多参融合-skyreels+infineteTalk_2019304591753482241.json、视频生成/图生视频/多参跨模态音画同步脸部参考图生视频V1（全自动版）_2017489851356028929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

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
- `INTConstant`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `RH_GetAudioDuration`
- `SaveAudio`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_Unbatch`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WhisperSTT`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有

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
