---
name: text_to_image_sampler_clip_unet_157
type: Text To Image
frequency: 4
level: moderate
coverage: 0.842
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-Base文生图（turbo对比)_2018000039255216130.json, 图片生成/文生图/Z-image-base文生图洗图自动化_2016501851377639425.json, 图片生成/文生图/Z-image文生图洗图自动化_1993872494906064897.json, 图片生成/文生图/阿里z-image文生图，洗图_1993976067994091521.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-Base文生图（turbo对比)_2018000039255216130.json、图片生成/文生图/Z-image-base文生图洗图自动化_2016501851377639425.json、图片生成/文生图/Z-image文生图洗图自动化_1993872494906064897.json、图片生成/文生图/阿里z-image文生图，洗图_1993976067994091521.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MaraScottIsEmptyOrNone_v1` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `easy int` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `SeedGenerator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 4 | 50% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3 | 4 | 52% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1144 | 4 | 95% |
| 高度 | 1536 | 1472 - 1536 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1144，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1536，观测区间 1472 - 1536，4 个样本，取值集中（一致性 98%）
