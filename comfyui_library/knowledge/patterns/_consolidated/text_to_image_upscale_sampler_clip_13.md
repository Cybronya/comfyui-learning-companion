---
name: text_to_image_upscale_sampler_clip_13
type: Text To Image
frequency: 8
level: weak
coverage: 0.789875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, KSampler, PreviewImage, PrimitiveFloat, SaveImage, Seed (rgthree), SimpleMathDual+, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/▶▷Krea2-极清生图流+USD图像放大_2099319902912995330.json, 图片生成/图生图/▶▷Krea2-极清生图流+USD图像放大_2099663943764627457.json, 图片生成/文生图/1. 超写实文生图工作流｜原生真实人像质感_2081413061948297218.json, 图片生成/文生图/Krea2 极清文生图｜双重采样+高清重绘_2101078599364337666.json, 图片生成/文生图/Krea2_极清生图流_2111217269018812418.json, 图片生成/文生图/Krea2双重采样高清重绘极清文生图处理工作流_2101351948409729026.json, 图片生成/文生图/Krea2极清生图流，人像写真高清放大文生图_2111604044065230850.json, 图片生成/文生图/▶▷Krea2-极清生图流+USD图像放大_2098441574471520258.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/▶▷Krea2-极清生图流+USD图像放大_2099319902912995330.json、图片生成/图生图/▶▷Krea2-极清生图流+USD图像放大_2099663943764627457.json、图片生成/文生图/1. 超写实文生图工作流｜原生真实人像质感_2081413061948297218.json、图片生成/文生图/Krea2 极清文生图｜双重采样+高清重绘_2101078599364337666.json、图片生成/文生图/Krea2_极清生图流_2111217269018812418.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `KSampler`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMathDual+`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 7/8 个有
- `LatentUpscaleBy` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `JjkText` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `easy loraStack` —— 2/8 个有
- `easy loraStackApply` —— 2/8 个有
- `solarL_SaveImagesToZip` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 8 | 47% |
| 高度 | 1024 | 80 - 1280 | 8 | 47% |
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 8 | 8 | 20% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 0.77 | 0.54 - 1 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 47%
- 高度 中位数 1024，观测区间 80 - 1280，8 个样本，取值分散，一致性仅 47%
- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 8，8 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 0.77，观测区间 0.54 - 1，6 个样本
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
