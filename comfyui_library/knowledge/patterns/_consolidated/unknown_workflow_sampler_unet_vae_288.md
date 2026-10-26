---
name: unknown_workflow_sampler_unet_vae_288
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.544333
common_nodes: [CLIPLoader, EmptyLatentImage, GetNode, KSampler, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json, 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json, 图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_288

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-image2.1 空间折叠流之太虚生成_2103043423883321346.json、图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json、图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `StringConstantMultiline` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `ImpactInt` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 50 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
