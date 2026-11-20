---
name: unknown_workflow_sampler_clip_checkpoint_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.848
common_nodes: [CLIPTextEncode, CR Simple Image Compare, CheckpointLoaderSimple, ConditioningZeroOut, DisplayText_Zho, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, KSampler, LayerUtility: PurgeVRAM, PreviewImage, RH_Prompter, SDXLAspectRatioSelector, SaveImage, SeargePromptText, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json, 图片生成/文生图/OpenFlux vs Flux_1843662142867197954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json、图片生成/文生图/OpenFlux vs Flux_1843662142867197954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DisplayText_Zho`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `RH_Prompter`
- `SDXLAspectRatioSelector`
- `SaveImage`
- `SeargePromptText`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 97% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
