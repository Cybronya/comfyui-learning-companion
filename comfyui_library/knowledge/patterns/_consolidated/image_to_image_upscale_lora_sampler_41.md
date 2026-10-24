---
name: image_to_image_upscale_lora_sampler_41
type: Image To Image
frequency: 4
level: weak
coverage: 0.954
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Evaluate Strings, FluxGuidance, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Translator, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext +pulid  万物迁移-场景+动作_1941382304831062018.json, 图片生成/图生图/Kontext 万物迁移-固定场景换人物_1941364298730127361.json, 图片生成/图生图/只需一步天天过女神节一键转花仙子（rick随风），人间美女天上仙子不是梦！_2014600380822327298.json, 图片生成/图生图/女神节一键转花仙子（rick随风）_1897193087721263106.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext +pulid  万物迁移-场景+动作_1941382304831062018.json、图片生成/图生图/Kontext 万物迁移-固定场景换人物_1941364298730127361.json、图片生成/图生图/只需一步天天过女神节一键转花仙子（rick随风），人间美女天上仙子不是梦！_2014600380822327298.json、图片生成/图生图/女神节一键转花仙子（rick随风）_1897193087721263106.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Evaluate Strings`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BaiduTranslateNode` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `DepthAnything_V2` —— 2/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `InstructPixToPixConditioning` —— 2/4 个有
- `LayerMask: BiRefNetUltraV2` —— 2/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/4 个有
- `LayerUtility: ImageBlendAdvance` —— 2/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | 6 - 30 | 4 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 0.59 | 0.18 - 1 | 4 | 31% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，观测区间 6 - 30，4 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 0.59，观测区间 0.18 - 1，4 个样本，取值分散，一致性仅 31%
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
