---
name: text_to_image_controlnet_ipadapter_upscale_2
type: Text To Image
frequency: 4
level: moderate
coverage: 0.75825
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ClipInterrogator, ConditioningAverage, Constant Number, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, GetNode, IPAdapter, IPAdapterUnifiedLoader, Image Comparer (rgthree), Image Filter Adjustments, Image Tiled, ImageConcanateOfUtils, ImageFromBatch, ImageScaleBy, ImageUpscaleWithModel, ImitationHueNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SetNode, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, Text Concatenate, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageInsetCrop, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/线稿转效果图+高清放大_2078482185241321474.json, 图片生成/图生图/风格参考生图4K_1997560760425463810.json, 平台全量/响响-AI建筑设计-风格参考生图_1997569224740651010.json, 平台全量/建筑效果图+TTP放大（两分钟4K，超好用）_1981651992525324289.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/线稿转效果图+高清放大_2078482185241321474.json、图片生成/图生图/风格参考生图4K_1997560760425463810.json、平台全量/响响-AI建筑设计-风格参考生图_1997569224740651010.json、平台全量/建筑效果图+TTP放大（两分钟4K，超好用）_1981651992525324289.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
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
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.9 | 4 | 95% |
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 4 | 36% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.9，4 个样本，取值集中（一致性 95%）
- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，4 个样本，取值分散，一致性仅 36%
