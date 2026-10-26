---
key: 图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json
name: Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json
hash: 57bc1e6ebb85361a
coverage: 0.87234
learned_at: 2026-10-26 01:46:36
nodes: [VAELoader, UpscaleModelLoader, VAEEncode, CLIPTextEncode, ImageUpscaleWithModel, CLIPLoader, VAEDecodeTiled, KSampler, UNETLoader, CLIPTextEncode, easy imageListToImageBatch, llama_cpp_parameters, easy cleanGpuUsed, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, Reroute, TTP_Image_Tile_Batch, LayerUtility: PurgeVRAM V2, VAELoader, ShowText|pysssss, Text, TTP_Image_Assy, PreviewImage, SaveImage, Image Comparer (rgthree), Miaoshouai_Tagger, easy imageBatchToImageList, TTP_Tile_image_size, ImageLoader, LoadImage, CLIPTextEncode, LoraLoader, ImageScaleToTotalPixels, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VAEEncode, CLIPLoader, ModelSamplingAuraFlow, VAEDecode, KSampler, Note, LoraLoaderModelOnly, LazySwitch1way, easy boolean]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1113435480372639, "steps": 9, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Z-Image+Qwen3.5-完美洗图-4K放大_2067395166289354754.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `VAELoader`
- `UpscaleModelLoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy imageListToImageBatch`
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Reroute`
- `TTP_Image_Tile_Batch`
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `ShowText|pysssss`
- `Text`
- `TTP_Image_Assy`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Miaoshouai_Tagger`
- `easy imageBatchToImageList`
- `TTP_Tile_image_size`
- `ImageLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LazySwitch1way`
- `easy boolean`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `1113435480372639`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7500000000000001`
- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`VAELoader`、`UpscaleModelLoader`、`VAEEncode`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`CLIPLoader`、`VAEDecodeTiled`、`KSampler`、`UNETLoader`、`easy imageListToImageBatch`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`TTP_Image_Tile_Batch`、`LayerUtility: PurgeVRAM V2`、`Text`、`TTP_Image_Assy`、`SaveImage`、`Miaoshouai_Tagger`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`ImageLoader`、`LoadImage`、`LoraLoader`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`VAEDecode`、`LoraLoaderModelOnly`、`LazySwitch1way`、`easy boolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
