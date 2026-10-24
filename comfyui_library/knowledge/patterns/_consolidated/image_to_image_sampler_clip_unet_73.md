---
name: image_to_image_sampler_clip_unet_73
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9015
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json, 图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json, 图片生成/图生图/Flux2 Klein_2055322613999783938.json, 图片生成/图生图/Flux2-Klein-图片编辑 (单图)_2028867735513468929.json, 图片生成/图生图/Flux2-Klein-扩图_2058461347406503937.json, 图片生成/图生图/Flux2-Klein-扩图_2087947080038969345.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux.2-Klein图生图洗图工作流_2075029554900586497.json、图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json、图片生成/图生图/Flux2 Klein_2055322613999783938.json、图片生成/图生图/Flux2-Klein-图片编辑 (单图)_2028867735513468929.json、图片生成/图生图/Flux2-Klein-扩图_2058461347406503937.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `GetImageSize` —— 4/6 个有
- `ImagePadForOutpaint` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `Seed (rgthree)` —— 3/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `Image Blank` —— 2/6 个有
- `ImageCompositeMasked` —— 2/6 个有
- `JoinImageWithAlpha` —— 2/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageScaleToMaxDimension` —— 1/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 6 | 73% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
