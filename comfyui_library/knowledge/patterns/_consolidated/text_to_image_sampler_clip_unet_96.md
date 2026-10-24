---
name: text_to_image_sampler_clip_unet_96
type: Text To Image
frequency: 7
level: weak
coverage: 0.962571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json, 图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json, 图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json, 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json, 图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json, 图片生成/文生图/Z-image-文生图（自用测试版）_2052717804557742081.json, 图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json、图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json、图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json、图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json、图片生成/文生图/Z-Image Turbo 文生图_2009309148017598465.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `ConditioningNoiseInjection` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LatentUpscale` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | 9 - 50 | 7 | 34% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 7 | 43% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 0.35 - 1 | 7 | 75% |
| 宽度 | 1080 | 1024 - 1920 | 7 | 72% |
| 高度 | 1504 | 1024 - 1920 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，观测区间 9 - 50，7 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，7 个样本
- 宽度 中位数 1080，观测区间 1024 - 1920，7 个样本
- 高度 中位数 1504，观测区间 1024 - 1920，7 个样本
