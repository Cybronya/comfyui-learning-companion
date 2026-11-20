---
name: image_to_image_sampler_clip_unet_94
type: Image To Image
frequency: 6
level: strong
coverage: 0.868167
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json, 图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2015965598240477186.json, 图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2068640783539982338.json, 图片生成/图生图/Flux-2-klein-多图精准控制编辑工作流-万能贴_2016050666283732994.json, 平台全量/FLUX2-Klein指定区域重绘编辑工作流_2050080493185581058.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/F2_klein指定区域重绘_2056253513142988802.json、图片生成/图生图/FLUX2-Klein单图、多图编辑工作流_2068602290797375490.json、图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2015965598240477186.json、图片生成/图生图/FLUX2-Klein指定区域重绘编辑工作流_2068640783539982338.json、图片生成/图生图/Flux-2-klein-多图精准控制编辑工作流-万能贴_2016050666283732994.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageCompositeMasked` —— 4/6 个有
- `LayerUtility: ColorImage` —— 4/6 个有
- `取色器_孤海` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `BiRefNetRMBG` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `FastCanvas` —— 1/6 个有
- `FastCanvasTool` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
