---
name: text_to_image_sampler_clip_unet_12
type: Text To Image
frequency: 21
level: weak
coverage: 0.852524
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-风情万种_写实人像（双采版）_2071459488988749825.json, 图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json, 图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json, 图片生成/文生图/Krea2_写实人像_2083068524297277442.json, 图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json, 图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json, 图片生成/文生图/Krea2_写实人像（双采版）_2079377240273547266.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087070012069736450.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087380793143422978.json, 图片生成/文生图/Krea2文生图-MJ影视柔光_2109529285030670338.json, 图片生成/文生图/Krea2文生图_2095904097835765761.json, 图片生成/文生图/Krea2文生图极简工作流｜输入描述直接出高质量图_2107649169803534338.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成_2098834148222914561.json, 图片生成/文生图/Krea2极清生图流 高清写实风格图片生成工作流_2098711426352377857.json, 图片生成/文生图/Krea2极清画质文生图工作流｜写实高清放大一步到位_2098698482818314242.json, 图片生成/文生图/▶▷Krea2-极清生图流_2098429137626161153.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099309892925485057.json, 图片生成/文生图/▶▷Krea2-极清生图流_2099663087610712065.json, 视频生成/文生视频/Krea2 极清生图｜从一句灵感，到惊艳大片_2098733373807218689.json, 视频生成/文生视频/Krea2极清灵感生图 从文字到惊艳大片_2098843566570299393.json, 视频生成/文生视频/Krea2极清生图神器｜一句灵感直达惊艳大片质感｜文生视频图生视频_2099127688740036610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/Krea2-风情万种_写实人像（双采版）_2071459488988749825.json、图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json、图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json、图片生成/文生图/Krea2_写实人像_2083068524297277442.json、图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 10/21 个有
- `LoraLoaderModelOnly` —— 10/21 个有
- `PreviewImage` —— 10/21 个有
- `Seed (rgthree)` —— 10/21 个有
- `KSamplerAdvanced` —— 9/21 个有
- `LatentUpscaleBy` —— 9/21 个有
- `LoadLatent` —— 9/21 个有
- `PrimitiveStringMultiline` —— 9/21 个有
- `SaveLatent` —— 9/21 个有
- `孤海注释` —— 9/21 个有
- `JjkText` —— 7/21 个有
- `solarL_SaveImagesToZip` —— 7/21 个有
- `Label (rgthree)` —— 1/21 个有
- `RH_Translator` —— 1/21 个有
- `easy anythingIndexSwitch` —— 1/21 个有
- `easy promptLine` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 21 | 36% |
| 高度 | 1024 | 80 - 1024 | 21 | 37% |
| 采样步数 | 4 | 4 - 12 | 21 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 21 | 24% |
| 采样算法 | euler | - | 21 | 62% |
| 调度器 | simple | - | 21 | 33% |
| 重绘幅度 | 1 | 0.4 - 1 | 21 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 37/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 36%
- 高度 中位数 1024，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 37%
- 采样步数 中位数 4，观测区间 4 - 12，21 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，21 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，21 个样本，一致性 62%
- 调度器 最常用 simple，21 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，21 个样本
- 高发问题（37/21 个样本）：Steps较低可能导致细节不足
