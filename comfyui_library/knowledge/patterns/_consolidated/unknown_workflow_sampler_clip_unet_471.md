---
name: unknown_workflow_sampler_clip_unet_471
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7755
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/自动词优化版Moss-image Sft文生图_2112123208332824577.json, 图片生成/文生图/（自用-贞贞版）Moss-image Sft Fixed文生图_2112438870972387329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_471

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/自动词优化版Moss-image Sft文生图_2112123208332824577.json、图片生成/文生图/（自用-贞贞版）Moss-image Sft Fixed文生图_2112438870972387329.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
