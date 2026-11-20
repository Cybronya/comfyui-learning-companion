---
name: image_to_image_controlnet_upscale_lora_8
type: Image To Image
frequency: 4
level: weak
coverage: 0.89875
common_nodes: [AIO_Preprocessor, ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, CR Prompt Text, ColorMatch, ConditioningAverage, Constant Number, ControlNetLoader, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageResizeKJ, ImageSharpen, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, Text Concatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/建筑效果工作流_1930582206639427586.json, 平台全量/建筑SU截图导出效果图工作流_1963774615023751169.json, 平台全量/建筑建模图生成渲染图+模型体块生成同款效果图渲染图示意图 建筑效果图一键生成_1991685700133273601.json, 平台全量/建筑效果图工作流（学习版）_1962066835707465730.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/建筑效果工作流_1930582206639427586.json、平台全量/建筑SU截图导出效果图工作流_1963774615023751169.json、平台全量/建筑建模图生成渲染图+模型体块生成同款效果图渲染图示意图 建筑效果图一键生成_1991685700133273601.json、平台全量/建筑效果图工作流（学习版）_1962066835707465730.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ColorMatch`
- `ConditioningAverage`
- `Constant Number`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `Text Concatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `FluxUnionControlNetApply` —— 3/4 个有
- `Image Compare (mtb)` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `Int` —— 3/4 个有
- `ModelSamplingFlux` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `ReduxAdvanced` —— 3/4 个有
- `SetUnionControlNetType` —— 3/4 个有
- `StyleModelLoader` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `IPAdapterUnifiedLoader` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `PrepImageForClipVision` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `easy ipadapterApplyADV` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 30 | 4 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 4 | 0% |
| 采样算法 | uni_pc | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 0.18 | 0.18 - 0.8 | 4 | 20% |
| ControlNet 权重 | depth | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 30，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 0.18，观测区间 0.18 - 0.8，4 个样本，取值分散，一致性仅 20%
- ControlNet 权重 最常用 depth，4 个样本，一致性 75%
