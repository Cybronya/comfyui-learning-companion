---
name: text_to_image_lora_sampler_clip_165
type: Text To Image
frequency: 7
level: moderate
coverage: 0.863429
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, easy isMaskEmpty, easy seed]
members: [图片生成/文生图/1986272605315485698.json, 图片生成/文生图/1989221367381889026.json, 图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json, 图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json, 图片生成/文生图/Krea2 人物LoRA测试—Taslim_2073325908940902401.json, 图片生成/文生图/Krea2+Turbo文生图（双采版）_2071171911891111938.json, 图片生成/文生图/Qwen-Image-2512 电影艺术照片_2011354812247445505.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_165

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1986272605315485698.json、图片生成/文生图/1989221367381889026.json、图片生成/文生图/A-14 Z-Image Turbo 特定风格 人像大作 文生图_2096961472139194369.json、图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json、图片生成/文生图/Krea2 人物LoRA测试—Taslim_2073325908940902401.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ResolutionSelector` —— 4/7 个有
- `PreviewImage` —— 3/7 个有
- `easy seed` —— 3/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `SaveLatent` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `easy isMaskEmpty` —— 2/7 个有
- `LayerUtility: ImageReel` —— 1/7 个有
- `LayerUtility: ImageReelComposit` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 7 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 43% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 960 - 2480 | 7 | 63% |
| 高度 | 1024 | 928 - 2480 | 7 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 43%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 2480，7 个样本
- 高度 中位数 1024，观测区间 928 - 2480，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy isMaskEmpty、easy seed
