---
name: text_to_image_controlnet_upscale_sampler
type: Text To Image
frequency: 2
level: weak
coverage: 0.6475
common_nodes: [ApplyInstantID, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Prompt Text, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, GetImageSize+, Image Comparer (rgthree), ImageComposite+, ImageConcanate, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWInteger, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM V2, LoadImage, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: [ImageComposite+, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM V2, Note Plus (mtb), easy imageColorMatch, CR Prompt Text, CR Upscale Image, GetImageSize+, MaskPreview+]
members: [图片生成/文生图/1915996781723713538.json, 图片生成/文生图/1925982816373264386.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1915996781723713538.json、图片生成/文生图/1925982816373264386.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Prompt Text`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageConcanate`
- `ImageScale`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: LayerImageTransform`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `BNK_CLIPTextEncodeAdvanced` —— 1/2 个有
- `CLIPSetLastLayer` —— 1/2 个有
- `EasyFunction_Lite` —— 1/2 个有
- `HyperLoRAApplyLoRA` —— 1/2 个有
- `HyperLoRAConfig` —— 1/2 个有
- `HyperLoRAFaceAttr` —— 1/2 个有
- `HyperLoRAGenerateIDLoRA` —— 1/2 个有
- `HyperLoRAIDCond` —— 1/2 个有
- `HyperLoRALoader` —— 1/2 个有
- `ImpactMakeImageBatch` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `PMRF` —— 1/2 个有
- `StoryDiffusion_Apply` —— 1/2 个有
- `StoryDiffusion_CLIPTextEncode` —— 1/2 个有
- `StoryDiffusion_KSampler` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ImageComposite+、LayerMask: MaskGrow、LayerMask: PersonMaskUltra V2、LayerUtility: CropBoxResolve、LayerUtility: CropByMask
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
