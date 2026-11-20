---
name: image_to_image_controlnet_upscale_sampler_3
type: Image To Image
frequency: 8
level: strong
coverage: 0.919125
common_nodes: [ApplyInstantID, CLIPTextEncode, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, GetImageSize+, ImageComposite+, ImageScale, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LoadImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Instant ID换脸_1911048136863772673.json, 平台全量/内部测试专用002（HL）_2015411066922082305.json, 平台全量/完美换脸_1907426181048594433.json, 平台全量/换脸-MINTS_1932017581572423681.json, 平台全量/旅拍换脸工作流_1956547035984003074.json, 平台全量/超强换脸_多角度参考_无惧遮挡_1915677638843629569.json, 平台全量/（自用）InstantID常用换脸工作流_1958196819966758913.json, 数字人/数字人/换脸-MINTS_1944988752395816961.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Instant ID换脸_1911048136863772673.json、平台全量/内部测试专用002（HL）_2015411066922082305.json、平台全量/完美换脸_1907426181048594433.json、平台全量/换脸-MINTS_1932017581572423681.json、平台全量/旅拍换脸工作流_1956547035984003074.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GetImageSize+`
- `ImageComposite+`
- `ImageScale`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
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
- `CM_IntToFloat` —— 7/8 个有
- `CM_IntToNumber` —— 7/8 个有
- `CM_NumberToInt` —— 7/8 个有
- `CM_NumberUnaryOperation` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `ImageScaleBy` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `LayerMask: PersonMaskUltra V2` —— 6/8 个有
- `MaskPreview+` —— 6/8 个有
- `FaceAnalysisModels` —— 5/8 个有
- `FaceBoundingBox` —— 5/8 个有
- `Image Batch` —— 4/8 个有
- `JWImageResizeByLongerSide` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `ConstrainImage|pysssss` —— 3/8 个有
- `JWInteger` —— 3/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `ApplyFBCacheOnModel` —— 1/8 个有
- `LatentLoaderAdvanced` —— 1/8 个有
- `PDIMAGE_LongerSize` —— 1/8 个有
- `SAM3Segment` —— 1/8 个有
- `SaveLatent` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SeedVR2BlockSwap` —— 1/8 个有
- `VAELoader` —— 1/8 个有
- `easy imageScaleDownBy` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 8 | 100% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 100% |
| 调度器 | sgm_uniform | - | 8 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.6 | 8 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.6，8 个样本，取值集中（一致性 94%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
