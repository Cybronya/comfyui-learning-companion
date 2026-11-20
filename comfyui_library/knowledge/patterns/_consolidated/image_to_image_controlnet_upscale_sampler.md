---
name: image_to_image_controlnet_upscale_sampler
type: Image To Image
frequency: 9
level: moderate
coverage: 0.849222
common_nodes: [ApplyInstantID, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, FaceAnalysisModels, FaceBoundingBox, GetImageSize+, Image Comparer (rgthree), ImageComposite+, ImageConcanate, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LoadImage, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI摄影，生成专属自己的海报_1953124001817292802.json, 图片生成/图生图/DreamFit Flux高质量性感换装工作流V3（人脸一致性版）_1923641767445319681.json, 图片生成/图生图/DreamFit Flux高质量性感换装工作流V3（姿势，人脸版）_1923650301994127361.json, 图片生成/图生图/DreamFit Flux高质量换装生成V1（上下装鞋子，人脸，姿势）_1923689036513202178.json, 图片生成/图生图/DreamFit Flux高质量换装生成V1（上下装，人脸，姿势）_1923677323194003457.json, 图片生成/图生图/DreamO 双图融合人物一致性加强版V2（不炸显存）_1925924770247053313.json, 图片生成/图生图/DreanFit性感百变双主体上下装优化版工作流（人脸一致性）_1921065415924187137.json, 图片生成/图生图/Ominigen2单主体动作编辑ID加强+高清化V1_1936624718294454274.json, 图片生成/文生图/DreamO IP控制文生图人物一致性进阶版V2（不炸显存）_1925972588705845250.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AI摄影，生成专属自己的海报_1953124001817292802.json、图片生成/图生图/DreamFit Flux高质量性感换装工作流V3（人脸一致性版）_1923641767445319681.json、图片生成/图生图/DreamFit Flux高质量性感换装工作流V3（姿势，人脸版）_1923650301994127361.json、图片生成/图生图/DreamFit Flux高质量换装生成V1（上下装鞋子，人脸，姿势）_1923689036513202178.json、图片生成/图生图/DreamFit Flux高质量换装生成V1（上下装，人脸，姿势）_1923677323194003457.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ImageConcanate`
- `ImageScale`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
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
- `PMRF` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `Note Plus (mtb)` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `PDIMAGE_LongerSize` —— 4/9 个有
- `RunningHub_DreamFit_Flux` —— 4/9 个有
- `JWInteger` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `RunningHub DreamO` —— 2/9 个有
- `CLIPLoader` —— 1/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `ImageMaskSwitch` —— 1/9 个有
- `LayerMask: BiRefNetUltraV2` —— 1/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `LoadOmniGen2Model` —— 1/9 个有
- `ModelSamplingAuraFlow` —— 1/9 个有
- `OmniGen2` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `RunningHub_DreamFit_SD` —— 1/9 个有
- `SeedVR2` —— 1/9 个有
- `SeedVR2BlockSwap` —— 1/9 个有
- `TTP_Expand_And_Mask` —— 1/9 个有
- `TextConcatenator` —— 1/9 个有
- `UNETLoader` —— 1/9 个有
- `VAELoader` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 9 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 9 | 39% |
| 采样算法 | euler_ancestral | - | 9 | 89% |
| 调度器 | sgm_uniform | - | 9 | 89% |
| 重绘幅度 | 0.5 | 0.5 - 1 | 9 | 72% |
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 89%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 89%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 1，9 个样本
- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
