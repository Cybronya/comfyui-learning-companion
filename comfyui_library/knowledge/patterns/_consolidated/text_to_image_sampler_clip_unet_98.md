---
name: text_to_image_sampler_clip_unet_98
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json, 图片生成/文生图/Anima正式版-文生图工作流_2084627398477303810.json, 图片生成/文生图/Krea2 文生图_2071762623535861761.json, 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_98

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json、图片生成/文生图/Anima正式版-文生图工作流_2084627398477303810.json、图片生成/文生图/Krea2 文生图_2071762623535861761.json、图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json）

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
- `ConditioningZeroOut` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `PDRatioSelector` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 4 | 59% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 4 | 59% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1052 | 1024 - 1080 | 4 | 97% |
| 高度 | 1728 | 1024 - 1920 | 4 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 1024 - 1080，4 个样本，取值集中（一致性 97%）
- 高度 中位数 1728，观测区间 1024 - 1920，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
