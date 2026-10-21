---
name: text_to_image_sampler_clip_unet_74
type: Text To Image
frequency: 7
level: strong
coverage: 0.945571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json, 图片生成/文生图/z-image文生图_2094325413752426498.json, 图片生成/文生图/【极速版】Krea2 Trubo 美商极高文生图 V2_2098689048914259969.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099331628756725762.json, 图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099337911668924418.json, 图片生成/文生图/👾怪獸-Z-Image 文生图圣诞特集👾_1996136993329496065.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/z-image文生图+FlashVSR超清放大-简单直观方便新手研究学习_1996121050985512961.json、图片生成/文生图/z-image文生图_2094325413752426498.json、图片生成/文生图/【极速版】Krea2 Trubo 美商极高文生图 V2_2098689048914259969.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2098225838008389634.json、图片生成/文生图/【极速版】Krea2 Trubo美商极高文生图_2099331628756725762.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

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
- `LoraLoaderModelOnly` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `QZ_ResolutionPreset` —— 3/7 个有
- `FlashVSRNode` —— 1/7 个有
- `FluxGuidance` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1920 | 7 | 74% |
| 高度 | 1080 | 1024 - 1960 | 7 | 69% |
| 采样步数 | 10 | 9 - 10 | 7 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1920，7 个样本
- 高度 中位数 1080，观测区间 1024 - 1960，7 个样本
- 采样步数 中位数 10，观测区间 9 - 10，7 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
