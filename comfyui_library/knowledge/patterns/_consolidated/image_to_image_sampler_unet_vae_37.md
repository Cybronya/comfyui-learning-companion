---
name: image_to_image_sampler_unet_vae_37
type: Image To Image
frequency: 7
level: moderate
coverage: 0.980571
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json, 图片生成/文生图/2031316609993805825.json, 图片生成/文生图/FLUX图生图（洗图）工作流_2048585634318651394.json, 图片生成/文生图/FLUX工作流_2100147250554040322.json, 图片生成/文生图/FLUX模型工作流搭建-文生图、图生图（洗图）_1962526879636959233.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json、图片生成/文生图/2031316609993805825.json、图片生成/文生图/FLUX图生图（洗图）工作流_2048585634318651394.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 4/7 个有
- `CLIPTextEncode` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `ModelSamplingFlux` —— 3/7 个有
- `ReferenceLatent` —— 3/7 个有
- `SetLatentNoiseMask` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 24 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 55% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 7 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 24，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，7 个样本
