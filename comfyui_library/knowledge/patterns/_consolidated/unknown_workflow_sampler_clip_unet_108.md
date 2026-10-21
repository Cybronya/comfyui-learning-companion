---
name: unknown_workflow_sampler_clip_unet_108
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.940167
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1914548552176205826.json, 图片生成/文生图/1955386783511056385.json, 图片生成/文生图/1956995525369323522.json, 图片生成/文生图/5.其他类型-06.NSF+-06.FLUX.2-010.flux-2-klein-文生图标准流_2026630137671852033.json, 图片生成/文生图/ERNIE+结构化提示词海报风格增强_2074133568149868546.json, 图片生成/文生图/F01.文生图标准流_2061325864108908545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1914548552176205826.json、图片生成/文生图/1955386783511056385.json、图片生成/文生图/1956995525369323522.json、图片生成/文生图/5.其他类型-06.NSF+-06.FLUX.2-010.flux-2-klein-文生图标准流_2026630137671852033.json、图片生成/文生图/ERNIE+结构化提示词海报风格增强_2074133568149868546.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 4/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `FlexLoraLoaderModelOnly` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 20 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 32% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 20，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
