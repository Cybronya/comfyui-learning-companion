---
name: image_to_image_lora_sampler_clip_89
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9268
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageConcatMulti, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/擦除画面中任何物品_1975502122869501954.json, 图片生成/文生图/【大炮工具】擦除画面中任何物品_1925115333550481410.json, 平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json, 平台全量/kontext 扩图LORA加强版_1942430308408963074.json, 平台全量/取衣去人(扩图后)换模特_1991395283084902402.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/擦除画面中任何物品_1975502122869501954.json、图片生成/文生图/【大炮工具】擦除画面中任何物品_1925115333550481410.json、平台全量/Flux.1-Fill-OneReward无损消除元素_1958473949078306818.json、平台全量/kontext 扩图LORA加强版_1942430308408963074.json、平台全量/取衣去人(扩图后)换模特_1991395283084902402.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 4/5 个有
- `InpaintModelConditioning` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `ModelSamplingFlux` —— 3/5 个有
- `easy int` —— 3/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `ReferenceLatent` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `ImpactImageBatchToImageList` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 5 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.41 - 1 | 5 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.41 - 1，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
