---
name: image_to_image_controlnet_inpaint_upscale
type: Image To Image
frequency: 11
level: strong
coverage: 0.921273
common_nodes: [ApplyFBCacheOnModel, ApplyInstantID, ApplyPulidFlux, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorAdjust(FaceParsing), ControlNetLoader, CropFaces, DetectFaces, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), Image Lucy Sharpen, ImageFromBatch, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReActorFaceSwap, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WarpFacesBack, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/1_1超高相似度任务换脸_2001542518049239041.json, 图片生成/图生图/全自动人像换脸+高清修复_1984963717710364673.json, 图片生成/图生图/换脸人像（多角度）_1967585552226754561.json, 图片生成/图生图/换脸人像（多角度）_1975067630673506306.json, 图片生成/图生图/换脸人像（超高相似度）_1959206954939920385.json, 图片生成/图生图/换脸人像（超高相似度）_1962156544936841217.json, 图片生成/图生图/换脸人像（超高相似度）_2001947777271754754.json, 图片生成/图生图/换脸人像（超高相似度）_2008171861728825346.json, 图片生成/图生图/换脸人像（超高相似度）_2014148376803155970.json, 图片生成/图生图/换脸技术新版_1962501496229244930.json, 图片生成/图生图/西洲 换脸人像（超高相似度）_1975061060241764354.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/1_1超高相似度任务换脸_2001542518049239041.json、图片生成/图生图/全自动人像换脸+高清修复_1984963717710364673.json、图片生成/图生图/换脸人像（多角度）_1967585552226754561.json、图片生成/图生图/换脸人像（多角度）_1975067630673506306.json、图片生成/图生图/换脸人像（超高相似度）_1959206954939920385.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `ApplyInstantID`
- `ApplyPulidFlux`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorAdjust(FaceParsing)`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Image Lucy Sharpen`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReActorFaceSwap`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WarpFacesBack`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `GrowMask` —— 1/11 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/11 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/11 个有
- `SeCModelLoader` —— 1/11 个有
- `SeCVideoSegmentation` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 0.02 | 0.02 - 0.03 | 11 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 0.02，观测区间 0.02 - 0.03，11 个样本，取值集中（一致性 86%）
- 风险：重绘幅度 观测到 0.02，低于常用下限 0.1（）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
