---
name: image_to_image_controlnet_inpaint_upscale_4
type: Image To Image
frequency: 2
level: weak
coverage: 0.84
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, Image Comparer (rgthree), ImageListSelect(FaceParsing), ImageScaleBy, ImageToMask, ImpactMakeAnyList, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlend, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageRemoveAlpha, LoadImage, MaskListSelect(FaceParsing), MaskPreview, MaskToImage, PreviewImage, RandomNoise, ReActorFaceSwap, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetLatentNoiseMask, SmartColorMatch, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2-klein-for循环-婚纱摄影-双人及单人换脸_2099052699428933633.json, 图片生成/图生图/flux2-klein-for循环-婚纱摄影-双人及单人换脸_2099425205931302914.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux2-klein-for循环-婚纱摄影-双人及单人换脸_2099052699428933633.json、图片生成/图生图/flux2-klein-for循环-婚纱摄影-双人及单人换脸_2099425205931302914.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `Image Comparer (rgthree)`
- `ImageListSelect(FaceParsing)`
- `ImageScaleBy`
- `ImageToMask`
- `ImpactMakeAnyList`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `MaskListSelect(FaceParsing)`
- `MaskPreview`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `ReActorFaceSwap`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetLatentNoiseMask`
- `SmartColorMatch`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
