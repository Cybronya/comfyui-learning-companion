---
name: text_to_image_sampler_clip_unet_107
type: Text To Image
frequency: 4
level: strong
coverage: 0.89225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image 文生图细节增强版_2015753448066650114.json, 图片生成/文生图/Z-Image-Turbo-BF16文生图_2078377958095544321.json, 图片生成/文生图/Z-Image（文生图）工作流_1993963189358493697.json, 图片生成/文生图/Z-image增强版_2005571137486680066.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image 文生图细节增强版_2015753448066650114.json、图片生成/文生图/Z-Image-Turbo-BF16文生图_2078377958095544321.json、图片生成/文生图/Z-Image（文生图）工作流_1993963189358493697.json、图片生成/文生图/Z-image增强版_2005571137486680066.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Int` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `GenerateNoise` —— 2/4 个有
- `LGNoiseInjectionLatent` —— 2/4 个有
- `easy promptList` —— 2/4 个有
- `Float` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LatentSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1140 | 720 - 1280 | 4 | 80% |
| 高度 | 1760 | 1280 - 1920 | 4 | 84% |
| 采样步数 | 10 | 9 - 12 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 4 | 92% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1140，观测区间 720 - 1280，4 个样本
- 高度 中位数 1760，观测区间 1280 - 1920，4 个样本，取值集中（一致性 84%）
- 采样步数 中位数 10，观测区间 9 - 12，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，4 个样本，取值集中（一致性 92%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
