---
name: unknown_workflow_sampler_clip_unet_135
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.902333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json, 图片生成/文生图/全量版Z_IMAGE文生图工作流_2068260369071689729.json, 图片生成/文生图/关键帧生成_2069402773254397953.json, 图片生成/文生图/加速版文生图WAN2.2_1955257152644550657.json, 图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json, 图片生成/文生图/千问大模型Z_Image 文生图大模型（目前最真实）_1994767919693410305.json, 图片生成/文生图/千问文生图-海报制造机器_1954172979645181954.json, 图片生成/文生图/千问文生图工作流_1980117131083812865.json, 图片生成/文生图/大凯辰光-潜水亚洲审美模型Z_image_turbo-UltraFluxVAE高清直出-文生图工作流_2009840006055071746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json、图片生成/文生图/全量版Z_IMAGE文生图工作流_2068260369071689729.json、图片生成/文生图/关键帧生成_2069402773254397953.json、图片生成/文生图/加速版文生图WAN2.2_1955257152644550657.json、图片生成/文生图/千问-qwen2512-image-文生图工作流_2008014250991685634.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/9 个有
- `LoadImage` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `CFGNorm` —— 1/9 个有
- `FluxGuidance` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `MemoryCleaner` —— 1/9 个有
- `easy hiresFix` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 9 | 61% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 9 | 51% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
