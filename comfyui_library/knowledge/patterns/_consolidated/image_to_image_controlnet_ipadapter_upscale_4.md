---
name: image_to_image_controlnet_ipadapter_upscale_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.866667
common_nodes: [ApplyInstantIDAdvanced, ApplyPulid, BNK_CLIPTextEncodeAdvanced, BasicGuider, BasicScheduler, BboxDetectorSEGS, Bounded Image Blend, Bounded Image Crop with Mask, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ClipInterrogator, ColorMatch, ControlNetApply, ControlNetLoader, DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, FaceAnalysisModels, FaceEmbedDistance, FaceShaper, FaceShaperModels, IPAdapterAdvanced, IPAdapterModelLoader, Image Comparer (rgthree), ImageRandomTransform+, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, ImpactMakeImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWMaskResize, KSampler, KSamplerSelect, LayerMask: MaskEdgeUltraDetail V2, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, MaskToImage, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, RandomNoise, RemapMaskRange, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize, easy int, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/单人复刻写真工作流_1949678543434338305.json, 平台全量/双人写真工作流_1949707143273435137.json, 平台全量/证件照V3_1949719559948390401.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/单人复刻写真工作流_1949678543434338305.json、平台全量/双人写真工作流_1949707143273435137.json、平台全量/证件照V3_1949719559948390401.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyInstantIDAdvanced`
- `ApplyPulid`
- `BNK_CLIPTextEncodeAdvanced`
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `Bounded Image Blend`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ClipInterrogator`
- `ColorMatch`
- `ControlNetApply`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `FaceShaper`
- `FaceShaperModels`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Comparer (rgthree)`
- `ImageRandomTransform+`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactMakeImageBatch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskEdgeUltraDetail V2`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RandomNoise`
- `RemapMaskRange`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AddBackgroundNode` —— 1/3 个有
- `BiRefNet_Hugo` —— 1/3 个有
- `CR Image Input Switch` —— 1/3 个有
- `HivisionLayOutNode` —— 1/3 个有
- `HivisionNode` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImpactSEGSToMaskBatch` —— 1/3 个有
- `ImpactSimpleDetectorSEGS` —— 1/3 个有
- `LaterProcessNode` —— 1/3 个有
- `MaskFromBatch+` —— 1/3 个有
- `SEGSPreview` —— 1/3 个有
- `ZHHivisionParamsNode` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageCount` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 1 | 3 | 90% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 0.45 - 1 | 3 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，3 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
