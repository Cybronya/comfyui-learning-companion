---
name: image_to_image_ipadapter_upscale_sampler
type: Image To Image
frequency: 3
level: strong
coverage: 0.733333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ConditioningCombine, ConstrainImage|pysssss, DepthAnythingV2Preprocessor, DetailTransfer, DualCLIPLoader, GetImageSize+, ICLightConditioning, IPAdapter, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageInvert, ImageResizeKJ, ImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerColor: Brightness & Contrast, LayerColor: Color of Shadow & Highlight, LayerColor: RGB, LayerFilter: GaussianBlur, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadAndApplyICLightUnet, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy clearCacheAll, easy imageDetailTransfer]
problems: []
missing: []
members: [平台全量/产品 修复 精修 放大_1890060851376795649.json, 平台全量/空白工作流_1980126015030726657.json, 平台全量/自动抠图精修_1932999622610616321.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/产品 修复 精修 放大_1890060851376795649.json、平台全量/空白工作流_1980126015030726657.json、平台全量/自动抠图精修_1932999622610616321.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningCombine`
- `ConstrainImage|pysssss`
- `DepthAnythingV2Preprocessor`
- `DetailTransfer`
- `DualCLIPLoader`
- `GetImageSize+`
- `ICLightConditioning`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageInvert`
- `ImageResizeKJ`
- `ImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: RGB`
- `LayerFilter: GaussianBlur`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`
- `easy imageDetailTransfer`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `InspyrenetRembg` —— 2/3 个有
- `Joy_caption_two_advanced` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `Joy_extra_options` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `SUPIR_conditioner` —— 2/3 个有
- `SUPIR_decode` —— 2/3 个有
- `SUPIR_encode` —— 2/3 个有
- `SUPIR_first_stage` —— 2/3 个有
- `SUPIR_model_loader_v2` —— 2/3 个有
- `SUPIR_sample` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `ImageListToImageBatch` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModel` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: ColorImage V2` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `TTP_Image_Assy` —— 1/3 个有
- `TTP_Image_Tile_Batch` —— 1/3 个有
- `TTP_Tile_image_size` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.3 - 0.4 | 3 | 87% |
| LoRA 模型强度 | 0.85 | - | 2 | 82% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 0.4，3 个样本，取值集中（一致性 87%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
