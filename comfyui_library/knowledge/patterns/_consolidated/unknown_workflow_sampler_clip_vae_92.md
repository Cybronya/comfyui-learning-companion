---
name: unknown_workflow_sampler_clip_vae_92
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, Label (rgthree), LoadImage, ModelSamplingFlux, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, TextCombinerTwo, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/多头部视图角色表_1852013216225271809.json, 平台全量/莫奈花园_1853323618410242049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_92

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/多头部视图角色表_1852013216225271809.json、平台全量/莫奈花园_1853323618410242049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextCombinerTwo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `Int Literal` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy positive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | - | 1 | 100% |
| 宽度 | 832 | - | 1 | 100% |
| 高度 | 1216 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
