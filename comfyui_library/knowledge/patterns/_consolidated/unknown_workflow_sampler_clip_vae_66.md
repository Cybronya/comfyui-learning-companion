---
name: unknown_workflow_sampler_clip_vae_66
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.875
common_nodes: [CLIPTextEncodeSDXLRefiner, EmptyLatentImage, KSampler, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/文生图工作流_2054883897737007106.json, 图片生成/文生图/文生图教学版_2054741592807878658.json, 图片生成/文生图/简易版文生图工作流_2053105946179715074.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生图工作流_2054883897737007106.json、图片生成/文生图/文生图教学版_2054741592807878658.json、图片生成/文生图/简易版文生图工作流_2053105946179715074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeSDXLRefiner`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 768 - 1024 | 3 | 87% |
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 5 | 5 - 8 | 3 | 76% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.8 | 0.8 - 1 | 3 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 8，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.8，观测区间 0.8 - 1，3 个样本，取值集中（一致性 89%）
