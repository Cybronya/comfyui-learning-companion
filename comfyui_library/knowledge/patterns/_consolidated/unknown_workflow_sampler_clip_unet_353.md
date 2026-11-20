---
name: unknown_workflow_sampler_clip_unet_353
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.868333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, ModelSamplingAuraFlow, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_image 图生图_1993271845350735874.json, 图片生成/文生图/Qwen3反推洗图_Z_image_seedvr2_1994317011379568642.json, 图片生成/文生图/Qwen_image 文生图_1993266820811603970.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_353

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen_image 图生图_1993271845350735874.json、图片生成/文生图/Qwen3反推洗图_Z_image_seedvr2_1994317011379568642.json、图片生成/文生图/Qwen_image 文生图_1993266820811603970.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `ImpactInt` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `CR Text Replace` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JWStringConcat` —— 1/3 个有
- `LoadLoraOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 3 | 94% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，3 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
