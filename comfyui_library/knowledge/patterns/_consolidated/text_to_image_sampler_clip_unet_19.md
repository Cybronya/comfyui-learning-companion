---
name: text_to_image_sampler_clip_unet_19
type: Text To Image
frequency: 18
level: weak
coverage: 0.883889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 全官方 LoRA 风格集成_2069797124136595458.json, 图片生成/文生图/Krea2 Trubo 美商极高文生图 V2【极速版】_2115257635292401665.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json, 图片生成/文生图/Krea2 Turbo美商极高文生图 极速版高质量图片生成_2098661641754857473.json, 图片生成/文生图/Krea2图图工作流｜人像写真高质量质感生成_2095245729957761026.json, 图片生成/文生图/Krea2图图文生图｜高质量图像生成工作流_2095973742240423938.json, 图片生成/文生图/Krea2基础文生图高清出图｜美少女写实风格_2090073140905988098.json, 图片生成/文生图/Krea2影视柔光效果｜文生图MJ风格质感_2094546613636255746.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成_2098834148222914561.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成工作流_2098711426352377857.json, 图片生成/文生图/Krea2极清画质文生图工作流｜写实高清放大一步到位_2098698482818314242.json, 图片生成/文生图/▶▷Krea2-极清生图流_2098429137626161153.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json, 视频生成/文生视频/Krea2 极清生图｜从一句灵感，到惊艳大片_2098733373807218689.json, 视频生成/文生视频/Krea2极清灵感生图 从文字到惊艳大片_2098843566570299393.json, 视频生成/文生视频/Krea2极清生图神器｜一句灵感直达惊艳大片质感｜文生视频图生视频_2099127688740036610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Krea-2 全官方 LoRA 风格集成_2069797124136595458.json、图片生成/文生图/Krea2 Trubo 美商极高文生图 V2【极速版】_2115257635292401665.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json、图片生成/文生图/Krea2 Turbo美商极高文生图 极速版高质量图片生成_2098661641754857473.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/18 个有
- `LoraLoaderModelOnly` —— 15/18 个有
- `JjkText` —— 13/18 个有
- `solarL_SaveImagesToZip` —— 13/18 个有
- `孤海注释` —— 13/18 个有
- `PreviewImage` —— 12/18 个有
- `Fast Groups Bypasser (rgthree)` —— 11/18 个有
- `ResolutionSelector` —— 10/18 个有
- `KSamplerAdvanced` —— 9/18 个有
- `LatentUpscaleBy` —— 9/18 个有
- `LoadLatent` —— 9/18 个有
- `SaveLatent` —— 9/18 个有
- `Seed (rgthree)` —— 9/18 个有
- `CR Text` —— 4/18 个有
- `QZ_ResolutionPreset` —— 2/18 个有
- `Anything Everywhere` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 18 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 56% |
| 采样算法 | er_sde | - | 18 | 72% |
| 调度器 | beta | - | 18 | 78% |
| 重绘幅度 | 1 | 0.54 - 1 | 18 | 81% |
| 宽度 | 80 | 80 - 1080 | 18 | 0% |
| 高度 | 80 | 80 - 1920 | 18 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 38/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，18 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本
- 采样算法 最常用 er_sde，18 个样本，一致性 72%
- 调度器 最常用 beta，18 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.54 - 1，18 个样本，取值集中（一致性 81%）
- 宽度 中位数 80，观测区间 80 - 1080，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，18 个样本，取值分散，一致性仅 0%
- 高发问题（38/18 个样本）：Steps较低可能导致细节不足
