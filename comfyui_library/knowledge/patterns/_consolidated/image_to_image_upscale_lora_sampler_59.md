---
name: image_to_image_upscale_lora_sampler_59
type: Image To Image
frequency: 3
level: strong
coverage: 0.705667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, ETN_Translate, FluxGuidance, GetNode, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/【网红洗图】Flux智能反推提示词 一键批量生图_1911677261945470977.json, 图片生成/文生图/8K放大】FLUX去除AI感，图片细化+手部修复_1902541158919122945.json, 图片生成/文生图/FLUX+JOY2反推-图生图+TTP图像放大_1909860762637271042.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【网红洗图】Flux智能反推提示词 一键批量生图_1911677261945470977.json、图片生成/文生图/8K放大】FLUX去除AI感，图片细化+手部修复_1902541158919122945.json、图片生成/文生图/FLUX+JOY2反推-图生图+TTP图像放大_1909860762637271042.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ETN_Translate`
- `FluxGuidance`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
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
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `StyleModelApply` —— 2/3 个有
- `StyleModelLoader` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 0.7 | 0.5 - 1 | 3 | 72% |
| LoRA 模型强度 | 0.8 | 0.75 - 0.8 | 3 | 97% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.7，观测区间 0.5 - 1，3 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.75 - 0.8，3 个样本，取值集中（一致性 97%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
