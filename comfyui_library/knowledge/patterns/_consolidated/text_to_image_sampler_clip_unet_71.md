---
name: text_to_image_sampler_clip_unet_71
type: Text To Image
frequency: 9
level: weak
coverage: 0.907556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2风格迁移文生图，双采样2K直出质感在线_2112684567713902593.json, 图片生成/图生图/文生图双采样2K直出｜Krea2 风格迁移一键换画风_2096199582404407298.json, 图片生成/图生图/风格迁移双采样直出｜Krea2文生图2K高清生成_2095933118401306625.json, 图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json, 图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json, 图片生成/文生图/Krea2双图编辑完美替换｜文生图图生图堪比闭源_2090473972126273538.json, 图片生成/文生图/Krea2双采样2K直出文生图｜高质量图像生成_2094557972373528577.json, 图片生成/文生图/双图编辑完美替换｜Krea2文生图图生图处理_2090192438358011906.json, 视频生成/文生视频/单图编辑完美一致性｜Krea2文生图图生视频生成_2090203681751912449.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2风格迁移文生图，双采样2K直出质感在线_2112684567713902593.json、图片生成/图生图/文生图双采样2K直出｜Krea2 风格迁移一键换画风_2096199582404407298.json、图片生成/图生图/风格迁移双采样直出｜Krea2文生图2K高清生成_2095933118401306625.json、图片生成/文生图/2K直出双采样｜Krea2文生图一键高质量生成_2094796360594837505.json、图片生成/文生图/Krea2-双采样2K直出-文生图_2094364725722304513.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `solarL_SaveImagesToZip` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `CR Prompt Text` —— 6/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `EmptySD3LatentImage` —— 6/9 个有
- `FloatConstant` —— 6/9 个有
- `ImageSharpenKJ` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `easy seed` —— 6/9 个有
- `Krea2EditGroundedEncode` —— 3/9 个有
- `Krea2EditModelPatch` —— 3/9 个有
- `Krea2StyleReference` —— 3/9 个有
- `Krea2StyleTransfer` —— 3/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `Seed (rgthree)` —— 3/9 个有
- `Label (rgthree)` —— 2/9 个有
- `GetImageSize+` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 9 | 0% |
| 高度 | 80 | 80 - 768 | 9 | 0% |
| 采样步数 | 4 | 4 - 5 | 9 | 92% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 73% |
| 采样算法 | er_sde | - | 9 | 89% |
| 调度器 | beta | - | 9 | 89% |
| 重绘幅度 | 1 | 0.6 - 1 | 9 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，9 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 768，9 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 5，9 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 89%
- 调度器 最常用 beta，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 87%）
- 高发问题（20/9 个样本）：Steps较低可能导致细节不足
