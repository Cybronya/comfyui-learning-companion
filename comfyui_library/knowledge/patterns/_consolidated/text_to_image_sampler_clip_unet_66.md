---
name: text_to_image_sampler_clip_unet_66
type: Text To Image
frequency: 7
level: weak
coverage: 0.892714
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json, 图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json, 图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json, 图片生成/文生图/Krea2人像摄影应用｜turbo-bf16写实人像生成_2095562706337230850.json, 图片生成/文生图/Krea2双采样2K直出文生图｜高质量图像生成_2094557972373528577.json, 图片生成/文生图/Z-Seed超清人像引擎｜高质量写真文生图_2094582526194044930.json, 图片生成/文生图/文生图写真创作工作流+4K出图_2082314053673902082.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json、图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json、图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json、图片生成/文生图/Krea2人像摄影应用｜turbo-bf16写实人像生成_2095562706337230850.json、图片生成/文生图/Krea2双采样2K直出文生图｜高质量图像生成_2094557972373528577.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `solarL_SaveImagesToZip` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `FloatConstant` —— 4/7 个有
- `ImageSharpenKJ` —— 4/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `VAEEncode` —— 3/7 个有
- `easy seed` —— 3/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `KSamplerAdvanced` —— 2/7 个有
- `LatentUpscaleBy` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `SeedVR2LoadDiTModel` —— 2/7 个有
- `SeedVR2LoadVAEModel` —— 2/7 个有
- `SeedVR2VideoUpscaler` —— 2/7 个有
- `CLIPLoaderGGUF` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `SimpleCalculatorKJ` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 7 | 0% |
| 高度 | 80 | 80 - 768 | 7 | 0% |
| 采样步数 | 4 | 4 - 5 | 7 | 92% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 69% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 0.6 - 1 | 7 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 768，7 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 5，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，7 个样本，取值集中（一致性 85%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
