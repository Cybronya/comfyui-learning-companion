---
name: unknown_workflow_sampler_clip_vae_16
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.8276
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingSD3, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1930274381468176385.json, 图片生成/文生图/1930275054787969025.json, 图片生成/文生图/1934213208926285826.json, 图片生成/文生图/1953166220825718786.json, 图片生成/文生图/1956995525369323522.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1930274381468176385.json、图片生成/文生图/1930275054787969025.json、图片生成/文生图/1934213208926285826.json、图片生成/文生图/1953166220825718786.json、图片生成/文生图/1956995525369323522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `QuadrupleCLIPLoader` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `LoadImage` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 6 - 50 | 5 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 5 | 28% |
| 采样算法 | lcm | - | 5 | 40% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，观测区间 6 - 50，5 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，5 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 lcm，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
