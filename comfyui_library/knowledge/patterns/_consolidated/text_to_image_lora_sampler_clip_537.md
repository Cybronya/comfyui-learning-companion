---
name: text_to_image_lora_sampler_clip_537
type: Text To Image
frequency: 3
level: moderate
coverage: 0.678
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001-krea2t-zit-对比_2083174076629213186.json, 图片生成/文生图/Qwen image 2512文生图_2006878431128064001.json, 图片生成/文生图/千问文生图-加速高清放大_1988478559381577729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_537

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/001-krea2t-zit-对比_2083174076629213186.json、图片生成/文生图/Qwen image 2512文生图_2006878431128064001.json、图片生成/文生图/千问文生图-加速高清放大_1988478559381577729.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `Seed Everywhere` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 3 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 3 | 61% |
| 宽度 | 1280 | 1280 - 2048 | 3 | 76% |
| 高度 | 720 | 720 - 1536 | 3 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，3 个样本
- 宽度 中位数 1280，观测区间 1280 - 2048，3 个样本
- 高度 中位数 720，观测区间 720 - 1536，3 个样本
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
