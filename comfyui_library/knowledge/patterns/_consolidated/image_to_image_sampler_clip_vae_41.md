---
name: image_to_image_sampler_clip_vae_41
type: Image To Image
frequency: 4
level: strong
coverage: 0.8975
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json, 图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json, 图片生成/图生图/极速图像水印擦除无损文字_2010878088397201409.json, 图片生成/图生图/水印擦除无损文字_1963570799078772738.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/nunchaku-flux.1-kontext-扩图2_1957247851829059585.json、图片生成/图生图/nunchaku-flux.1-kontext-扩图_1956295255689711618.json、图片生成/图生图/极速图像水印擦除无损文字_2010878088397201409.json、图片生成/图生图/水印擦除无损文字_1963570799078772738.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `GetImageSize+` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `LayerUtility: ImageCombineAlpha` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
