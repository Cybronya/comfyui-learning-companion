---
name: image_to_image_sampler_clip_unet_146
type: Image To Image
frequency: 3
level: moderate
coverage: 0.860333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2参考洗图_2095834326972846082.json, 图片生成/图生图/qwen编辑图片_1958176395472080898.json, 图片生成/图生图/最强图生·Qwen Image 正式登场！等你来推理、来挑战！_1953507024598388737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea2参考洗图_2095834326972846082.json、图片生成/图生图/qwen编辑图片_1958176395472080898.json、图片生成/图生图/最强图生·Qwen Image 正式登场！等你来推理、来挑战！_1953507024598388737.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 3 | 51% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
