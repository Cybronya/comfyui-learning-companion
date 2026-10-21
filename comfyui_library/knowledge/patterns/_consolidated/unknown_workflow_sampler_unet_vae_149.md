---
name: unknown_workflow_sampler_unet_vae_149
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5938
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2108373842572959745.json, 图片生成/文生图/多图编辑工作流_2105329811446124546.json, 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_149

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json、图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json、图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2108373842572959745.json、图片生成/文生图/多图编辑工作流_2105329811446124546.json、图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `Text` —— 3/5 个有
- `忽略多组孤海` —— 3/5 个有
- `BatchImagesNode` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `TextGenerateLTX2Prompt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1152 | 5 | 95% |
| 高度 | 1024 | 1024 - 1536 | 5 | 82% |
| 采样步数 | 35 | 25 - 50 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1152，5 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 1024 - 1536，5 个样本，取值集中（一致性 82%）
- 采样步数 中位数 35，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
