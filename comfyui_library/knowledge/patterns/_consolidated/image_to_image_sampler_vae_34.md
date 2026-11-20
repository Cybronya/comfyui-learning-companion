---
name: image_to_image_sampler_vae_34
type: Image To Image
frequency: 3
level: strong
coverage: 0.856333
common_nodes: [CFGNorm, CLIPLoader, Image Rembg (Remove Background), KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SetLatentNoiseMask, TTP_Expand_And_Mask, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-edit-2509物体迁移_1988956822683914242.json, 图片生成/文生图/Qwen Image Edit Plus的万物迁移_1972355834023964674.json, 平台全量/Qwen Image Edit 2509 万物迁移_1978102063672483842.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen-edit-2509物体迁移_1988956822683914242.json、图片生成/文生图/Qwen Image Edit Plus的万物迁移_1972355834023964674.json、平台全量/Qwen Image Edit 2509 万物迁移_1978102063672483842.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Rembg (Remove Background)`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `TTP_Expand_And_Mask`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Mask To Image (mtb)` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
