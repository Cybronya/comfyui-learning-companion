---
name: image_to_image_lora_sampler_unet_205
type: Image To Image
frequency: 3
level: strong
coverage: 0.730667
common_nodes: [Any Switch (rgthree), BiRefNetRMBG, CLIPLoader, DrawMaskOnImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ResizeImageMaskNode, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy stylesSelector]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4-Krea2编辑好用功能合集工作流-V1_2093145195037675522.json, 平台全量/Krea2编辑好用功能合集工作流-V1_2095689159951347713.json, 平台全量/Krea2编辑好用功能合集工作流-V1_2095697794010017793.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_205

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/4-Krea2编辑好用功能合集工作流-V1_2093145195037675522.json、平台全量/Krea2编辑好用功能合集工作流-V1_2095689159951347713.json、平台全量/Krea2编辑好用功能合集工作流-V1_2095697794010017793.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BiRefNetRMBG`
- `CLIPLoader`
- `DrawMaskOnImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
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

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（18/3 个样本）：Steps较低可能导致细节不足
