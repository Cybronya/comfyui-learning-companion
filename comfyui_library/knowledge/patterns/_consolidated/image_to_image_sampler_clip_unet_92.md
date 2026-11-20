---
name: image_to_image_sampler_clip_unet_92
type: Image To Image
frequency: 5
level: strong
coverage: 0.5856
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, GetNode, KSampler, LoadImage, ModelSamplingFlux, ReferenceLatent, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext 局部重绘+万物消除（好用）_1954922738977685505.json, 图片生成/图生图/Kontext 开源版 _ 双图组合（简易版）_1954913189995712513.json, 图片生成/图生图/Kontext 开源版 _ 双图组合（简易版）_1990120107005407234.json, 图片生成/图生图/Kontext 开源版本 _ 单图编辑处理_1954902834832556034.json, 图片生成/图生图/Kontext+老照片一键修复+上色_1955226608435171330.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 局部重绘+万物消除（好用）_1954922738977685505.json、图片生成/图生图/Kontext 开源版 _ 双图组合（简易版）_1954913189995712513.json、图片生成/图生图/Kontext 开源版 _ 双图组合（简易版）_1990120107005407234.json、图片生成/图生图/Kontext 开源版本 _ 单图编辑处理_1954902834832556034.json、图片生成/图生图/Kontext+老照片一键修复+上色_1955226608435171330.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `GetNode`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `GLM_Text_Chat` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `Convert Masks to Images` —— 1/5 个有
- `Image To Mask` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `String` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
