---
name: unknown_workflow_video_upscale_latent_upscale_124
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.811
common_nodes: [AudioAdjustVolume, AudioCombine, AudioMerge, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentAudio, Evaluate Integers, GetImageSize, GoogleTranslateTextNode, ImageResizeKJv2, ImageScaleToTotalPixels, Int, JWInteger, JjkText, JoinStrings, KSampler, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadAudio, LoadImage, LoraLoaderModelOnly, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, MathExpression|pysssss, ModelSamplingSD3, PreviewAudio, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, Qwen3_VQA, RH_Captioner, RH_Translator, RandomNoise, RunningHub Deepcleaner, SamplerCustomAdvanced, SaveAudio, SetLatentNoiseMask, SetNode, ShowAnything|Mie, SimpleMath+, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecodeAudio, VAELoader, VAELoaderKJ, VHS_VideoCombine, WooshLoadFlow, WooshSample, WooshTextEncode, easy showAnything]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/adigital_combination.json_2072223926792581121.json, 视频生成/图生视频/digital_combination.json_2070335522396000257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_124

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/adigital_combination.json_2072223926792581121.json、视频生成/图生视频/digital_combination.json_2070335522396000257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioAdjustVolume`
- `AudioCombine`
- `AudioMerge`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentAudio`
- `Evaluate Integers`
- `GetImageSize`
- `GoogleTranslateTextNode`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Int`
- `JWInteger`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `Qwen3_VQA`
- `RH_Captioner`
- `RH_Translator`
- `RandomNoise`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SaveAudio`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowAnything|Mie`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `WooshLoadFlow`
- `WooshSample`
- `WooshTextEncode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy downloadIndexTTSAndLoadModel` —— 1/2 个有
- `easy indexTTSGenerateSimple` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 40 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 60 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 60，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
