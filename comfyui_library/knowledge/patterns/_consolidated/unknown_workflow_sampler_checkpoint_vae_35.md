---
name: unknown_workflow_sampler_checkpoint_vae_35
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CR Prompt Text, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, VAEDecode, ZenImageEditCheckpointLoader, ZenImageEditEncodeAdvanced, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Zen Image Edit图像编辑_2103757151029260289.json, 图片生成/图生图/Zen Image Edit图像编辑_2103820859654893569.json, 图片生成/图生图/Zen Image Edit图像编辑_2103823692970151937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Zen Image Edit图像编辑_2103757151029260289.json、图片生成/图生图/Zen Image Edit图像编辑_2103820859654893569.json、图片生成/图生图/Zen Image Edit图像编辑_2103823692970151937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `VAEDecode`
- `ZenImageEditCheckpointLoader`
- `ZenImageEditEncodeAdvanced`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
