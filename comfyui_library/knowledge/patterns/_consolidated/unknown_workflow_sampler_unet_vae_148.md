---
name: unknown_workflow_sampler_unet_vae_148
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6522
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json, 图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json, 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json, 图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json, 图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_148

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json、图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json、图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json、图片生成/文生图/Qwen2.1文生图｜文生图图生图双模式｜出图稳定值得收藏_2102312649605341186.json、图片生成/文生图/心然·寻源-Qwen2.1文生图_2101891525948043265.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `StringConstantMultiline` —— 2/5 个有
- `TextGenerate` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 25 | 25 - 40 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
