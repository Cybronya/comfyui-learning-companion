---
name: unknown_workflow_sampler_unet_vae_215
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9288
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/▶Qwen-image21-生图_2112039123488960513.json, 图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json, 图片生成/文生图/千问2.1文生图_2101907864641167362.json, 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json, 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_215

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/▶Qwen-image21-生图_2112039123488960513.json、图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json、图片生成/文生图/千问2.1文生图_2101907864641167362.json、图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json、图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

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
- `SaveImageAdvanced` —— 3/5 个有
- `Text` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy promptList` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
