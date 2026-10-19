---
name: text_to_image_upscale_sampler_clip_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.98
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1984983374504804353.json, 图片生成/文生图/1988895729412354050.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1984983374504804353.json、图片生成/文生图/1988895729412354050.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CFGNorm` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.575 | - | 2 | 26% |
| 宽度 | 1152 | - | 2 | 67% |
| 高度 | 1536 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 宽度 中位数 1152，样本不足，未给区间，2 个样本
- 高度 中位数 1536，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
