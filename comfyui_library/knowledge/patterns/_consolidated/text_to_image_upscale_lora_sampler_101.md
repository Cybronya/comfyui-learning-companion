---
name: text_to_image_upscale_lora_sampler_101
type: Text To Image
frequency: 3
level: strong
coverage: 0.969
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/图生图控制_1903454090603433985.json, 平台全量/室内白模高清渲染_1897303296510775297.json, 平台全量/室内风格融合_1902007794751709186.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生图控制_1903454090603433985.json、平台全量/室内白模高清渲染_1897303296510775297.json、平台全量/室内风格融合_1902007794751709186.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ArgosTranslateTextNode` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `FaceDetailer` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `SetShakkerLabsUnionControlNetType` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 21 - 25 | 3 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1224 | 1024 - 1280 | 3 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 21 - 25，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1224，观测区间 1024 - 1280，3 个样本，取值集中（一致性 91%）
