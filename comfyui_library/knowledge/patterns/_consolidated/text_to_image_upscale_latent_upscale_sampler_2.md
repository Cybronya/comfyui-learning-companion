---
name: text_to_image_upscale_latent_upscale_sampler_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.853667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LatentUpscaleBy, PreviewImage, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 双采_2073848581156589569.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2 双采_2073848581156589569.json、图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json、图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LatentUpscaleBy`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 2/3 个有
- `LoadLatent` —— 2/3 个有
- `SaveLatent` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `Image Compare (mtb)` —— 1/3 个有
- `SeedNode` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1536 | 3 | 80% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.54 | 0.54 - 0.55 | 3 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，3 个样本
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.54，观测区间 0.54 - 0.55，3 个样本，取值集中（一致性 99%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
