---
name: text_to_image_sampler_clip_checkpoint_15
type: Text To Image
frequency: 2
level: weak
coverage: 0.7945
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PortraitMaster_中文版, SaveImage, VAEDecode]
problems: []
missing: [PortraitMaster_中文版, easy seed]
members: [图片生成/文生图/1906519526463442946.json, 图片生成/文生图/1928323196418670594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1906519526463442946.json、图片生成/文生图/1928323196418670594.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PortraitMaster_中文版`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1408 | - | 2 | 91% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：PortraitMaster_中文版、easy seed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
