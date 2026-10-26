---
name: text_to_image_sampler_clip_unet_91
type: Text To Image
frequency: 8
level: weak
coverage: 0.876375
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/▶▷Krea2-极清生图流_2098429137626161153.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json, 图片生成/文生图/▶▷Krea2-极清生图流_2112007776892440578.json, 图片生成/文生图/▶▷Krea2-标准生图)_2077775542920769537.json, 视频生成/文生视频/Krea2 极清生图｜从一句灵感，到惊艳大片_2098733373807218689.json, 视频生成/文生视频/Krea2极清灵感生图 从文字到惊艳大片_2098843566570299393.json, 视频生成/文生视频/Krea2极清生图神器｜一句灵感直达惊艳大片质感｜文生视频图生视频_2099127688740036610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/▶▷Krea2-极清生图流_2098429137626161153.json、图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json、图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json、图片生成/文生图/▶▷Krea2-极清生图流_2112007776892440578.json、图片生成/文生图/▶▷Krea2-标准生图)_2077775542920769537.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 7/8 个有
- `LatentUpscaleBy` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `LoadLatent` —— 6/8 个有
- `SaveLatent` —— 6/8 个有
- `JjkText` —— 3/8 个有
- `Label (rgthree)` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `solarL_SaveImagesToZip` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 80 - 1024 | 8 | 31% |
| 高度 | 1024 | 80 - 1280 | 8 | 30% |
| 采样步数 | 4 | 4 - 10 | 8 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 27% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 0.77 | 0.54 - 1 | 8 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 31%
- 高度 中位数 1024，观测区间 80 - 1280，8 个样本，取值分散，一致性仅 30%
- 采样步数 中位数 4，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 0.77，观测区间 0.54 - 1，8 个样本
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足
