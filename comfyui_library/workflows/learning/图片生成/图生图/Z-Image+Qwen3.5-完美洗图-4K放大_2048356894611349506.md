---
key: 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json
name: Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json
hash: c8dc29a89595b9b2
coverage: 0.906977
learned_at: 2026-10-23 11:29:28
nodes: [VAELoader, UpscaleModelLoader, VAEEncode, CLIPTextEncode, ImageUpscaleWithModel, CLIPLoader, VAEDecodeTiled, KSampler, TTP_Tile_image_size, easy imageBatchToImageList, UNETLoader, CLIPTextEncode, LoraLoader, easy imageListToImageBatch, KSampler, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, VAEEncode, LoraLoaderModelOnly, UNETLoader, llama_cpp_parameters, easy cleanGpuUsed, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, Reroute, TTP_Image_Assy, ImageLoader, TTP_Image_Tile_Batch, VAEDecode, LayerUtility: PurgeVRAM V2, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, Miaoshouai_Tagger, ShowText|pysssss, SaveImage, SaveImage, Image Comparer (rgthree), Text, AddLabel]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 425124092345534, "steps": 9, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAELoader`
- `UpscaleModelLoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `easy imageListToImageBatch`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `llama_cpp_parameters`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Reroute`
- `TTP_Image_Assy`
- `ImageLoader`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `Miaoshouai_Tagger`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Text`
- `AddLabel`

**识别到的模式**：lora

## 关键参数

- `seed` = `425124092345534`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7500000000000001`
- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`VAELoader`、`UpscaleModelLoader`、`VAEEncode`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`CLIPLoader`、`VAEDecodeTiled`、`KSampler`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`UNETLoader`、`LoraLoader`、`easy imageListToImageBatch`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`TTP_Image_Assy`、`ImageLoader`、`TTP_Image_Tile_Batch`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`Miaoshouai_Tagger`、`SaveImage`、`Text`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
