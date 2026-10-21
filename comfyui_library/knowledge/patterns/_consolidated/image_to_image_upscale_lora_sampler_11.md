---
name: image_to_image_upscale_lora_sampler_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.683
common_nodes: [AILab_QwenVL, AdvancedLyingSigmaSampler, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DisableNoise, FlipSigmas, Float, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Get resolution [Crystools], Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, InFluxModelSamplingPred, JWFloat, KSampler, KSamplerSelect, Latent Noise Injection, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, OutFluxModelSamplingPred, PreviewImage, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UNETLoader_Any, UltimateSDUpscaleCustomSample, Upscale Model Loader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy int]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: PurgeVRAM V2, SimpleMath+, easy cleanGpuUsed, easy imageColorMatch, easy int, Get resolution [Crystools], ImageResize+, Latent Noise Injection, Upscale Model Loader, LayerColor: RGB]
members: [图片生成/图生图/2055160504007569410.json, 图片生成/图生图/2059536367583059970.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2055160504007569410.json、图片生成/图生图/2059536367583059970.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `AdvancedLyingSigmaSampler`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DisableNoise`
- `FlipSigmas`
- `Float`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Get resolution [Crystools]`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InFluxModelSamplingPred`
- `JWFloat`
- `KSampler`
- `KSamplerSelect`
- `Latent Noise Injection`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UNETLoader_Any`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LayerColor: RGB` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3.5 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.7 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM V2、SimpleMath+、easy cleanGpuUsed、easy imageColorMatch
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
