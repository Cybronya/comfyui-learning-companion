---
name: text_to_image_sampler_clip_unet_190
type: Text To Image
frequency: 3
level: strong
coverage: 0.979333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2-双采+放大_2077598774695907329.json, 图片生成/文生图/krea2的极致美学_2069777686637142018.json, 图片生成/文生图/zimage3.0 文生图_2046928615945801730.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2-双采+放大_2077598774695907329.json、图片生成/文生图/krea2的极致美学_2069777686637142018.json、图片生成/文生图/zimage3.0 文生图_2046928615945801730.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 2/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1024 - 1080 | 3 | 98% |
| 高度 | 1920 | 1280 - 1920 | 3 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1080，3 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1280 - 1920，3 个样本，取值集中（一致性 82%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
