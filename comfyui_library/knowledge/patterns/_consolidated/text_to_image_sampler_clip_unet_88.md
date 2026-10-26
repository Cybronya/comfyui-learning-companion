---
name: text_to_image_sampler_clip_unet_88
type: Text To Image
frequency: 8
level: moderate
coverage: 0.95175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE-TURBO：文生图 （api 专用）_2034271324402622466.json, 图片生成/文生图/Z-Image Re-Turbo_2073289018476941314.json, 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json, 图片生成/文生图/Z-Image-Base文生图批量生图_2018255513896624130.json, 图片生成/文生图/Z-Image-Base高质量多细节文生图_2015636535781101570.json, 图片生成/文生图/Z-image-Base文生图（turbo对比)_2018000039255216130.json, 图片生成/文生图/Z-image-distall-patch文生图_2002052529569579010.json, 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE-TURBO：文生图 （api 专用）_2034271324402622466.json、图片生成/文生图/Z-Image Re-Turbo_2073289018476941314.json、图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json、图片生成/文生图/Z-Image-Base文生图批量生图_2018255513896624130.json、图片生成/文生图/Z-Image-Base高质量多细节文生图_2015636535781101570.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `easy promptLine` —— 4/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `ModelSamplingAuraFlow` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `ImpactInt` —— 1/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有
- `SeedGenerator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 8 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 8 | 45% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1144 | 1024 - 1920 | 8 | 73% |
| 高度 | 1472 | 1024 - 1920 | 8 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，8 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，8 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1144，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1472，观测区间 1024 - 1920，8 个样本
