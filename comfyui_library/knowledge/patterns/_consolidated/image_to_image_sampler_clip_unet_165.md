---
name: image_to_image_sampler_clip_unet_165
type: Image To Image
frequency: 2
level: weak
coverage: 0.831
common_nodes: [CLIPTextEncode, CR Text, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, NunchakuFluxDiTLoader, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext智能移除_1943132802625781761.json, 图片生成/图生图/flux-kontext-生成爆款手办_1964682155462901762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext智能移除_1943132802625781761.json、图片生成/图生图/flux-kontext-生成爆款手办_1964682155462901762.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
