---
name: unknown_workflow_upscale_sampler_clip_52
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7515
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, FluxGuidance, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingFlux, SaveImage, SetNode, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/瓷器-放大_2033082316158935042.json, 图片生成/图生图/高清放大_2038689591447789570.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/瓷器-放大_2033082316158935042.json、图片生成/图生图/高清放大_2038689591447789570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingFlux`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
