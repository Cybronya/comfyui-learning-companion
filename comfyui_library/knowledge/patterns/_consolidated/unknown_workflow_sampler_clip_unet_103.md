---
name: unknown_workflow_sampler_clip_unet_103
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree)]
members: [图片生成/文生图/1982805138127630338.json, 图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_103

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1982805138127630338.json、图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FastFilmGrain` —— 1/2 个有
- `FastLaplacianSharpen` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |
| 采样步数 | 9 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1.4 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.86 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
