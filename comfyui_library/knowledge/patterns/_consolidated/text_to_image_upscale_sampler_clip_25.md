---
name: text_to_image_upscale_sampler_clip_25
type: Text To Image
frequency: 4
level: weak
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen文生图+真实感+8K高清_1994701699338080257.json, 图片生成/文生图/Qwen文生图真实感_1991384108102430721.json, 图片生成/文生图/Z image_1984983374504804353.json, 图片生成/文生图/Z-Image Turbo 图像放大和细节处理_2051922049270071297.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen文生图+真实感+8K高清_1994701699338080257.json、图片生成/文生图/Qwen文生图真实感_1991384108102430721.json、图片生成/文生图/Z image_1984983374504804353.json、图片生成/文生图/Z-Image Turbo 图像放大和细节处理_2051922049270071297.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageScaleBy` —— 2/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 928 | 768 - 1280 | 4 | 81% |
| 高度 | 1344 | 720 - 1664 | 4 | 68% |
| 采样步数 | 17 | 9 - 25 | 4 | 53% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | res_2m | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 0.625 | 0.15 - 1 | 4 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 928，观测区间 768 - 1280，4 个样本，取值集中（一致性 81%）
- 高度 中位数 1344，观测区间 720 - 1664，4 个样本
- 采样步数 中位数 17，观测区间 9 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 res_2m，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 0.625，观测区间 0.15 - 1，4 个样本，取值分散，一致性仅 33%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
