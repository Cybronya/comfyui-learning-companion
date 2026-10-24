---
name: text_to_image_video_lora_sampler_225
type: Text To Image
frequency: 2
level: weak
coverage: 0.6935
common_nodes: [Anything Everywhere3, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, DF_Integer, EasyCache, EmptyImage, EmptyLatentImage, GetNode, H3SigmaRefiner, ImageCompositeMasked, InvertMask, JjkText, KSampler, KSamplerSelect, LayerMask: RmBgUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PathchSageAttentionKJ, Prompts Everywhere, SaveImage, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json, 视频生成/图生视频/视频编辑替换Minimax H3 Replace V2 场景替换方案_2105430795514114050.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_225

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/视频编辑替换Minimax H3 CharacterSwapLora 人物替换方案_2105429242321391618.json、视频生成/图生视频/视频编辑替换Minimax H3 Replace V2 场景替换方案_2105430795514114050.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `DF_Integer`
- `EasyCache`
- `EmptyImage`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `ImageCompositeMasked`
- `InvertMask`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: RmBgUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `Prompts Everywhere`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SelfLiftH3Sampler` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有

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
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
