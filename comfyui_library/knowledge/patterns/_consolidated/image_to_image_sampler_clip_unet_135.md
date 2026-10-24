---
name: image_to_image_sampler_clip_unet_135
type: Image To Image
frequency: 3
level: strong
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json, 图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json, 图片生成/图生图/Flux2-klein-9b 局部重绘-万物迁移_2015984171918827522.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json、图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json、图片生成/图生图/Flux2-klein-9b 局部重绘-万物迁移_2015984171918827522.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `Mask To Image (mtb)` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
