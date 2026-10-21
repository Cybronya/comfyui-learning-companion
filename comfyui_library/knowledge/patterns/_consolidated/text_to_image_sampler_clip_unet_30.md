---
name: text_to_image_sampler_clip_unet_30
type: Text To Image
frequency: 11
level: weak
coverage: 0.860818
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, PreviewImage, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1. 超写实文生图工作流｜原生真实人像质感_2081413061948297218.json, 图片生成/文生图/Krea2 极清文生图｜双重采样+高清重绘_2101078599364337666.json, 图片生成/文生图/Krea2双重采样高清重绘极清文生图处理工作流_2101351948409729026.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成_2098834148222914561.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成工作流_2098711426352377857.json, 图片生成/文生图/Krea2极清画质文生图工作流｜写实高清放大一步到位_2098698482818314242.json, 图片生成/文生图/▶▷Krea2-极清生图流+USD图像放大_2098441574471520258.json, 图片生成/文生图/▶▷Krea2-极清生图流_2098429137626161153.json, 视频生成/文生视频/Krea2 极清生图｜从一句灵感，到惊艳大片_2098733373807218689.json, 视频生成/文生视频/Krea2极清灵感生图 从文字到惊艳大片_2098843566570299393.json, 视频生成/文生视频/Krea2极清生图神器｜一句灵感直达惊艳大片质感｜文生视频图生视频_2099127688740036610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1. 超写实文生图工作流｜原生真实人像质感_2081413061948297218.json、图片生成/文生图/Krea2 极清文生图｜双重采样+高清重绘_2101078599364337666.json、图片生成/文生图/Krea2双重采样高清重绘极清文生图处理工作流_2101351948409729026.json、图片生成/文生图/Krea2极清生图流 高清写实风格图片生成_2098834148222914561.json、图片生成/文生图/Krea2极清生图流 高清写实风格图片生成工作流_2098711426352377857.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 10/11 个有
- `LatentUpscaleBy` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `JjkText` —— 7/11 个有
- `LoadLatent` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `SaveLatent` —— 7/11 个有
- `solarL_SaveImagesToZip` —— 7/11 个有
- `孤海注释` —— 7/11 个有
- `GetImageSize+` —— 4/11 个有
- `PrimitiveFloat` —— 4/11 个有
- `SimpleMathDual+` —— 4/11 个有
- `UltimateSDUpscale` —— 4/11 个有
- `UpscaleModelLoader` —— 4/11 个有
- `Label (rgthree)` —— 2/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `ModelSamplingAuraFlow` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1280 | 11 | 0% |
| 采样步数 | 4 | 4 - 8 | 10 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 11 | 48% |
| 采样算法 | er_sde | - | 11 | 64% |
| 调度器 | beta | - | 11 | 64% |
| 重绘幅度 | 1 | 0.54 - 1 | 10 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，11 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，11 个样本，一致性 64%
- 调度器 最常用 beta，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 0.54 - 1，10 个样本
- 高发问题（21/11 个样本）：Steps较低可能导致细节不足
