---
name: text_to_image_ipadapter_upscale_sampler_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.967
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Latent Input Switch, CheckpointLoaderSimple, ConditioningZeroOut, DetailTransfer, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, FaceAlign, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GrowMaskWithBlur, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageColorTransfer, ImageCompositeMasked, ImageScale, Joy_caption, Joy_caption_load, KSampler, KSamplerSelect, LayerMask: CreateGradientMask, LayerMask: PersonMaskUltra V2, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/摄影艺术写真换脸大师-StarAI_1892457955365707778.json, 平台全量/摄影艺术写真换脸大师_1913455066412711938.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/摄影艺术写真换脸大师-StarAI_1892457955365707778.json、平台全量/摄影艺术写真换脸大师_1913455066412711938.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Latent Input Switch`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceAlign`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageColorTransfer`
- `ImageCompositeMasked`
- `ImageScale`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: CreateGradientMask`
- `LayerMask: PersonMaskUltra V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
