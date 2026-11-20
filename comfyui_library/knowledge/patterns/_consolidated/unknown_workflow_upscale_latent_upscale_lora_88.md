---
name: unknown_workflow_upscale_latent_upscale_lora_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8645
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, Crop Face, DualCLIPLoader, ImageResize+, KSamplerSelect, LatentUpscaleBy, Load RetinaFace, LoadImage, LoraLoader, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [平台全量/头像生成_毛毡风格_1990316193389178882.json, 平台全量/班味毛毡头像_1854055187294851074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/头像生成_毛毡风格_1990316193389178882.json、平台全量/班味毛毡头像_1854055187294851074.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `Crop Face`
- `DualCLIPLoader`
- `ImageResize+`
- `KSamplerSelect`
- `LatentUpscaleBy`
- `Load RetinaFace`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
