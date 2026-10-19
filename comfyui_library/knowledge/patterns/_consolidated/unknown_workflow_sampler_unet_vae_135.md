---
name: unknown_workflow_sampler_unet_vae_135
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7314
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/千问2.1！ 文生图！ 提示词自动优化！_2103393990568660994.json, 图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json, 数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json, 数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json, 数字人/数字人/千问2.1！ 文生图！ 提示词自动优化！_2101851079326658561.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/千问2.1！ 文生图！ 提示词自动优化！_2103393990568660994.json、图片生成/文生图/千问iamge2.1文生图_2102716967022063618.json、数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json、数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json、数字人/数字人/千问2.1！ 文生图！ 提示词自动优化！_2101851079326658561.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 50 | 25 - 50 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
