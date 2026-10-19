---
name: text_to_image_lora_sampler_clip_199
type: Text To Image
frequency: 4
level: moderate
coverage: 0.81975
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, easy isMaskEmpty, easy seed]
members: [图片生成/文生图/1986272605315485698.json, 图片生成/文生图/1989221367381889026.json, 图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json, 图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1986272605315485698.json、图片生成/文生图/1989221367381889026.json、图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json、图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 2/4 个有
- `SaveLatent` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy isMaskEmpty` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1536 | 960 - 2480 | 4 | 67% |
| 高度 | 1104 | 928 - 2480 | 4 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 960 - 2480，4 个样本
- 高度 中位数 1104，观测区间 928 - 2480，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy isMaskEmpty、easy seed
