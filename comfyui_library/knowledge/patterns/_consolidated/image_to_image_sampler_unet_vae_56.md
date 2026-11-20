---
name: image_to_image_sampler_unet_vae_56
type: Image To Image
frequency: 4
level: strong
coverage: 0.8615
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, CropFaces, DWPreprocessor, DetectFaces, FluxKontextMultiReferenceLatentMethod, GetImageSize+, GrowMask, Image Blank, ImageCompositeMasked, ImageScaleToTotalPixels, JoinImageWithAlpha, KSampler, LayerMask: MaskGrow, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, WarpFacesBack, easy imageColorMatch, easy imageScaleToNormPixels]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 2511一键换头换脸最强相似度_2006379391579852801.json, 图片生成/图生图/遮罩Qwen edit 2511一键换头换脸最强相似度_2009263213426253826.json, 图片生成/图生图/遮罩Qwen edit 2511一键换头换脸最强相似度_2017263490062360578.json, 平台全量/内部测试专用003（HT）_2015424431618789378.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen edit 2511一键换头换脸最强相似度_2006379391579852801.json、图片生成/图生图/遮罩Qwen edit 2511一键换头换脸最强相似度_2009263213426253826.json、图片生成/图生图/遮罩Qwen edit 2511一键换头换脸最强相似度_2017263490062360578.json、平台全量/内部测试专用003（HT）_2015424431618789378.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropFaces`
- `DWPreprocessor`
- `DetectFaces`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize+`
- `GrowMask`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `WarpFacesBack`
- `easy imageColorMatch`
- `easy imageScaleToNormPixels`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `VaeGGUF` —— 3/4 个有
- `ClothesSegment` —— 1/4 个有
- `FeatherMask` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LayerMask: PersonMaskUltra V2` —— 1/4 个有
- `LoadSAM3Model` —— 1/4 个有
- `MaskComposite` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewBridge` —— 1/4 个有
- `SAM3Segmentation` —— 1/4 个有
- `Switch any [Crystools]` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ddim | - | 4 | 100% |
| 调度器 | linear_quadratic | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，4 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
