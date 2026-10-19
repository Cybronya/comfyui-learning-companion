---
name: unknown_workflow_sampler_clip_checkpoint_17
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.908
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningCombine, ConditioningSetTimestepRange, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingSD3, SaveImage, TripleCLIPLoader, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SD3基础工作流_1807671903036354561.json, 图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SD3基础工作流_1807671903036354561.json、图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `ConditioningSetTimestepRange`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `TripleCLIPLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `HD UltimateSDUpscale` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 25% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
