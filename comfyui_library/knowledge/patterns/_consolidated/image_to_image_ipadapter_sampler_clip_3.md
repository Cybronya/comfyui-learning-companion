---
name: image_to_image_ipadapter_sampler_clip_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.695
common_nodes: [BackgroundScaler, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, GrowMask, ICLightConditioning, Image Blend by Mask, Image Blending Mode, Image Filter Adjustments, Image Levels Adjustment, ImageBlur, ImageInvert, ImpactGaussianBlurMask, KSampler, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, SaveImage, SplitImageWithAlpha, VAEDecode, VAEEncode, easy hiresFix, easy ipadapterApply]
problems: []
missing: []
members: [平台全量/10.换背景丨保留细节丨原图无损丨电商图丨4K+高清丨文字不失真_2000793114258403330.json, 平台全量/CG迷-高清产品海报工作流，保留细节，更换背景_1927043571172462593.json, 平台全量/换背景丨保留细节丨原图无损丨电商图_1988153330654429186.json, 平台全量/换背景丨保留细节丨原图无损丨电商图丨4K 高清丨文字不失真_1988544567043604482.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/10.换背景丨保留细节丨原图无损丨电商图丨4K+高清丨文字不失真_2000793114258403330.json、平台全量/CG迷-高清产品海报工作流，保留细节，更换背景_1927043571172462593.json、平台全量/换背景丨保留细节丨原图无损丨电商图_1988153330654429186.json、平台全量/换背景丨保留细节丨原图无损丨电商图丨4K 高清丨文字不失真_1988544567043604482.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `BackgroundScaler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `GrowMask`
- `ICLightConditioning`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Filter Adjustments`
- `Image Levels Adjustment`
- `ImageBlur`
- `ImageInvert`
- `ImpactGaussianBlurMask`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SplitImageWithAlpha`
- `VAEDecode`
- `VAEEncode`
- `easy hiresFix`
- `easy ipadapterApply`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `LayerMask: BiRefNetUltra` —— 3/4 个有
- `Label (rgthree)` —— 2/4 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/4 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `SAMModelLoader (segment anything)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 4 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 0.9 | 0.9 - 1 | 4 | 95% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 1，4 个样本，取值集中（一致性 95%）
