---
name: text_to_image_sampler_clip_unet_84
type: Text To Image
frequency: 7
level: weak
coverage: 0.935286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Boogu图生图标准版_2068947798048989186.json, 图片生成/图生图/F2_klein多图_2056028041498898434.json, 图片生成/图生图/Klein-9B-姿势控制按参考图生成_2071965968569552898.json, 图片生成/图生图/Klein-9B-法线按参考图生成_2071952516740370433.json, 图片生成/图生图/Klein-9B-深度控制按参考图生成_2071964572617105410.json, 图片生成/图生图/Klein-9B-线稿按参考图生成_2071927150692880385.json, 图片生成/图生图/双图姿势迁移＋4K高清放大工作流｜自动跟随构图，换图即可运行_2095860795405070337.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Boogu图生图标准版_2068947798048989186.json、图片生成/图生图/F2_klein多图_2056028041498898434.json、图片生成/图生图/Klein-9B-姿势控制按参考图生成_2071965968569552898.json、图片生成/图生图/Klein-9B-法线按参考图生成_2071952516740370433.json、图片生成/图生图/Klein-9B-深度控制按参考图生成_2071964572617105410.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `Int` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `DWPreprocessor` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `CannyEdgePreprocessor` —— 1/7 个有
- `DSINE-NormalMapPreprocessor` —— 1/7 个有
- `DepthAnythingV2Preprocessor` —— 1/7 个有
- `EmptyFlux2LatentImage` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有
- `ZML_PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 7 | 70% |
| 高度 | 512 | 512 - 1344 | 7 | 55% |
| 采样步数 | 8 | 6 - 50 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，7 个样本
- 高度 中位数 512，观测区间 512 - 1344，7 个样本
- 采样步数 中位数 8，观测区间 6 - 50，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
