---
name: image_to_image_upscale_lora_sampler_30
type: Image To Image
frequency: 5
level: moderate
coverage: 0.7964
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX Krea TTP 高清放大_1951208128249536513.json, 图片生成/图生图/FLUX TTP® 商用级放大工作流_1926509095090819073.json, 图片生成/图生图/FLUXTTP放大工作流_1935592665171808257.json, 图片生成/图生图/FLUX建筑洗图  5k_1981008797827219458.json, 图片生成/图生图/TTP分块高清修复_2044978017885229058.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX Krea TTP 高清放大_1951208128249536513.json、图片生成/图生图/FLUX TTP® 商用级放大工作流_1926509095090819073.json、图片生成/图生图/FLUXTTP放大工作流_1935592665171808257.json、图片生成/图生图/FLUX建筑洗图  5k_1981008797827219458.json、图片生成/图生图/TTP分块高清修复_2044978017885229058.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `easy imageSize` —— 4/5 个有
- `LayerMask: LoadFlorence2Model` —— 3/5 个有
- `LayerUtility: Florence2Image2Prompt` —— 3/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `CR Latent Batch Size` —— 1/5 个有
- `CropMask` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `LayerUtility: CropBoxResolve` —— 1/5 个有
- `LayerUtility: CropByMask V2` —— 1/5 个有
- `LayerUtility: RestoreCropBox` —— 1/5 个有
- `Load Image Batch` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 5 | 82% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 0.32 | 0.2 - 0.42 | 5 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 0.32，观测区间 0.2 - 0.42，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
