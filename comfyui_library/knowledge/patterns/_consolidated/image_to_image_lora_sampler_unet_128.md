---
name: image_to_image_lora_sampler_unet_128
type: Image To Image
frequency: 6
level: moderate
coverage: 0.849833
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, FluxKontextMultiReferenceLatentMethod, ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, ReferenceLatent, SaveImage, SetLatentNoiseMask, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 双图遮罩编辑v2.0-不偏色-不偏移_2004217721007075329.json, 图片生成/图生图/遮罩编辑 & 无遮罩编辑【双模式切换】Qwen Edit-2511_2005546827141316610.json, 图片生成/图生图/遮罩编辑换衣服_2088193397772345345.json, 平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json, 平台全量/图像万能编辑 Qwen Edit-2511 遮罩编辑 & 无遮罩编辑 双模式切换  精准电商换装 服_2007631549130350593.json, 平台全量/遮罩编辑&Qwen+Edit-2511.HQ14（修改万物指哪里改哪里）_2024049627607080961.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_128

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 双图遮罩编辑v2.0-不偏色-不偏移_2004217721007075329.json、图片生成/图生图/遮罩编辑 & 无遮罩编辑【双模式切换】Qwen Edit-2511_2005546827141316610.json、图片生成/图生图/遮罩编辑换衣服_2088193397772345345.json、平台全量/不偏色-不偏移Qwen+Edit+2511+双图遮罩编辑v2.0_2005274774496571394.json、平台全量/图像万能编辑 Qwen Edit-2511 遮罩编辑 & 无遮罩编辑 双模式切换  精准电商换装 服_2007631549130350593.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageConcanate` —— 4/6 个有
- `Mask Fill Holes` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ToBinaryMask` —— 4/6 个有
- `easy boolean` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `easy ifElse` —— 4/6 个有
- `ImageAndMaskPreview` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 6 | 93% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，6 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
