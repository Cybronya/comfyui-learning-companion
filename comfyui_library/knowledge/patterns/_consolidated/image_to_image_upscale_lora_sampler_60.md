---
name: image_to_image_upscale_lora_sampler_60
type: Image To Image
frequency: 3
level: strong
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LazySwitch1way, LoadImage, LoraLoader, LoraLoaderModelOnly, Miaoshouai_Tagger, ModelSamplingAuraFlow, PreviewImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json, 图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395218244202497.json, 平台全量/Z-Image+Qwen3.5-完美洗图-4K放大_2067092866232569857.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json、图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395218244202497.json、平台全量/Z-Image+Qwen3.5-完美洗图-4K放大_2067092866232569857.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LazySwitch1way`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Miaoshouai_Tagger`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.75 | 0.75 - 0.75 | 3 | 100% |
| LoRA 模型强度 | 0.85 | 0.85 - 0.85 | 3 | 100% |
| LoRA 文本强度 | 0.85 | 0.85 - 0.85 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，观测区间 0.85 - 0.85，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，观测区间 0.85 - 0.85，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
