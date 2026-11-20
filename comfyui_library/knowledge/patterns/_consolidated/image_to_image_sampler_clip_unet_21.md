---
name: image_to_image_sampler_clip_unet_21
type: Image To Image
frequency: 12
level: moderate
coverage: 0.867083
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json, 图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json, 图片生成/图生图/Flux2-Klein 图片高清放大 图生图_2081675636019654657.json, 图片生成/图生图/Flux2-Klein-9B-万物精修_2016119793451016194.json, 图片生成/图生图/Flux2-Klein-9B-毛坯图转效果图_2016119803773198338.json, 图片生成/图生图/Flux2-klein-万物精修（产品盒标贴一致性）_2036777306714279938.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2032355193949528065.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2037862676570836993.json, 图片生成/图生图/Flux2-klein-图像编辑（单图）_2037876044539109377.json, 图片生成/图生图/flux-2-klein-多图编辑工作流_2015764934323343361.json, 图片生成/图生图/flux2-klein编辑+高清修复_2013069939640377345.json, 图片生成/图生图/精修天花板Flux2-klein-万物精修_2017956716545056769.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json、图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json、图片生成/图生图/Flux2-Klein 图片高清放大 图生图_2081675636019654657.json、图片生成/图生图/Flux2-Klein-9B-万物精修_2016119793451016194.json、图片生成/图生图/Flux2-Klein-9B-毛坯图转效果图_2016119803773198338.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 11/12 个有
- `ReferenceLatent` —— 11/12 个有
- `ConditioningZeroOut` —— 9/12 个有
- `LatentUpscaleBy` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `FluxKontextImageScale` —— 4/12 个有
- `ImageResize+` —— 4/12 个有
- `easy imageColorMatch` —— 4/12 个有
- `ColorMatch` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 2/12 个有
- `Anything Everywhere` —— 1/12 个有
- `EmptyFlux2LatentImage` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `ImageCASharpening+` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 12 | 97% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 12 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，12 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，12 个样本，取值集中（一致性 81%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
