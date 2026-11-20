---
name: text_to_image_upscale_lora_sampler_46
type: Text To Image
frequency: 6
level: weak
coverage: 0.810667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS文生图+全节点注释_2112471507770372097.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json, 图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2113461455063441409.json, 图片生成/文生图/MOSS文生图加VOSR放大组合｜文生黑马出图再超分一步到位_2113522691427880962.json, 图片生成/文生图/MOSS文生图黑马VOSR放大 8步极速图像生成工具_2113703027365470209.json, 数字人/数字人/图像高清放大工作流｜Vosr2数字人图片画质增强_2097525104493293570.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/MOSS文生图+全节点注释_2112471507770372097.json、图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2111999115608547329.json、图片生成/文生图/MOSS文生图_文生黑马_VOSR放大_2113461455063441409.json、图片生成/文生图/MOSS文生图加VOSR放大组合｜文生黑马出图再超分一步到位_2113522691427880962.json、图片生成/文生图/MOSS文生图黑马VOSR放大 8步极速图像生成工具_2113703027365470209.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `MuyeTextEditOutput` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SkipLayerGuidanceDiTSimple` —— 5/6 个有
- `JjkText` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `EmptyImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 6 | 36% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 552 | 80 - 1024 | 6 | 14% |
| 高度 | 552 | 80 - 1024 | 6 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 552，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 14%
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
