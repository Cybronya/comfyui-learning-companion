---
name: unknown_workflow_sampler_clip_checkpoint_24
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, TripleCLIPLoader, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/01.SD3.5_文生图_1990215639241510914.json, 图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json, 图片生成/文生图/SD3基础工作流_1807671903036354561.json, 图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_24

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/01.SD3.5_文生图_1990215639241510914.json、图片生成/文生图/SD3.5文生图官方工作流FP16_1930199196047982593.json、图片生成/文生图/SD3基础工作流_1807671903036354561.json、图片生成/文生图/sd3.5_large Turbo版 官方文生图示例_1848727011702476802.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `TripleCLIPLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningCombine` —— 3/4 个有
- `ConditioningSetTimestepRange` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `ModelSamplingSD3` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `HD UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | 4 - 30 | 4 | 52% |
| Prompt 约束强度(CFG) | 4.975 | 1 - 5.5 | 4 | 55% |
| 采样算法 | dpmpp_2m | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，观测区间 4 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 4.975，观测区间 1 - 5.5，4 个样本
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
