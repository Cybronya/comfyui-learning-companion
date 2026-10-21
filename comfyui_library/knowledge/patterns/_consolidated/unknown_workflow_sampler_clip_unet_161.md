---
name: unknown_workflow_sampler_clip_unet_161
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.97925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image批量文生图_1993908239676932097.json, 图片生成/文生图/Z-image-base文生图_2019404038776823810.json, 图片生成/文生图/Z-image-base文生图_2020836862188851201.json, 图片生成/文生图/Z-image-turbo-t2i_2073765816608313345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image批量文生图_1993908239676932097.json、图片生成/文生图/Z-image-base文生图_2019404038776823810.json、图片生成/文生图/Z-image-base文生图_2020836862188851201.json、图片生成/文生图/Z-image-turbo-t2i_2073765816608313345.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/4 个有
- `Bookmark (rgthree)` —— 1/4 个有
- `CompressImages` —— 1/4 个有
- `FromListGet1Image` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 38 | 4 | 16% |
| Prompt 约束强度(CFG) | 2 | 1 - 8 | 4 | 12% |
| 采样算法 | res_multistep | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 4 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 38，4 个样本，取值分散，一致性仅 16%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 8，4 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 res_multistep，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，4 个样本，取值集中（一致性 96%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
