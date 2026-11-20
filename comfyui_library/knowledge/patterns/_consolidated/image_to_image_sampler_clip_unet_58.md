---
name: image_to_image_sampler_clip_unet_58
type: Image To Image
frequency: 9
level: moderate
coverage: 0.978444
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json, 图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json, 图片生成/图生图/模特手持产品生成V4_1957790299702788098.json, 图片生成/图生图/灰度_2061703047289589762.json, 平台全量/Kontext 【一键生成】线稿 - IP形象 - IP三视图_1958349532503425025.json, 平台全量/KontextDev老照片修复_1941695983388672001.json, 平台全量/Kontext试衣间_1955449246726197249.json, 平台全量/万能贴（产品_场景融合）_1957677868362952705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2085355037840207873.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086262667588751362.json、图片生成/图生图/姿势锁定换衣｜局部遮罩换装工作流_2086272064624873474.json、图片生成/图生图/模特手持产品生成V4_1957790299702788098.json、图片生成/图生图/灰度_2061703047289589762.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
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
- `FluxGuidance` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `RH_Translator` —— 5/9 个有
- `EmptySD3LatentImage` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `FluxKontextImageScale` —— 3/9 个有
- `ModelSamplingFlux` —— 3/9 个有
- `SetLatentNoiseMask` —— 3/9 个有
- `StringFunction|pysssss` —— 2/9 个有
- `easy imageRemBg` —— 2/9 个有
- `FastCanvas` —— 1/9 个有
- `FastCanvasTool` —— 1/9 个有
- `GoogleTranslateTextNode` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 20 - 25 | 9 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 53% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 20 - 25，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
