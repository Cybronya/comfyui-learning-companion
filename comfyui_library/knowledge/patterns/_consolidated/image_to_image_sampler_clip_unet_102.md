---
name: image_to_image_sampler_clip_unet_102
type: Image To Image
frequency: 5
level: strong
coverage: 0.9882
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json, 图片生成/图生图/模特手持产品生成V4_1957790299702788098.json, 图片生成/图生图/灰度_2061703047289589762.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json、图片生成/图生图/模特手持产品生成V4_1957790299702788098.json、图片生成/图生图/灰度_2061703047289589762.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `ModelSamplingFlux` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `FluxGuidance` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RH_Translator` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 24 - 25 | 5 | 98% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 5 | 61% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
