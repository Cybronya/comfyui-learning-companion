---
name: unknown_workflow_sampler_clip_checkpoint_17
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.822667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell.json, comfyui-workflow-templates-json/sd3.5_large_blur.json, comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell.json、comfyui-workflow-templates-json/sd3.5_large_blur.json、comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `Canny` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 32 | 3 | 42% |
| Prompt 约束强度(CFG) | 4 | 1 - 4.5 | 3 | 51% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.83 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 32，3 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.83，样本不足，未给区间，2 个样本
