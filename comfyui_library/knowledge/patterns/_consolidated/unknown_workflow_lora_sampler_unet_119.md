---
name: unknown_workflow_lora_sampler_unet_119
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854167
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI生成你的前世今生之260503_2042885986253807617.json, 图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json, 图片生成/文生图/FireRed-Image-Edit超强合集_2032145474236456961.json, 图片生成/文生图/一键换衣_2076039591257264130.json, 图片生成/文生图/换装  换衣  一键换衣  衣服展示_2050943553332883458.json, 视频生成/图生视频/换装 换衣  电商服装展示 FireRed-Image-Edit 小红书_2073634953857953794.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_119

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/AI生成你的前世今生之260503_2042885986253807617.json、图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json、图片生成/文生图/FireRed-Image-Edit超强合集_2032145474236456961.json、图片生成/文生图/一键换衣_2076039591257264130.json、图片生成/文生图/换装  换衣  一键换衣  衣服展示_2050943553332883458.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `easy promptLine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 15 | 6 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 15，6 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
