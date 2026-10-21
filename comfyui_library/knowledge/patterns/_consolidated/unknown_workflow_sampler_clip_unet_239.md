---
name: unknown_workflow_sampler_clip_unet_239
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json, 图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_239

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/kera-2 文生图 _ 图生图 + gemma4 自动提示词工作流_2072549485133262849.json、图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextGenerate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 26% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
