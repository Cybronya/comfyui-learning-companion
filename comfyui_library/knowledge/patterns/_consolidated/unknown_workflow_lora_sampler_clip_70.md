---
name: unknown_workflow_lora_sampler_clip_70
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.932625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/003.FLUX.2智能综合002.文生图标准流_2035170236101562369.json, 图片生成/文生图/5.其他类型-06.NSF+-06.FLUX.2-010.flux-2-klein-文生图标准流_2026630137671852033.json, 图片生成/文生图/ERNIE+结构化提示词海报风格增强_2074133568149868546.json, 图片生成/文生图/ERNIE-Image-Turbo文生图_2063975108284346370.json, 图片生成/文生图/ERNIE-Image-Turbo文生图艺术字设计_2052935133627465729.json, 图片生成/文生图/F01.文生图标准流_2061325864108908545.json, 图片生成/文生图/MOSS-4步文生图_2115254302515220482.json, 图片生成/文生图/flux-2-klein-文生图标准流_2040040486324408321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/003.FLUX.2智能综合002.文生图标准流_2035170236101562369.json、图片生成/文生图/5.其他类型-06.NSF+-06.FLUX.2-010.flux-2-klein-文生图标准流_2026630137671852033.json、图片生成/文生图/ERNIE+结构化提示词海报风格增强_2074133568149868546.json、图片生成/文生图/ERNIE-Image-Turbo文生图_2063975108284346370.json、图片生成/文生图/ERNIE-Image-Turbo文生图艺术字设计_2052935133627465729.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `EasySizeSimpleSetting` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `RAMCleanup` —— 1/8 个有
- `TTResolutionSelector` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
