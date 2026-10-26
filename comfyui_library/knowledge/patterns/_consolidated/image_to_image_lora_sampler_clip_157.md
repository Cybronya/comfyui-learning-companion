---
name: image_to_image_lora_sampler_clip_157
type: Image To Image
frequency: 2
level: weak
coverage: 0.732
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, DisableNoise, DualCLIPLoader, FaceAnalysisModels, FaceSegmentation, FluxForwardODESampler, FluxReverseODESampler, GrowMaskWithBlur, ImageCompositeMasked, ImpactMakeImageBatch, InFluxModelSamplingPred, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoader, MaskComposite, OutFluxModelSamplingPred, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReActorBuildFaceModel, ReActorFaceSwap, SamplerCustomAdvanced, SaveImage, Seed Everywhere, SetLatentNoiseMask, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/单人照-影楼爆款写真同款【脸部模型注入+逆采样+细节重绘】_1892214312688328705.json, 图片生成/图生图/最强 Flux 图片换脸 ｜参考图换脸 + 高清超分辨率_1910707665335713794.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_157

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/单人照-影楼爆款写真同款【脸部模型注入+逆采样+细节重绘】_1892214312688328705.json、图片生成/图生图/最强 Flux 图片换脸 ｜参考图换脸 + 高清超分辨率_1910707665335713794.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `DisableNoise`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceSegmentation`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImpactMakeImageBatch`
- `InFluxModelSamplingPred`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoader`
- `MaskComposite`
- `OutFluxModelSamplingPred`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReActorBuildFaceModel`
- `ReActorFaceSwap`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Apply Instagram Filter` —— 1/2 个有
- `CLIPTextEncodeFlux` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Convert Masks to Images` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FilmGrain` —— 1/2 个有
- `FlipSigmas` —— 1/2 个有
- `FlipSigmasAdjusted` —— 1/2 个有
- `FluxDeGuidance` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.25 | - | 2 | 80% |
| 宽度 | 832x1216 (0.68) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
