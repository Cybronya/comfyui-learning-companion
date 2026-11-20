---
name: image_to_image_lora_sampler_unet_179
type: Image To Image
frequency: 3
level: moderate
coverage: 0.851667
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, FluxKontextMultiReferenceLatentMethod, ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, ReferenceLatent, SaveImage, SetLatentNoiseMask, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 双图遮罩编辑v2.0-不偏色-不偏移_2004217721007075329.json, 图片生成/图生图/遮罩编辑 & 无遮罩编辑【双模式切换】Qwen Edit-2511_2005546827141316610.json, 图片生成/图生图/遮罩编辑换衣服_2088193397772345345.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 双图遮罩编辑v2.0-不偏色-不偏移_2004217721007075329.json、图片生成/图生图/遮罩编辑 & 无遮罩编辑【双模式切换】Qwen Edit-2511_2005546827141316610.json、图片生成/图生图/遮罩编辑换衣服_2088193397772345345.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ToBinaryMask` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `ImageAndMaskPreview` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 3 | 91% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，3 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
