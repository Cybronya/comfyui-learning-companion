---
name: image_to_image_sampler_clip_unet_85
type: Image To Image
frequency: 5
level: strong
coverage: 0.8496
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/B7、扩图 kontext - 和风_1992964096752631810.json, 图片生成/图生图/C10、高清修复 kontext - 和风_1993501162225811458.json, 图片生成/图生图/Kontext-物品移除_1962442365640249345.json, 图片生成/图生图/Kontext移除工作流_1941522792838021122.json, 图片生成/图生图/Kontext移除工作流升级版_1939928704434741250.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/B7、扩图 kontext - 和风_1992964096752631810.json、图片生成/图生图/C10、高清修复 kontext - 和风_1993501162225811458.json、图片生成/图生图/Kontext-物品移除_1962442365640249345.json、图片生成/图生图/Kontext移除工作流_1941522792838021122.json、图片生成/图生图/Kontext移除工作流升级版_1939928704434741250.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `EmptyImage` —— 4/5 个有
- `ImageCompositeMasked` —— 4/5 个有
- `JoinImageWithAlpha` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `Anything Everywhere3` —— 2/5 个有
- `ImageAndMaskPreview` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Mask Fill Holes` —— 2/5 个有
- `MaskPreview` —— 2/5 个有
- `ACE_TextTranslate` —— 1/5 个有
- `DF_Get_image_size` —— 1/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `ImageCompositeMaskedOneByOne` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerMask: MaskGrow` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: LaMa` —— 1/5 个有
- `PDImageConcante` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
