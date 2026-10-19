---
name: unknown_workflow_sampler_clip_unet_95
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7685
common_nodes: [BasicScheduler, CFGGuider, CFGZeroStarAndInit, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1904911641337860097.json, 图片生成/文生图/通用文生图Zero_1892035886346047490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1904911641337860097.json、图片生成/文生图/通用文生图Zero_1892035886346047490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CFGZeroStarAndInit`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CompileModel` —— 1/2 个有
- `DetailDaemonGraphSigmasNode` —— 1/2 个有
- `DetailDaemonSamplerNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
