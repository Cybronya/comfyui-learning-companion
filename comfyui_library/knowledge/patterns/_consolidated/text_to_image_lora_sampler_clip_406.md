---
name: text_to_image_lora_sampler_clip_406
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7552
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageAutoCrop V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/CG迷-最强的产品海报光影溶图工作流_1965017645324095489.json, 图片生成/文生图/产品生成海报打光溶图工作流_1962866539986923521.json, 平台全量/25.9.26 史上最强的产品海报光影溶图_1971557953935503361.json, 平台全量/kontext产品海报溶图_1991125202400575490.json, 平台全量/产品生成&海报打光溶图工作流_2054468835369078785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_406

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/CG迷-最强的产品海报光影溶图工作流_1965017645324095489.json、图片生成/文生图/产品生成海报打光溶图工作流_1962866539986923521.json、平台全量/25.9.26 史上最强的产品海报光影溶图_1971557953935503361.json、平台全量/kontext产品海报溶图_1991125202400575490.json、平台全量/产品生成&海报打光溶图工作流_2054468835369078785.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageAutoCrop V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/5 个有
- `CLIPLoader` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `TextEncodeQwenImageEdit` —— 2/5 个有
- `easy imageDetailTransfer` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 5 | 69% |
| 高度 | 1280 | 512 - 1280 | 5 | 61% |
| 采样步数 | 20 | 8 - 20 | 5 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.2 - 1 | 5 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，5 个样本
- 高度 中位数 1280，观测区间 512 - 1280，5 个样本
- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，5 个样本，取值分散，一致性仅 42%
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
