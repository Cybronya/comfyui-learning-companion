---
name: unknown_workflow_upscale_lora_sampler_114
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8575
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, PresetTextSelector, PrimitiveStringMultiline, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, VAEDecode, easy promptConcat]
problems: []
missing: []
members: [图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json, 图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image  SeedVR2.5.1写实AI短剧定妆照文生图_2013072564117049346.json、图片生成/文生图/Z-image + SeedVR2.5.1 超真实感 AI短剧 定妆照 文生图_2010364235049603074.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `PresetTextSelector`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `VAEDecode`
- `easy promptConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
