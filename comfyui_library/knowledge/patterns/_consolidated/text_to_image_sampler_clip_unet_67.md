---
name: text_to_image_sampler_clip_unet_67
type: Text To Image
frequency: 11
level: moderate
coverage: 0.916364
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image增强版_2005571137486680066.json, 图片生成/文生图/Z-image文生图工作流_2075475394177880066.json, 图片生成/文生图/wanxia_2086138759858450434.json, 图片生成/文生图/z-image文生图工作流_2001830276877697026.json, 图片生成/文生图/z-image文生图工作流_2002604407730630657.json, 图片生成/文生图/z-image文生图工作流_2009919536497168386.json, 图片生成/文生图/人物生成（自用）_2094050883234521090.json, 图片生成/文生图/千问大模型文生图工作流_1959919853350105089.json, 图片生成/文生图/太猛了！Z-image文生图新王-支持中文！_1995051018658492417.json, 图片生成/文生图/文生图-boogu_turbo-模板_2090689514200195074.json, 图片生成/文生图/阿清的偶像捏脸工作流_2057382985531478018.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Z-image增强版_2005571137486680066.json、图片生成/文生图/Z-image文生图工作流_2075475394177880066.json、图片生成/文生图/wanxia_2086138759858450434.json、图片生成/文生图/z-image文生图工作流_2001830276877697026.json、图片生成/文生图/z-image文生图工作流_2002604407730630657.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `easy promptList` —— 8/11 个有
- `INTConstant` —— 2/11 个有
- `Image Comparer (rgthree)` —— 2/11 个有
- `GenerateNoise` —— 1/11 个有
- `LGNoiseInjectionLatent` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 904 - 1600 | 11 | 81% |
| 高度 | 1536 | 768 - 1920 | 11 | 75% |
| 采样步数 | 9 | 4 - 35 | 11 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 33% |
| 采样算法 | euler | - | 11 | 82% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 904 - 1600，11 个样本，取值集中（一致性 81%）
- 高度 中位数 1536，观测区间 768 - 1920，11 个样本
- 采样步数 中位数 9，观测区间 4 - 35，11 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，11 个样本，一致性 82%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
