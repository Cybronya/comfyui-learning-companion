---
name: unknown_workflow_sampler_clip_vae_54
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93325
common_nodes: [CLIPTextEncodeFlux, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUx-gguf_1830883788774666242.json, 图片生成/文生图/flux1-gguf官方工作流_1930149940532559873.json, 图片生成/文生图/小红书风格美女奶大器_1994232545766211585.json, 图片生成/文生图/小红书风格美女生成，含增大器_1992532655405330433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_54

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUx-gguf_1830883788774666242.json、图片生成/文生图/flux1-gguf官方工作流_1930149940532559873.json、图片生成/文生图/小红书风格美女奶大器_1994232545766211585.json、图片生成/文生图/小红书风格美女生成，含增大器_1992532655405330433.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `DualCLIPLoaderGGUF` —— 2/4 个有
- `Lora Loader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 4 - 25 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 896 - 1024 | 4 | 94% |
| 高度 | 1344 | 1024 - 1536 | 4 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 4 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 896 - 1024，4 个样本，取值集中（一致性 94%）
- 高度 中位数 1344，观测区间 1024 - 1536，4 个样本，取值集中（一致性 83%）
