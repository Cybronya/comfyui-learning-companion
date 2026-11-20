---
name: text_to_image_sampler_clip_checkpoint_17
type: Text To Image
frequency: 4
level: moderate
coverage: 0.712
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image文生图支持LORA以及细节增强_2016028625149104130.json, 图片生成/文生图/z-image-turbo-aio-课程对应工作流____1998300993865547778.json, 图片生成/文生图/z-image-文生图_2013815667270619137.json, 图片生成/文生图/▶▷Krea2-高清生图AIO_2077747265082585089.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image文生图支持LORA以及细节增强_2016028625149104130.json、图片生成/文生图/z-image-turbo-aio-课程对应工作流____1998300993865547778.json、图片生成/文生图/z-image-文生图_2013815667270619137.json、图片生成/文生图/▶▷Krea2-高清生图AIO_2077747265082585089.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LatentUpscaleBy` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `Label (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 3 - 10 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_multistep | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.775 | 0.55 - 1 | 4 | 71% |
| 宽度 | 1152 | 768 - 1152 | 4 | 84% |
| 高度 | 1736 | 1280 - 1736 | 4 | 88% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 3 - 10，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.775，观测区间 0.55 - 1，4 个样本
- 宽度 中位数 1152，观测区间 768 - 1152，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1736，观测区间 1280 - 1736，4 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
