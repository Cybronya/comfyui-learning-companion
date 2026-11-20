---
name: unknown_workflow_sampler_clip_vae_91
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.637
common_nodes: [Anything Everywhere3, ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, GetNode, ImageConcatMulti, ImageScale, InFluxModelSamplingPred, LoadImage, OutFluxModelSamplingPred, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, SaveImage, SetNode, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/人像写真切换造型风格_1851215157744783362.json, 平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_91

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人像写真切换造型风格_1851215157744783362.json、平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `GetNode`
- `ImageConcatMulti`
- `ImageScale`
- `InFluxModelSamplingPred`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AutoCropFaces` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `Image Flip` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextCombinerTwo` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832x1152 (0.72) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 832x1152 (0.72)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
