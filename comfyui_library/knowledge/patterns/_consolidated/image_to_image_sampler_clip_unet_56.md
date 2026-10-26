---
name: image_to_image_sampler_clip_unet_56
type: Image To Image
frequency: 7
level: moderate
coverage: 0.892429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json, 图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json, 图片生成/图生图/Flux 2 Klein 9B Edit_2063304186351149058.json, 图片生成/图生图/Flux-2 Klein 双图编辑_2093268073829724161.json, 图片生成/图生图/Flux-2-klein-多图精准控制编辑工作流-万能贴_2016050666283732994.json, 图片生成/图生图/Flux2 Klein_2055322613999783938.json, 图片生成/图生图/flux-2klein单图_多图编辑_2038533995062890497.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json、图片生成/图生图/FLUX板块：FLUX.2-Klein图洗图工作流_2049795289871073281.json、图片生成/图生图/Flux 2 Klein 9B Edit_2063304186351149058.json、图片生成/图生图/Flux-2 Klein 双图编辑_2093268073829724161.json、图片生成/图生图/Flux-2-klein-多图精准控制编辑工作流-万能贴_2016050666283732994.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ReferenceLatent` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `EmptyFlux2LatentImage` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `BiRefNetRMBG` —— 1/7 个有
- `FastCanvas` —— 1/7 个有
- `FastCanvasTool` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `ImageScaleToMaxDimension` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
