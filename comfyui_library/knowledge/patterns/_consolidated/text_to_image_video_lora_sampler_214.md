---
name: text_to_image_video_lora_sampler_214
type: Text To Image
frequency: 2
level: weak
coverage: 0.6095
common_nodes: [AudioConcat, BasicGuider, BlockSparseAttention, CLIPLoader, CLIPTextEncode, CM_FloatToInt, ColorTransfer, ComfyMathExpression, ComfySwitchNode, CreateVideo, EmptyAudio, EmptyLatentImage, Float, GetNode, GetVideoComponents, ImageAddNoise, ImageBatchMulti, ImageFromBatch, Int, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, MemoryManager, MiniMaxH3AddGuide, MiniMaxH3PromptEnhancerT8, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaDropdown, PreviewAny, PreviewAudio, RH_IndexTTS25_Loader, RH_IndexTTS25_Synthesize, RandomNoise, RepeatImageBatch, ResizeShortestToNode, ResolutionSelector, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, StringMergeNode, StringToNumber, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VideoFrameSample, VideoTemporalCrop, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMaxH3综合工作流 数字人替换动作迁移长视频工具_2113707746108461057.json, 数字人/数字人/MinimaxH3综合工作流｜数字人人物替换动作迁移断点续接_2113536562838466562.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_214

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/MiniMaxH3综合工作流 数字人替换动作迁移长视频工具_2113707746108461057.json、数字人/数字人/MinimaxH3综合工作流｜数字人人物替换动作迁移断点续接_2113536562838466562.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `ColorTransfer`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `EmptyAudio`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `GetVideoComponents`
- `ImageAddNoise`
- `ImageBatchMulti`
- `ImageFromBatch`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MemoryManager`
- `MiniMaxH3AddGuide`
- `MiniMaxH3PromptEnhancerT8`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaDropdown`
- `PreviewAny`
- `PreviewAudio`
- `RH_IndexTTS25_Loader`
- `RH_IndexTTS25_Synthesize`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeShortestToNode`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `StringMergeNode`
- `StringToNumber`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoFrameSample`
- `VideoTemporalCrop`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
