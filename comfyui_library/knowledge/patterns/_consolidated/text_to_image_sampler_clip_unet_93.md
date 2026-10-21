---
name: text_to_image_sampler_clip_unet_93
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9628
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图art_2017930293285490690.json, 图片生成/文生图/Z-image文生图：超细腻写实质感+精准文字渲染_1994608742673096706.json, 图片生成/文生图/Z-image新王登基君临天下(文生图)_1993946984736292866.json, 图片生成/文生图/Z-image，文生图_1995081308172955649.json, 图片生成/文生图/Z-lmage-Turbo绘梦：我的AI圣诞海报_1994213789992157185.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image文生图art_2017930293285490690.json、图片生成/文生图/Z-image文生图：超细腻写实质感+精准文字渲染_1994608742673096706.json、图片生成/文生图/Z-image新王登基君临天下(文生图)_1993946984736292866.json、图片生成/文生图/Z-image，文生图_1995081308172955649.json、图片生成/文生图/Z-lmage-Turbo绘梦：我的AI圣诞海报_1994213789992157185.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `Int` —— 4/5 个有
- `ImpactSwitch` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `Text` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 512 - 1144 | 5 | 67% |
| 高度 | 1472 | 512 - 1920 | 5 | 52% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1144，5 个样本
- 高度 中位数 1472，观测区间 512 - 1920，5 个样本
