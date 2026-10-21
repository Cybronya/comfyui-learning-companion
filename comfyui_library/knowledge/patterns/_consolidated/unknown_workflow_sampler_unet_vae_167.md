---
name: unknown_workflow_sampler_unet_vae_167
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.883
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json, 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json, 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json, 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json、图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json、图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json、数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
