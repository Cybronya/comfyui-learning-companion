---
name: image_to_image_lora_sampler_clip_17
type: Image To Image
frequency: 10
level: moderate
coverage: 0.7664
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DisableNoise, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, ImageResize+, InFluxModelSamplingPred, KSampler, LoadImage, LoraLoaderModelOnly, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, OutFluxModelSamplingPred, PrimitiveFloat, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader_Any, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json, 图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2077642667059666946.json, 图片生成/图生图/为什么你AI出的图总感觉_脏_？用这个一步救回来_2069996619147337729.json, 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2083490624929615873.json, 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2095782841480212482.json, 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2096074942369583105.json, 图片生成/图生图/去AI感，真实感放大：Krea重塑自然美学_2071416993240150018.json, 图片生成/图生图/商业级真实感放大最终章_1970132736906326018.json, 图片生成/图生图/商业级真实感放大最终章_2066849997286629378.json, 图片生成/图生图/通用放大终版_2072942349625413633.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json、图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2077642667059666946.json、图片生成/图生图/为什么你AI出的图总感觉_脏_？用这个一步救回来_2069996619147337729.json、图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2083490624929615873.json、图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2095782841480212482.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DisableNoise`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `ImageResize+`
- `InFluxModelSamplingPred`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `OutFluxModelSamplingPred`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader_Any`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `CR Text` —— 8/10 个有
- `Bounded Image Crop with Mask` —— 7/10 个有
- `ImageToMask` —— 7/10 个有
- `Int` —— 7/10 个有
- `KuwaharaBlur` —— 7/10 个有
- `LayerColor: Color of Shadow & Highlight` —— 7/10 个有
- `LayerColor: RGB` —— 7/10 个有
- `RHHiddenNodes` —— 7/10 个有
- `ResizeAndPadImage` —— 7/10 个有
- `ResizeImageMixlab` —— 7/10 个有
- `easy boolean` —— 7/10 个有
- `easy ifElse` —— 7/10 个有
- `Latent Noise Injection` —— 6/10 个有
- `UNETLoader` —— 6/10 个有
- `ModelSamplingAuraFlow` —— 5/10 个有
- `DisTorchPurgeVRAMV2` —— 4/10 个有
- `KSamplerAdvanced` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `llama_cpp_instruct_adv` —— 4/10 个有
- `llama_cpp_model_loader` —— 4/10 个有
- `AILab_QwenVL` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `ClipLoaderGGUF` —— 1/10 个有
- `DF_Integer` —— 1/10 个有
- `GrowMask` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `JoinImageWithAlpha` —— 1/10 个有
- `LayerMask: BiRefNetUltraV2` —— 1/10 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/10 个有
- `Upscale Model Loader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | sa_solver | - | 10 | 60% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 10 | 100% |
| 重绘幅度 | 1 | 0.28 - 1 | 10 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，10 个样本，一致性 60%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.28 - 1，10 个样本
- 高发问题（23/10 个样本）：Steps较低可能导致细节不足
