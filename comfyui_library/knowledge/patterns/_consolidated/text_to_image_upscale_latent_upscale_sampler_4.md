---
name: text_to_image_upscale_latent_upscale_sampler_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.924333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, KSampler, LatentUpscaleBy, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 文生图双采样4K版_2092280334065946625.json, 图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json, 平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2 文生图双采样4K版_2092280334065946625.json、图片生成/文生图/Krea2｜三段式渲染文生图_2072217224156377090.json、平台全量/Krea2 Two-Stage HD Refinement_2072998797275602944.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LatentUpscaleBy`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Float` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 3 | 89% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |
| 采样步数 | 8 | 6 - 8 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 0.45 - 1 | 3 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，3 个样本
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
