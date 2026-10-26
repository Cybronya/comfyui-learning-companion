---
name: image_to_image_sampler_unet_vae_23
type: Image To Image
frequency: 8
level: strong
coverage: 0.875625
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext-模特换装_1943237232079888386.json, 图片生成/图生图/kontext_dev一键扩图_1952734346315821058.json, 图片生成/图生图/kontext_dev基础图生图_1950160096715259906.json, 图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json, 图片生成/图生图/kontext完美去水印_1982370246738755585.json, 图片生成/图生图/kontext完美去水印_1989946491684966402.json, 图片生成/图生图/kontext手办_1946110044947836930.json, 图片生成/图生图/像素级高清放大工作流_1940572324460474370.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_23

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/kontext-模特换装_1943237232079888386.json、图片生成/图生图/kontext_dev一键扩图_1952734346315821058.json、图片生成/图生图/kontext_dev基础图生图_1950160096715259906.json、图片生成/图生图/kontext一键去水印 _ 前后对比_2069314818917625857.json、图片生成/图生图/kontext完美去水印_1982370246738755585.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `PreviewImage` —— 5/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `GoogleTranslateCLIPTextEncodeNode` —— 1/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: SaveImagePlusV2` —— 1/8 个有
- `SetLatentNoiseMask` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
