---
name: unknown_workflow_sampler_clip_unet_489
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, EmptyLatentImage, FluxGuidance, InjectLatentNoise+, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmasDenoise, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/pulid换脸_1983869528738332673.json, 平台全量/PuLID换脸_在线生图_1894973580826836993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_489

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/pulid换脸_1983869528738332673.json、平台全量/PuLID换脸_在线生图_1894973580826836993.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `InjectLatentNoise+`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmasDenoise`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `SUPIR_conditioner` —— 1/2 个有
- `SUPIR_decode` —— 1/2 个有
- `SUPIR_encode` —— 1/2 个有
- `SUPIR_first_stage` —— 1/2 个有
- `SUPIR_model_loader_v2` —— 1/2 个有
- `SUPIR_sample` —— 1/2 个有
- `Seed_` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | - | 2 | 93% |
| 高度 | 1344 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 960，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 高度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
