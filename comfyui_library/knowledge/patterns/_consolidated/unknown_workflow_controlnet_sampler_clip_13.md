---
name: unknown_workflow_controlnet_sampler_clip_13
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.811
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json, 图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json, 图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/New Blur ControlNet Models for SD 3.5 Large_1862928933510426626.json、图片生成/图生图/New Canny ControlNet Models for SD 3.5 Large_1862926012681007106.json、图片生成/图生图/New Depth ControlNet Models for SD 3.5 Large_1862922937178238977.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Canny` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 5 | 3 | 89% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 5，3 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
