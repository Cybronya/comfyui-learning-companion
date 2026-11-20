---
name: unknown_workflow_sampler_clip_unet_472
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8945
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, KSampler, ModelSamplingAuraFlow, SaveImage, Seed Generator, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, workflow>横屏]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZImage+Qwen3提示词反推_1996029746645549058.json, 图片生成/文生图/反推词image图生图洗图_2043516005657350145.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_472

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ZImage+Qwen3提示词反推_1996029746645549058.json、图片生成/文生图/反推词image图生图洗图_2043516005657350145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed Generator`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `workflow>横屏`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MultiplePathsInput` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | - | 2 | 94% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
