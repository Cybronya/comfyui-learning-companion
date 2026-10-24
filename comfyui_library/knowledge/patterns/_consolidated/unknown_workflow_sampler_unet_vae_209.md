---
name: unknown_workflow_sampler_unet_vae_209
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.896
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, QwenPERewriteT8, ResolutionSelector, SaveImage, SaveImageAdvanced, Seed (rgthree), ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json, 图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json, 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json, 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json, 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_209

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json、图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json、图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json、图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json、图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2108444743310073857.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 4/5 个有
- `忽略多组孤海` —— 4/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
