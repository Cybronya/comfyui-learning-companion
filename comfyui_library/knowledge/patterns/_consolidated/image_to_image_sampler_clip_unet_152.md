---
name: image_to_image_sampler_clip_unet_152
type: Image To Image
frequency: 3
level: weak
coverage: 0.912333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强图生·Qwen Image 正式登场！等你来推理、来挑战！_1953507024598388737.json, 图片生成/图生图/（洗图图生图效果很好）Z-Image_turbo图生图-又快又好_2101289951110459394.json, 图片生成/文生图/Z-Image-Turbo图生图_1994260211968000002.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强图生·Qwen Image 正式登场！等你来推理、来挑战！_1953507024598388737.json、图片生成/图生图/（洗图图生图效果很好）Z-Image_turbo图生图-又快又好_2101289951110459394.json、图片生成/文生图/Z-Image-Turbo图生图_1994260211968000002.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 20 | 3 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.58 | 0.5 - 1 | 3 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.58，观测区间 0.5 - 1，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
