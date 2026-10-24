---
name: image_to_image_sampler_unet_vae_26
type: Image To Image
frequency: 9
level: strong
coverage: 0.864889
common_nodes: [DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext-模特换装_1943237232079888386.json, 图片生成/图生图/kontext_dev基础图生图_1950160096715259906.json, 图片生成/图生图/kontext_全能精修丨产品精修_1947203500150300673.json, 图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json, 图片生成/图生图/kontext完美去水印_1982370246738755585.json, 图片生成/图生图/kontext完美去水印_1989946491684966402.json, 图片生成/图生图/kontext服装精修_2020008788572512257.json, 图片生成/图生图/kontext灰度图工作流_1963233328004575234.json, 图片生成/图生图/万物皆可涂鸦_1965395252951531521.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/kontext-模特换装_1943237232079888386.json、图片生成/图生图/kontext_dev基础图生图_1950160096715259906.json、图片生成/图生图/kontext_全能精修丨产品精修_1947203500150300673.json、图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json、图片生成/图生图/kontext完美去水印_1982370246738755585.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
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
- `CLIPTextEncode` —— 8/9 个有
- `ConditioningZeroOut` —— 8/9 个有
- `FluxKontextImageScale` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 5/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `Anything Everywhere` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ChinesePrompt_Mix` —— 1/9 个有
- `ConstrainImage|pysssss` —— 1/9 个有
- `Evaluate Strings` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `GoogleTranslateCLIPTextEncodeNode` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `SetLatentNoiseMask` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 9 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，9 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
