---
name: image_to_image_sampler_clip_unet_25
type: Image To Image
frequency: 2
level: weak
coverage: 0.5
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PlaySound|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YZ金鱼-Z_Image-图文生图&洗图&高清修复v1_1993975579062059010.json, 图片生成/文生图/Z-Image-图文生图-洗图-高清修复 z image zimage_2007444305413148674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/YZ金鱼-Z_Image-图文生图&洗图&高清修复v1_1993975579062059010.json、图片生成/文生图/Z-Image-图文生图-洗图-高清修复 z image zimage_2007444305413148674.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
