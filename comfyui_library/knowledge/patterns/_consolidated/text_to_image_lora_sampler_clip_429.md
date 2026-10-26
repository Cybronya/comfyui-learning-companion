---
name: text_to_image_lora_sampler_clip_429
type: Text To Image
frequency: 4
level: strong
coverage: 0.782
common_nodes: [Any Switch (rgthree), BiRefNetRMBG, CLIPLoader, CLIPTextEncode, DrawMaskOnImage, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToTotalPixels, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResizeImageMaskNode, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy stylesSelector, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 Edit图像编辑功能合集，双图编辑局部重绘扩图风格转绘多合一_2103530011402792962.json, 图片生成/图生图/Krea2 编辑好用功能合集 V1｜重绘扩图风格转绘全都有_2096875053836234753.json, 图片生成/图生图/Krea2编辑功能合集局部重绘扩图风格转绘图生图处理工具_2102148673747636226.json, 图片生成/图生图/Krea2编辑好用功能合集V1｜局部重绘扩图图生图_2096679382592081921.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_429

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Krea2 Edit图像编辑功能合集，双图编辑局部重绘扩图风格转绘多合一_2103530011402792962.json、图片生成/图生图/Krea2 编辑好用功能合集 V1｜重绘扩图风格转绘全都有_2096875053836234753.json、图片生成/图生图/Krea2编辑功能合集局部重绘扩图风格转绘图生图处理工具_2102148673747636226.json、图片生成/图生图/Krea2编辑好用功能合集V1｜局部重绘扩图图生图_2096679382592081921.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy stylesSelector`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（28/4 个样本）：Steps较低可能导致细节不足
