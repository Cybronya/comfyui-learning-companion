---
name: unknown_workflow_sampler_clip_vae_16
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.828667
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1930274381468176385.json, 图片生成/文生图/1930275054787969025.json, 图片生成/文生图/1934213208926285826.json, 图片生成/文生图/1953166220825718786.json, 图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json, 图片生成/文生图/Z_image_turbo文生图原版工作流-B站UP主@好奇漫步_1995897359357919233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1930274381468176385.json、图片生成/文生图/1930275054787969025.json、图片生成/文生图/1934213208926285826.json、图片生成/文生图/1953166220825718786.json、图片生成/文生图/Z-Image-Turbo-文生图_2013422713167155201.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/6 个有
- `ModelSamplingSD3` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `CLIPLoader` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `QuadrupleCLIPLoader` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `LayerMask: BiRefNetUltra` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 8 - 50 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 6 | 11% |
| 采样算法 | lcm | - | 6 | 33% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 24，观测区间 8 - 50，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，6 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 lcm，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
