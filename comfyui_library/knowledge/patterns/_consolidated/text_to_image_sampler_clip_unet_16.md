---
name: text_to_image_sampler_clip_unet_16
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9365
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, Power Lora Loader (rgthree)]
members: [图片生成/文生图/1955085568910790658.json, 图片生成/文生图/1955863541137985538.json, 图片生成/文生图/1985898941021659137.json, 图片生成/文生图/👾怪獸-Krea2 文生图-人物设计多lora选择 👾_2102397348696645634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1955085568910790658.json、图片生成/文生图/1955863541137985538.json、图片生成/文生图/1985898941021659137.json、图片生成/文生图/👾怪獸-Krea2 文生图-人物设计多lora选择 👾_2102397348696645634.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ConditioningKrea2Rebalance` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `FluxResolutionNode` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Power Lora Loader (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 768 - 1080 | 4 | 87% |
| 高度 | 1324 | 1024 - 1920 | 4 | 77% |
| 采样步数 | 12 | 4 - 25 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 768 - 1080，4 个样本，取值集中（一致性 87%）
- 高度 中位数 1324，观测区间 1024 - 1920，4 个样本
- 采样步数 中位数 12，观测区间 4 - 25，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Power Lora Loader (rgthree)
