---
name: image_to_image_upscale_lora_sampler_72
type: Image To Image
frequency: 2
level: weak
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LazySwitch1way, LoadImage, LoraLoader, LoraLoaderModelOnly, Miaoshouai_Tagger, ModelSamplingAuraFlow, PreviewImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json, 图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395218244202497.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json、图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395218244202497.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
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
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 100% |
| LoRA 模型强度 | 0.85 | - | 2 | 100% |
| LoRA 文本强度 | 0.85 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
