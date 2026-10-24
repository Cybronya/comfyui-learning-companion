---
name: image_to_image_sampler_clip_checkpoint_18
type: Image To Image
frequency: 2
level: weak
coverage: 0.817
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洗图工作流_2058731125362745345.json, 图片生成/文生图/klein4b-fp8_2019698941041840129.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/洗图工作流_2058731125362745345.json、图片生成/文生图/klein4b-fp8_2019698941041840129.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
