---
name: image_to_image_sampler_clip_unet_46
type: Image To Image
frequency: 10
level: strong
coverage: 0.8813
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein-单图编辑_2064942255387013122.json, 图片生成/图生图/cos替换-klein9b_2029474740787748866.json, 图片生成/图生图/flux-2-klein-单图编辑工作流_2015742060871028738.json, 图片生成/图生图/flux-Klein-OpenPose姿势参考_2016816089824501761.json, 图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json, 图片生成/图生图/产品草图快速渲染工作流_2105565676927799297.json, 图片生成/文生图/FLUX板块：FLUX2-Klein单图编辑工作流_2050044921289166849.json, 图片生成/文生图/FLUX板块：FLUX2-Klein多图编辑工作流_2050045080513327106.json, 图片生成/文生图/Flux2-klein-单图编辑(True-V2)_2050760183818801154.json, 图片生成/文生图/Flux2-klein-单图编辑(new)_2048265964101308417.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Klein-单图编辑_2064942255387013122.json、图片生成/图生图/cos替换-klein9b_2029474740787748866.json、图片生成/图生图/flux-2-klein-单图编辑工作流_2015742060871028738.json、图片生成/图生图/flux-Klein-OpenPose姿势参考_2016816089824501761.json、图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `PreviewImage` —— 6/10 个有
- `EmptyFlux2LatentImage` —— 5/10 个有
- `GetImageSize` —— 4/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `LatentUpscaleBy` —— 3/10 个有
- `ImageResize+` —— 2/10 个有
- `LayerUtility: ImageReel` —— 2/10 个有
- `LayerUtility: ImageReelComposit` —— 2/10 个有
- `LoraLoader` —— 2/10 个有
- `Flux2KleinEnhancer` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 2 - 8 | 10 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 2 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
