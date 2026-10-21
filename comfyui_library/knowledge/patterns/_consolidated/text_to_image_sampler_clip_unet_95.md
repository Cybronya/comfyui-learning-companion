---
name: text_to_image_sampler_clip_unet_95
type: Text To Image
frequency: 5
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zimage_z-image文生图_1999490922389831681.json, 图片生成/文生图/⚡ Boogu-Turbo 极速高写实文生图_2068717870527369217.json, 图片生成/文生图/皮神-Zimage基础工作流_1996929661861040129.json, 图片生成/文生图/造相 Z-image 文生图_2073282210454659074.json, 图片生成/文生图/造相-Z-Image-Turo 文生图官方版_1993841938419957762.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/zimage_z-image文生图_1999490922389831681.json、图片生成/文生图/⚡ Boogu-Turbo 极速高写实文生图_2068717870527369217.json、图片生成/文生图/皮神-Zimage基础工作流_1996929661861040129.json、图片生成/文生图/造相 Z-image 文生图_2073282210454659074.json、图片生成/文生图/造相-Z-Image-Turo 文生图官方版_1993841938419957762.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `easy getNode` —— 1/5 个有
- `easy setNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 960 - 1920 | 5 | 71% |
| 高度 | 1280 | 1024 - 1920 | 5 | 73% |
| 采样步数 | 9 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 960 - 1920，5 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 9，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
