---
name: image_to_image_controlnet_inpaint_upscale_2
type: Image To Image
frequency: 6
level: strong
coverage: 0.889
common_nodes: [Any Switch (rgthree), ApplyInstantID, BboxDetectorSEGS, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, Fast Groups Bypasser (rgthree), GrowMask, Image Comparer (rgthree), ImageComposite+, ImageCrop+, ImageListToImageBatch, ImageResize+, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerUtility: SaveImagePlus, LoadImage, LoadImageListFromDir //Inspire, Mask Crop Region, MaskBlur+, MaskToImage, ModelSamplingSD3, PlaySound|pysssss, PreviewImage, RHHiddenNodes, SAMDetectorCombined, SAMLoader, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/去AI感电商洗图 变换人脸超高清_2019298778804654081.json, 图片生成/图生图/去AI感电商洗图 变换人脸超高清_2048641173635469314.json, 图片生成/图生图/去AI感电商洗图 变换人脸超高清_2056577967152779265.json, 图片生成/图生图/去AI感电商洗图 变换人脸超高清_2056633651881930753.json, 图片生成/图生图/去AI感电商洗图 变换人脸超高清_2059186838157488130.json, 图片生成/图生图/去AI感电商洗图 变换人脸超高清_2062823689917390850.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/去AI感电商洗图 变换人脸超高清_2019298778804654081.json、图片生成/图生图/去AI感电商洗图 变换人脸超高清_2048641173635469314.json、图片生成/图生图/去AI感电商洗图 变换人脸超高清_2056577967152779265.json、图片生成/图生图/去AI感电商洗图 变换人脸超高清_2056633651881930753.json、图片生成/图生图/去AI感电商洗图 变换人脸超高清_2059186838157488130.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyInstantID`
- `BboxDetectorSEGS`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageCrop+`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerUtility: SaveImagePlus`
- `LoadImage`
- `LoadImageListFromDir //Inspire`
- `Mask Crop Region`
- `MaskBlur+`
- `MaskToImage`
- `ModelSamplingSD3`
- `PlaySound|pysssss`
- `PreviewImage`
- `RHHiddenNodes`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler_ancestral | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，6 个样本，取值集中（一致性 100%）
