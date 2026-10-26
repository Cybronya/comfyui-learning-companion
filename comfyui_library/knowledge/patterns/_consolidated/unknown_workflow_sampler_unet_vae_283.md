---
name: unknown_workflow_sampler_unet_vae_283
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.658333
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json, 图片生成/文生图/Qwen Image 2.1_2102977844501639169.json, 图片生成/文生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_283

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json、图片生成/文生图/Qwen Image 2.1_2102977844501639169.json、图片生成/文生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `easy int` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1536 | 3 | 80% |
| 采样步数 | 25 | 25 - 50 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，3 个样本
- 采样步数 中位数 25，观测区间 25 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
