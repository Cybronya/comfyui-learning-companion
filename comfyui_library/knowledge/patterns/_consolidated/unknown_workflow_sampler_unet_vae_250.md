---
name: unknown_workflow_sampler_unet_vae_250
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.841
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json, 图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json, 图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json, 图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_250

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json、图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json、图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json、图片生成/文生图/文字生成图片（Qwen-Image 2.1）_2107738529978732546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `QwenPECanvasT8` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 25 | 4 | 89% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
