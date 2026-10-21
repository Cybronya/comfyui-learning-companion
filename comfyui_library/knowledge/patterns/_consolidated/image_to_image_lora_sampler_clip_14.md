---
name: image_to_image_lora_sampler_clip_14
type: Image To Image
frequency: 2
level: weak
coverage: 0.5945
common_nodes: [BasicGuider, BasicScheduler, Bounded Image Crop with Mask, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DisableNoise, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Image Comparer (rgthree), ImageResize+, ImageToMask, InFluxModelSamplingPred, Int, KSampler, KuwaharaBlur, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, LoadImage, LoraLoaderModelOnly, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, OutFluxModelSamplingPred, PreviewImage, PrimitiveFloat, RHHiddenNodes, ReferenceLatent, ResizeAndPadImage, ResizeImageMixlab, SamplerCustomAdvanced, SaveImage, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageColorMatch, easy int]
problems: [Steps较低可能导致细节不足]
missing: [Bounded Image Crop with Mask, CR Text, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, easy boolean, easy cleanGpuUsed, easy imageColorMatch, easy int, ImageResize+, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: PurgeVRAM V2, Latent Noise Injection, Upscale Model Loader]
members: [图片生成/图生图/2071416993240150018.json, 图片生成/图生图/2072942349625413633.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2071416993240150018.json、图片生成/图生图/2072942349625413633.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bounded Image Crop with Mask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DisableNoise`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageToMask`
- `InFluxModelSamplingPred`
- `Int`
- `KSampler`
- `KuwaharaBlur`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: RGB`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `ReferenceLatent`
- `ResizeAndPadImage`
- `ResizeImageMixlab`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageColorMatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `DisTorchPurgeVRAMV2` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `JoinImageWithAlpha` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 0.64 | - | 2 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 0.64，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Bounded Image Crop with Mask、CR Text、LayerColor: Color of Shadow & Highlight、LayerColor: RGB、easy boolean
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
