---
name: text_to_image_sampler_clip_unet_88
type: Text To Image
frequency: 8
level: weak
coverage: 0.90075
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2风格迁移文生图，双采样2K直出质感在线_2112684567713902593.json, 图片生成/图生图/文生图双采样2K直出｜Krea2 风格迁移一键换画风_2096199582404407298.json, 图片生成/图生图/风格迁移双采样直出｜Krea2文生图2K高清生成_2095933118401306625.json, 图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json, 图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json, 图片生成/文生图/Krea2双采样2K直出文生图｜高质量图像生成_2094557972373528577.json, 图片生成/文生图/Z-Seed超清人像引擎｜高质量写真文生图_2094582526194044930.json, 图片生成/文生图/文生图写真创作工作流+4K出图_2082314053673902082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2风格迁移文生图，双采样2K直出质感在线_2112684567713902593.json、图片生成/图生图/文生图双采样2K直出｜Krea2 风格迁移一键换画风_2096199582404407298.json、图片生成/图生图/风格迁移双采样直出｜Krea2文生图2K高清生成_2095933118401306625.json、图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json、图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `FloatConstant` —— 7/8 个有
- `ImageSharpenKJ` —— 7/8 个有
- `JjkText` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `solarL_SaveImagesToZip` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `VAEEncode` —— 6/8 个有
- `easy seed` —— 6/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `Krea2StyleReference` —— 3/8 个有
- `Krea2StyleTransfer` —— 3/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SeedVR2LoadDiTModel` —— 2/8 个有
- `SeedVR2LoadVAEModel` —— 2/8 个有
- `SeedVR2VideoUpscaler` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `SimpleCalculatorKJ` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 8 | 0% |
| 高度 | 80 | 80 - 768 | 8 | 0% |
| 采样步数 | 4 | 4 - 5 | 8 | 92% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 72% |
| 采样算法 | er_sde | - | 8 | 88% |
| 调度器 | beta | - | 8 | 88% |
| 重绘幅度 | 1 | 0.6 - 1 | 8 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 768，8 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 5，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，8 个样本，取值集中（一致性 86%）
- 高发问题（21/8 个样本）：Steps较低可能导致细节不足
