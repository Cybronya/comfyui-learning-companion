---
name: image_to_image_lora_sampler_clip_54
type: Image To Image
frequency: 5
level: moderate
coverage: 0.944
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, FluxGuidance, GetImageSize, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein9B 无痕换头放大天花板_2026456875612508162.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2024685759059464194.json, 图片生成/文生图/Flux2-Klein 换头放大版_2026341472559177729.json, 图片生成/文生图/Flux2-Klein9B 无痕换头放大大师版_2026299604819517442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein9B 无痕换头放大天花板_2026456875612508162.json、图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json、图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2024685759059464194.json、图片生成/文生图/Flux2-Klein 换头放大版_2026341472559177729.json、图片生成/文生图/Flux2-Klein9B 无痕换头放大大师版_2026299604819517442.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `FluxGuidance`
- `GetImageSize`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/5 个有
- `Image To Mask` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LanPaint_KSampler` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `Image Compare (mtb)` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 5 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，5 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
