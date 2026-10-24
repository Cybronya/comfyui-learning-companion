---
name: image_to_image_controlnet_upscale_sampler_2
type: Image To Image
frequency: 6
level: strong
coverage: 0.8645
common_nodes: [ApplyInstantID, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, FaceAnalysisModels, FaceBoundingBox, GetImageSize+, Image Comparer (rgthree), ImageComposite+, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LoadImage, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json, 图片生成/图生图/InstantCharacter超强ID一致性强化版V1（真人版）_1914277592759791618.json, 图片生成/图生图/InstantCharacter超强ID一致性强化版V1（真人版）_1914483676770463746.json, 图片生成/图生图/InstantID常用换脸工作流_1940979002498826241.json, 图片生成/图生图/【极速版】DreamO双重一致性真人版图像编辑_1930881751181099009.json, 图片生成/图生图/四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json、图片生成/图生图/InstantCharacter超强ID一致性强化版V1（真人版）_1914277592759791618.json、图片生成/图生图/InstantCharacter超强ID一致性强化版V1（真人版）_1914483676770463746.json、图片生成/图生图/InstantID常用换脸工作流_1940979002498826241.json、图片生成/图生图/【极速版】DreamO双重一致性真人版图像编辑_1930881751181099009.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageScale`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: LayerImageTransform`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `JWImageResizeByLongerSide` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `ImageConcanate` —— 4/6 个有
- `PMRF` —— 4/6 个有
- `ApplyFBCacheOnModel` —— 3/6 个有
- `DualCLIPLoader` —— 3/6 个有
- `FluxGuidance` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PDIMAGE_LongerSize` —— 3/6 个有
- `VAELoader` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `ConstrainImage|pysssss` —— 2/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `GoogleTranslateTextNode` —— 2/6 个有
- `ImageStitch` —— 2/6 个有
- `InstantCharacterGenerate` —— 2/6 个有
- `InstantCharacterLoadModel` —— 2/6 个有
- `LoadImageOutput` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `ApplyDreamO` —— 1/6 个有
- `CLIPLoader` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `DreamOProcessorLoader` —— 1/6 个有
- `DreamORefEncode` —— 1/6 个有
- `FastCanvas` —— 1/6 个有
- `FastCanvasTool` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `ImageCropper` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MagCache` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `NunchakuFluxLoraLoader` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `RepeatImageBatch` —— 1/6 个有
- `TTP_Expand_And_Mask` —— 1/6 个有
- `TeaCache` —— 1/6 个有
- `TrimVideoLatent` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `WanVaceToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 6 | 100% |
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
