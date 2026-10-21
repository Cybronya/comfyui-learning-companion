---
name: text_to_image_upscale_sampler_clip_19
type: Text To Image
frequency: 4
level: moderate
coverage: 0.764
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKVCache, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LatentColorMatchSimple, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-大图专用 蓝神大佬优化 1600万像素_2071508472050577410.json, 图片生成/文生图/Krea2-文生图直出4K （效果惊人不输闭源）_2071588832386052097.json, 图片生成/文生图/krea2json格式图生图像百万像素_2071963341316255746.json, 图片生成/文生图/krea2json格式文生图像百万像素_2072007993671114754.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-大图专用 蓝神大佬优化 1600万像素_2071508472050577410.json、图片生成/文生图/Krea2-文生图直出4K （效果惊人不输闭源）_2071588832386052097.json、图片生成/文生图/krea2json格式图生图像百万像素_2071963341316255746.json、图片生成/文生图/krea2json格式文生图像百万像素_2072007993671114754.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKVCache`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentColorMatchSimple`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `Text` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy showAnything` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1360 | 1360 - 1360 | 4 | 100% |
| 高度 | 2048 | 2048 - 2048 | 4 | 100% |
| 采样步数 | 6 | 6 - 8 | 4 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.35 | 0.2 - 1 | 4 | 31% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1360，观测区间 1360 - 1360，4 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 6 - 8，4 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.35，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 31%
- 高发问题（10/4 个样本）：Steps较低可能导致细节不足
