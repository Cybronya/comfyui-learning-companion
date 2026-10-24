---
name: unknown_workflow_sampler_clip_checkpoint_12
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8295
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell.json, comfyui-workflow-templates-json/sd3.5_large_blur.json, comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json, 图片生成/图生图/FLUX_InstantX_Canny_1902238464656433153.json, 图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json, 图片生成/图生图/Flux_Controlnet_Canny官方工作流_1930182640068935681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell.json、comfyui-workflow-templates-json/sd3.5_large_blur.json、comfyui-workflow-templates-json/sd3.5_large_canny_controlnet_example.json、图片生成/图生图/FLUX_InstantX_Canny_1902238464656433153.json、图片生成/图生图/Flux ControlNet-Union-Pro-2.0_1918244190503763969.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ControlNetLoader` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `Canny` —— 3/6 个有
- `ControlNetApplySD3` —— 3/6 个有
- `FluxGuidance` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `ControlNetApplyAdvanced` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `ImpactImageInfo` —— 1/6 个有
- `SetUnionControlNetType` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 32 | 6 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 26% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 0.66 | 0.4 - 1 | 5 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 32，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.66，观测区间 0.4 - 1，5 个样本
