---
name: unknown_workflow_sampler_unet_vae_188
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.821333
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json, 图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json, 图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 PE 文生图（优化版）_2102388624821153793.json、图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json、图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `QwenPECanvasT8` —— 1/3 个有
- `QwenPERewriteT8` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
