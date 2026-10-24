---
name: text_to_image_sampler_clip_unet_155
type: Text To Image
frequency: 4
level: moderate
coverage: 0.89075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE 质感人像（批量）_2096958018905788418.json, 图片生成/文生图/krea2 文生图_2071634483538915329.json, 图片生成/文生图/文生图 Qwen Image 2512_2031964505944625153.json, 图片生成/文生图/文生图基础款_2010012252333678593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE 质感人像（批量）_2096958018905788418.json、图片生成/文生图/krea2 文生图_2071634483538915329.json、图片生成/文生图/文生图 Qwen Image 2512_2031964505944625153.json、图片生成/文生图/文生图基础款_2010012252333678593.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `CR Prompt List` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `QwenImageLatentAspectRatio` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 768 - 1728 | 4 | 70% |
| 高度 | 1920 | 1024 - 2368 | 4 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1728，4 个样本
- 高度 中位数 1920，观测区间 1024 - 2368，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
