---
name: image_to_image_lora_sampler_clip_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.704333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImpactInt, InspyrenetRembg, KSampler, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [Label (rgthree), LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, Upscale Model Loader]
members: [图片生成/图生图/2047137205226840065.json, 图片生成/图生图/2054854751262650369.json, 图片生成/图生图/2056249240434864130.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2047137205226840065.json、图片生成/图生图/2054854751262650369.json、图片生成/图生图/2056249240434864130.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `InspyrenetRembg`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有
- `YUAN_TXTConvertAny` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2、LayerMask: MaskGrow、LayerUtility: HLFrequencyDetailRestore
