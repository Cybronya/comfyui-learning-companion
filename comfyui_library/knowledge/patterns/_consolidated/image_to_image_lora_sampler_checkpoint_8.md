---
name: image_to_image_lora_sampler_checkpoint_8
type: Image To Image
frequency: 4
level: moderate
coverage: 0.857
common_nodes: [CFGNorm, CheckpointLoaderSimple, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json, 图片生成/图生图/千问图像编辑胸部增大工作流_2037865814640037889.json, 图片生成/图生图/胸部美化神器，一键变美！_2038145235640913922.json, 平台全量/QwenAIO扩图_1995064484635009026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json、图片生成/图生图/千问图像编辑胸部增大工作流_2037865814640037889.json、图片生成/图生图/胸部美化神器，一键变美！_2038145235640913922.json、平台全量/QwenAIO扩图_1995064484635009026.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `ImageStitch` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
