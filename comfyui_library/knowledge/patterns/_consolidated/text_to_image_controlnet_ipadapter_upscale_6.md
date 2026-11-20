---
name: text_to_image_controlnet_ipadapter_upscale_6
type: Text To Image
frequency: 2
level: weak
coverage: 0.896
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, Florence2Run, FluxGuidance, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageResizeKJ, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/室内线稿转效果图（重绘+高清）_2038525529124507649.json, 平台全量/建筑效果图工作流_1916500738728460290.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/室内线稿转效果图（重绘+高清）_2038525529124507649.json、平台全量/建筑效果图工作流_1916500738728460290.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2Run`
- `FluxGuidance`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ConditioningAverage` —— 1/2 个有
- `Constant Number` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `ImageGenResolutionFromImage` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `LayerUtility: GetImageSize` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `TTP_CoordinateSplitter` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_condsetarea_merge` —— 1/2 个有
- `TTP_condtobatch` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageInsetCrop` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.77 | - | 2 | 65% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 77% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.77，样本不足，未给区间，2 个样本
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
