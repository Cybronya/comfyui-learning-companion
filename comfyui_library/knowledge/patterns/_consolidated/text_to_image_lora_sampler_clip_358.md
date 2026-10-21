---
name: text_to_image_lora_sampler_clip_358
type: Text To Image
frequency: 2
level: weak
coverage: 0.771
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Clamp Value, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImpactSwitch, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RH_LLMAPI_NODE, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2, Seed_, TeaCache, Text Multiline, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [CR Clamp Value, CR Text Concatenate, LayerUtility: PurgeVRAM, Text Multiline, MathExpression|pysssss]
members: [图片生成/文生图/1952355100364877826.json, 图片生成/文生图/1952761780301983745.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_358

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1952355100364877826.json、图片生成/文生图/1952761780301983745.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Clamp Value`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `Seed_`
- `TeaCache`
- `Text Multiline`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Clamp Value、CR Text Concatenate、LayerUtility: PurgeVRAM、Text Multiline、MathExpression|pysssss
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
