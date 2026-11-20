---
name: unknown_workflow_upscale_lora_sampler_31
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.608286
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/一键反推提示词——TTP高清放大工作流_1856530108285915137.json, 图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json, 图片生成/图生图/FluxGirl产品图衣服_2012758919466196993.json, 图片生成/文生图/FLUX无损高清放大修复    波浪Ai_1894631241784930305.json, 平台全量/Flux Your OOTD_1851879698333937666.json, 平台全量/Flux 双人成行_1848917334319677441.json, 平台全量/Flux 好事成双_1851642250714562562.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/一键反推提示词——TTP高清放大工作流_1856530108285915137.json、图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json、图片生成/图生图/FluxGirl产品图衣服_2012758919466196993.json、图片生成/文生图/FLUX无损高清放大修复    波浪Ai_1894631241784930305.json、平台全量/Flux Your OOTD_1851879698333937666.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 6/7 个有
- `CLIPTextEncode` —— 6/7 个有
- `DepthAnythingPreprocessor` —— 6/7 个有
- `LayerFilter: FilmV2` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `DisableNoise` —— 4/7 个有
- `EmptyLatentImage` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ImpactImageBatchToImageList` —— 4/7 个有
- `Int` —— 4/7 个有
- `ModelSamplingFlux` —— 4/7 个有
- `SplitSigmasDenoise` —— 4/7 个有
- `VAEDecode` —— 4/7 个有
- `CR Text Replace` —— 3/7 个有
- `DeepTranslatorTextNode` —— 3/7 个有
- `Multi Text Merge` —— 3/7 个有
- `PortraitMaster` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `TextInput_` —— 3/7 个有
- `easy imageBatchToImageList` —— 3/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `ControlNetApplySD3` —— 2/7 个有
- `ControlNetLoader` —— 2/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `ImpactSwitch` —— 2/7 个有
- `OpenposePreprocessor` —— 2/7 个有
- `SetUnionControlNetType` —— 2/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `DownloadAndLoadFlorence2Model` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `JWImageResizeByLongerSide` —— 1/7 个有
- `LayerUtility: ImageBlendAdvance` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `SDXLRecommendedImageSize` —— 1/7 个有
- `SaveImageAndMetadata_` —— 1/7 个有
- `Seed Everywhere` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy imageSize` —— 1/7 个有
- `workflow/展示文本` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 936 | 4 | 70% |
| 高度 | 512 | 512 - 1248 | 4 | 54% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 936，4 个样本
- 高度 中位数 512，观测区间 512 - 1248，4 个样本
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
