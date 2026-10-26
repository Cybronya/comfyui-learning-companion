---
name: text_to_image_upscale_sampler_clip_26
type: Text To Image
frequency: 4
level: strong
coverage: 0.681
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json, 图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json, 图片生成/文生图/z-image文生图_2055928133613826049.json, 图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json、图片生成/文生图/z-image文生图+全节点注释_2055922381788598273.json、图片生成/文生图/z-image文生图_2055928133613826049.json、图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `FluxResolutionNode` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy promptList` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1080 | 4 | 85% |
| 高度 | 1536 | 1280 - 1920 | 4 | 85% |
| 采样步数 | 8.5 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.9 | 0.8 - 1 | 4 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1080，4 个样本，取值集中（一致性 85%）
- 高度 中位数 1536，观测区间 1280 - 1920，4 个样本，取值集中（一致性 85%）
- 采样步数 中位数 8.5，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.8 - 1，4 个样本，取值集中（一致性 89%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
