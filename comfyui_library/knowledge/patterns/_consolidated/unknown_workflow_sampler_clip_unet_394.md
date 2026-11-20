---
name: unknown_workflow_sampler_clip_unet_394
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.965
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-turbo 文生图 细节增加_1982805138127630338.json, 图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json, 图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_394

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo 文生图 细节增加_1982805138127630338.json、图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json、图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailDaemonSamplerNode` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `FastFilmGrain` —— 1/3 个有
- `FastLaplacianSharpen` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1180 | - | 2 | 92% |
| 高度 | 1740 | - | 2 | 90% |
| 采样步数 | 9 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1.4 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.86 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1180，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1740，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
