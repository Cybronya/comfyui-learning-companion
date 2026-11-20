---
name: image_to_image_controlnet_inpaint_upscale
type: Image To Image
frequency: 14
level: moderate
coverage: 0.926
common_nodes: [ApplyFBCacheOnModel, ApplyInstantID, ApplyPulidFlux, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorAdjust(FaceParsing), ControlNetLoader, CropFaces, DetectFaces, DualCLIPLoader, FluxGuidance, Image Lucy Sharpen, ImageFromBatch, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReActorFaceSwap, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WarpFacesBack, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/1_1超高相似度任务换脸_2001542518049239041.json, 图片生成/图生图/全自动人像换脸+高清修复_1984963717710364673.json, 图片生成/图生图/换脸人像（多角度）_1967585552226754561.json, 图片生成/图生图/换脸人像（多角度）_1975067630673506306.json, 图片生成/图生图/换脸人像（超高相似度）_1959206954939920385.json, 图片生成/图生图/换脸人像（超高相似度）_1962156544936841217.json, 图片生成/图生图/换脸人像（超高相似度）_2001947777271754754.json, 图片生成/图生图/换脸人像（超高相似度）_2008171861728825346.json, 图片生成/图生图/换脸人像（超高相似度）_2014148376803155970.json, 图片生成/图生图/换脸技术新版_1962501496229244930.json, 图片生成/图生图/西洲 换脸人像（超高相似度）_1975061060241764354.json, 平台全量/【高精度换脸】换脸人像 傻瓜式 人像换脸多角度（超高相似度）_1989204528832589825.json, 平台全量/图片换脸_1981635172095410177.json, 平台全量/换脸人像（超高相似度）_2020491948565471233.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/1_1超高相似度任务换脸_2001542518049239041.json、图片生成/图生图/全自动人像换脸+高清修复_1984963717710364673.json、图片生成/图生图/换脸人像（多角度）_1967585552226754561.json、图片生成/图生图/换脸人像（多角度）_1975067630673506306.json、图片生成/图生图/换脸人像（超高相似度）_1959206954939920385.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 13/14 个有
- `LayerMask: PersonMaskUltra V2` —— 13/14 个有
- `LayerUtility: CropByMask` —— 13/14 个有
- `BlockifyMask` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `GrowMask` —— 1/14 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/14 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/14 个有
- `SeCModelLoader` —— 1/14 个有
- `SeCVideoSegmentation` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 14 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 0.02 | 0.02 - 0.6 | 14 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，14 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 0.02，观测区间 0.02 - 0.6，14 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 0.02，低于常用下限 0.1（）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
