---
name: text_to_image_upscale_sampler_clip_20
type: Text To Image
frequency: 4
level: moderate
coverage: 0.8665
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen文生图+真实感+8K高清_1994701699338080257.json, 图片生成/文生图/Qwen文生图真实感_1991384108102430721.json, 图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json, 图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen文生图+真实感+8K高清_1994701699338080257.json、图片生成/文生图/Qwen文生图真实感_1991384108102430721.json、图片生成/文生图/Z-Image_tuibo_bf16工作流合集_1993872840260861954.json、图片生成/文生图/工作流千问篇6-Qwen千问QwenZ-Image模型_2026202728204083201.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `easy promptList` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 976 | 928 - 1024 | 4 | 95% |
| 高度 | 1600 | 1536 - 1664 | 4 | 96% |
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | res_2m | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 0.9 | 0.8 - 1 | 4 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 976，观测区间 928 - 1024，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1600，观测区间 1536 - 1664，4 个样本，取值集中（一致性 96%）
- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 res_2m，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 0.9，观测区间 0.8 - 1，4 个样本，取值集中（一致性 89%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
