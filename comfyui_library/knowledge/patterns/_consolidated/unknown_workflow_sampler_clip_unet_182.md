---
name: unknown_workflow_sampler_clip_unet_182
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.854667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1979207949715410946.json, 图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json, 图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1979207949715410946.json、图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json、图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `TextCombinerSix` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 3 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，3 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio
