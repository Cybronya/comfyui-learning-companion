---
name: unknown_workflow_sampler_clip_vae_19
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9296
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/07.Flux_文生图_1993297490357190657.json, 图片生成/文生图/1938503902566506497.json, 图片生成/文生图/1952701907708088321.json, 图片生成/文生图/1954834253982908418.json, 图片生成/文生图/Flux+LoRA的文生图基础工作流_2001894494809276417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/07.Flux_文生图_1993297490357190657.json、图片生成/文生图/1938503902566506497.json、图片生成/文生图/1952701907708088321.json、图片生成/文生图/1954834253982908418.json、图片生成/文生图/Flux+LoRA的文生图基础工作流_2001894494809276417.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CheckpointLoaderSimple` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `DualCLIPLoaderGGUF` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `TeaCache` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
