---
name: unknown_workflow_sampler_clip_unet_518
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9475
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-turbo 文生图 细节增加_1982805138127630338.json, 图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_518

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo 文生图 细节增加_1982805138127630338.json、图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailDaemonSamplerNode` —— 1/2 个有
- `FastFilmGrain` —— 1/2 个有
- `FastLaplacianSharpen` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1180 | - | 2 | 92% |
| 高度 | 1740 | - | 2 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1180，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1740，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
