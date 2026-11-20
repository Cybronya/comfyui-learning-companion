---
name: image_to_image_lora_sampler_unet_100
type: Image To Image
frequency: 8
level: moderate
coverage: 0.889875
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_image_edit_2511现实融合动漫_2011981712590381058.json, 图片生成/图生图/ywt低价版1.0_2059986818820567041.json, 图片生成/图生图/ywt低价版2.0_2059997662291779585.json, 图片生成/图生图/ywt低价版3.0_2060024511612936194.json, 图片生成/图生图/ywt低价版4.0_2060256743405473793.json, 图片生成/图生图/ywt低价版5.0_2060394577848258561.json, 图片生成/图生图/产品摄影背景迁移 qwen_image_edit_2511_2015810728174821378.json, 图片生成/图生图/人物换发型_2037156801669505026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_100

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen_image_edit_2511现实融合动漫_2011981712590381058.json、图片生成/图生图/ywt低价版1.0_2059986818820567041.json、图片生成/图生图/ywt低价版2.0_2059997662291779585.json、图片生成/图生图/ywt低价版3.0_2060024511612936194.json、图片生成/图生图/ywt低价版4.0_2060256743405473793.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `RH_Nano_Banana_Image2Image` —— 5/8 个有
- `RH_RhartImageG2ImageToImage` —— 4/8 个有
- `CR Text` —— 2/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/8 个有
- `FillMaskedArea_UTK` —— 1/8 个有
- `GrowMask` —— 1/8 个有
- `LayerMask: MaskGrow` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `SetLatentNoiseMask` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 8 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 0.72 | 0.72 - 1 | 8 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，8 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 0.72，观测区间 0.72 - 1，8 个样本，取值集中（一致性 84%）
- 高发问题（16/8 个样本）：Steps较低可能导致细节不足
