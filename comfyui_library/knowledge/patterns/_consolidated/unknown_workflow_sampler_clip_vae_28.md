---
name: unknown_workflow_sampler_clip_vae_28
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93325
common_nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [String Literal, easy seed]
members: [图片生成/文生图/04.WAN2.2-文生图-nf_1991131479682166785.json, 图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json, 图片生成/文生图/1950527410125066242.json, 图片生成/文生图/1950849465034940417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/04.WAN2.2-文生图-nf_1991131479682166785.json、图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json、图片生成/文生图/1950527410125066242.json、图片生成/文生图/1950849465034940417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `UNETLoader` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 4 | 62% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.75 | 0.5 - 1 | 4 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.75，观测区间 0.5 - 1，4 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy seed
