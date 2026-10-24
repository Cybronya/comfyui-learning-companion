---
name: text_to_image_controlnet_ipadapter_upscale_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.7575
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ClipInterrogator, ConditioningAverage, Constant Number, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, GetNode, IPAdapter, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Filter Adjustments, Image Tiled, ImageConcanateOfUtils, ImageFromBatch, ImageScaleBy, ImageUpscaleWithModel, ImitationHueNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SetNode, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, Text Concatenate, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageInsetCrop, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/线稿转效果图+高清放大_2078482185241321474.json, 图片生成/图生图/风格参考生图4K_1997560760425463810.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/线稿转效果图+高清放大_2078482185241321474.json、图片生成/图生图/风格参考生图4K_1997560760425463810.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ClipInterrogator`
- `ConditioningAverage`
- `Constant Number`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImitationHueNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `Text Concatenate`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageInsetCrop`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.8 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
