---
name: image_to_image_sampler_clip_unet_43
type: Image To Image
frequency: 8
level: moderate
coverage: 0.49725
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, PlaySound|pysssss, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/YZ金鱼-Z_Image-图文生图&洗图&高清修复v1_2053381046279917570.json, 图片生成/图生图/ProReal Pipeline_2001169170496712705.json, 图片生成/图生图/Z-Image-图文生图-洗图-高清修复 z image zimage_1995761280600387585.json, 图片生成/图生图/去照片AI味道_2009622540498505729.json, 图片生成/图生图/洗图_1941160724741963777.json, 图片生成/图生图/洗图工作流_2031338925985370113.json, 图片生成/文生图/YZ金鱼-Z_Image-图文生图&洗图&高清修复v1_1993975579062059010.json, 图片生成/文生图/Z-Image-图文生图-洗图-高清修复 z image zimage_2007444305413148674.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/YZ金鱼-Z_Image-图文生图&洗图&高清修复v1_2053381046279917570.json、图片生成/图生图/ProReal Pipeline_2001169170496712705.json、图片生成/图生图/Z-Image-图文生图-洗图-高清修复 z image zimage_1995761280600387585.json、图片生成/图生图/去照片AI味道_2009622540498505729.json、图片生成/图生图/洗图_1941160724741963777.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 7/8 个有
- `CR SDXL Aspect Ratio` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ImageScaleBy` —— 7/8 个有
- `Qwen3_VQA` —— 7/8 个有
- `SeedVR2` —— 7/8 个有
- `SeedVR2BlockSwap` —— 7/8 个有
- `SeedVR2ExtraArgs` —— 7/8 个有
- `ShowText|pysssss` —— 7/8 个有
- `LayerUtility: ImageReel` —— 6/8 个有
- `LayerUtility: ImageReelComposit` —— 6/8 个有
- `Float` —— 1/8 个有
- `Lora Loader Stack (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 8 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.53 | 8 | 84% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 0.65 | 0.25 - 0.65 | 8 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.53，8 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 0.65，观测区间 0.25 - 0.65，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
