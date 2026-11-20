---
name: image_to_image_lora_sampler_unet_155
type: Image To Image
frequency: 4
level: moderate
coverage: 0.916
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetLatentNoiseMask, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511场景加模特（真实去AI感）_2013203484270665729.json, 图片生成/图生图/Qwen2511室内设计-局部修改变效果_2013202880232169474.json, 图片生成/图生图/Qwen场景加模特（真实去AI感）_2028289977292951554.json, 图片生成/图生图/qwen_image_edit_2511现实融合动漫_2011981712590381058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2511场景加模特（真实去AI感）_2013203484270665729.json、图片生成/图生图/Qwen2511室内设计-局部修改变效果_2013202880232169474.json、图片生成/图生图/Qwen场景加模特（真实去AI感）_2028289977292951554.json、图片生成/图生图/qwen_image_edit_2511现实融合动漫_2011981712590381058.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetLatentNoiseMask`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `GetImageSize+` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: RestoreCropBox` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `LayerMask: MaskGrow` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 12 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 12，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
