---
name: image_to_image_upscale_latent_upscale_face_detailer
type: Image To Image
frequency: 2
level: weak
coverage: 0.6235
common_nodes: [Anything Everywhere?, CLIPLoader, CLIPTextEncode, CR Latent Input Switch, DetailerForEach, DivideNode, DualCLIPLoader, EmptySD3LatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), GetNode, Image Perlin Noise, Image Power Noise, ImageBlend, ImageScale, ImageUpscaleWithModel, ImpactDilateMask, ImpactGaussianBlurMask, JDC_Plasma, JWFloatToInteger, KSampler, KSamplerAdvanced, LatentApplyOperation, LatentOperationSharpen, LatentUpscale, LoadImage, MaskToSEGS, Power Lora Loader (rgthree), SaveImage, SetNode, T5TokenizerOptions, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, mxSlider2D]
problems: [Steps较低可能导致细节不足]
missing: [Anything Everywhere?, Image Perlin Noise, Image Power Noise, easy cleanGpuUsed, easy int, CR Latent Input Switch, Power Lora Loader (rgthree), Preview from image [Crystools], Bookmark (rgthree), Label (rgthree)]
members: [图片生成/文生图/1931366022471987202.json, 图片生成/文生图/1931673497590759426.json]
source: knowledge_consolidation
---

# image_to_image_upscale_latent_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1931366022471987202.json、图片生成/文生图/1931673497590759426.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere?`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Latent Input Switch`
- `DetailerForEach`
- `DivideNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Perlin Noise`
- `Image Power Noise`
- `ImageBlend`
- `ImageScale`
- `ImageUpscaleWithModel`
- `ImpactDilateMask`
- `ImpactGaussianBlurMask`
- `JDC_Plasma`
- `JWFloatToInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LatentApplyOperation`
- `LatentOperationSharpen`
- `LatentUpscale`
- `LoadImage`
- `MaskToSEGS`
- `Power Lora Loader (rgthree)`
- `SaveImage`
- `SetNode`
- `T5TokenizerOptions`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `mxSlider2D`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Preview from image [Crystools]` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 9.5 | - | 2 | 74% |
| 采样算法 | 3 | - | 2 | 33% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9.5，样本不足，未给区间，2 个样本
- 采样算法 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Anything Everywhere?、Image Perlin Noise、Image Power Noise、easy cleanGpuUsed、easy int
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
