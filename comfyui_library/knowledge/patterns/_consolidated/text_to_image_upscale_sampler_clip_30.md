---
name: text_to_image_upscale_sampler_clip_30
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/iL、Pony、XL通用基础文生图工作流_2040618537173127170.json, 图片生成/文生图/iL、Pony、XL通用基础文生图工作流，简洁高效出图_1934957385754550274.json, 图片生成/文生图/文生图-并放大图片工作流_1934952424287182850.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/iL、Pony、XL通用基础文生图工作流_2040618537173127170.json、图片生成/文生图/iL、Pony、XL通用基础文生图工作流，简洁高效出图_1934957385754550274.json、图片生成/文生图/文生图-并放大图片工作流_1934952424287182850.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `FaceDetailer` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `UltralyticsDetectorProvider` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 8 | 3 | 71% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 512 - 720 | 3 | 85% |
| 高度 | 1280 | 512 - 1280 | 3 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 8，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 512 - 720，3 个样本，取值集中（一致性 85%）
- 高度 中位数 1280，观测区间 512 - 1280，3 个样本
