---
name: text_to_image_sampler_clip_unet_207
type: Text To Image
frequency: 3
level: moderate
coverage: 0.854333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE 质感人像（批量）_2096958018905788418.json, 图片生成/文生图/krea2 文生图_2071634483538915329.json, 图片生成/文生图/文生图基础款_2010012252333678593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE 质感人像（批量）_2096958018905788418.json、图片生成/文生图/krea2 文生图_2071634483538915329.json、图片生成/文生图/文生图基础款_2010012252333678593.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `CR Prompt List` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 3 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 768 - 1080 | 3 | 85% |
| 高度 | 1920 | 1024 - 1920 | 3 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1080，3 个样本，取值集中（一致性 85%）
- 高度 中位数 1920，观测区间 1024 - 1920，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
