---
name: unknown_workflow_lora_sampler_unet_72
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.857
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI生成你的前世今生之260503_2042885986253807617.json, 图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json, 图片生成/文生图/FireRed-Image-Edit超强合集_2032145474236456961.json, 图片生成/文生图/一键换衣_2076039591257264130.json, 图片生成/文生图/换装  换衣  一键换衣  衣服展示_2050943553332883458.json, 平台全量/Qwen-Edit-2509一键人物Cosplay_2073044928367783938.json, 平台全量/【一键变装】多服装展示，效果超合身_2072520380102832129.json, 平台全量/一键Cosplay换装_1992972872870199297.json, 平台全量/一键换衣- 换装&模特展示 服装展示_2039900928697962498.json, 平台全量/千问2511图像编辑_2013193664234790914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/AI生成你的前世今生之260503_2042885986253807617.json、图片生成/文生图/FireRed-Image-Edit 单图、双图编辑 万能图像编辑  超强图片编辑_2027222768265203714.json、图片生成/文生图/FireRed-Image-Edit超强合集_2032145474236456961.json、图片生成/文生图/一键换衣_2076039591257264130.json、图片生成/文生图/换装  换衣  一键换衣  衣服展示_2050943553332883458.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
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
- `PreviewImage` —— 8/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `Anything Everywhere3` —— 2/10 个有
- `FluxKontextImageScale` —— 2/10 个有
- `EmptyLatentImage` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `easy promptLine` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 15 | 10 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 15，10 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
