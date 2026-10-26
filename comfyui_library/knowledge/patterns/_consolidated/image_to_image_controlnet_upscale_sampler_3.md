---
name: image_to_image_controlnet_upscale_sampler_3
type: Image To Image
frequency: 5
level: weak
coverage: 0.8838
common_nodes: [ApplyInstantID, CLIPTextEncode, CR Upscale Image, CheckpointLoaderSimple, ControlNetLoader, FaceAnalysisModels, FaceBoundingBox, Image Comparer (rgthree), ImageComposite+, ImageScale, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LoadImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/InstantID换脸-背景人物不变_1952280658276241410.json, 图片生成/图生图/Step1X-Edit强一致性图像编辑（单人真人版）_1916692094662934529.json, 图片生成/图生图/最强InstnatlD图像换脸+SeedVR高清修复放大_1951501727793139714.json, 图片生成/图生图/照片时光机（输入时间、地点和照片体验）_1982995802052276225.json, 数字人/数字人/换脸-MINTS_1944988752395816961.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/InstantID换脸-背景人物不变_1952280658276241410.json、图片生成/图生图/Step1X-Edit强一致性图像编辑（单人真人版）_1916692094662934529.json、图片生成/图生图/最强InstnatlD图像换脸+SeedVR高清修复放大_1951501727793139714.json、图片生成/图生图/照片时光机（输入时间、地点和照片体验）_1982995802052276225.json、数字人/数字人/换脸-MINTS_1944988752395816961.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Image Comparer (rgthree)`
- `ImageComposite+`
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
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 4/5 个有
- `CM_IntToNumber` —— 4/5 个有
- `CM_NumberToInt` —— 4/5 个有
- `CM_NumberUnaryOperation` —— 4/5 个有
- `ControlNetApplyAdvanced` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `MaskPreview+` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `AV_LoraLoader` —— 1/5 个有
- `ApplyFBCacheOnModel` —— 1/5 个有
- `CLIPLoader` —— 1/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `ControlNetApplySD3` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `JWFloat` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RunningHub_Step1XEdit` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有
- `TextBox` —— 1/5 个有
- `TextCombinerSix` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `VAELoader` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | 0.1 - 0.35 | 5 | 33% |
| 采样步数 | 8 | 6 - 10 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 43% |
| 采样算法 | euler_ancestral | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 0.5 | 0.5 - 1 | 5 | 69% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.35，5 个样本，取值分散，一致性仅 33%
- 采样步数 中位数 8，观测区间 6 - 10，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
