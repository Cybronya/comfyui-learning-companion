---
name: unknown_workflow_sampler_unet_vae_152
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.75
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json, 图片生成/文生图/qwen2.1文生图_2104275580962304002.json, 图片生成/文生图/多图编辑工作流_2105329811446124546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json、图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json、图片生成/文生图/qwen2.1文生图_2104275580962304002.json、图片生成/文生图/多图编辑工作流_2105329811446124546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `Text` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1152 | 4 | 95% |
| 高度 | 1024 | 1024 - 1536 | 4 | 81% |
| 采样步数 | 30 | 25 - 50 | 4 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1152，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1536，4 个样本，取值集中（一致性 81%）
- 采样步数 中位数 30，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
