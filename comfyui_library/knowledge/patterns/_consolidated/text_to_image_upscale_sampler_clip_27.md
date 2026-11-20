---
name: text_to_image_upscale_sampler_clip_27
type: Text To Image
frequency: 5
level: strong
coverage: 0.7448
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json, 图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json, 图片生成/文生图/z-image文生图_2055928133613826049.json, 图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json, 图片生成/文生图/文生图极速出图_2055890159673061377.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json、图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json、图片生成/文生图/z-image文生图_2055928133613826049.json、图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json、图片生成/文生图/文生图极速出图_2055890159673061377.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `FluxResolutionNode` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `easy promptList` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1080 | 5 | 83% |
| 高度 | 1536 | 1280 - 1920 | 5 | 84% |
| 采样步数 | 9 | 8 - 10 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 5 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1080，5 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1280 - 1920，5 个样本，取值集中（一致性 84%）
- 采样步数 中位数 9，观测区间 8 - 10，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 89%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
