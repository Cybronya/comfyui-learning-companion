---
key: 图片生成/图生图/模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618.json
name: 模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618.json
hash: b03c1fde59a1a64d
coverage: 0.880952
learned_at: 2026-10-23 13:10:11
nodes: [VAELoader, UpscaleModelLoader, VAEEncode, CLIPTextEncode, ImageUpscaleWithModel, CLIPLoader, VAEDecodeTiled, KSampler, UNETLoader, CLIPTextEncode, LoraLoader, easy imageListToImageBatch, KSampler, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, VAEEncode, LoraLoaderModelOnly, UNETLoader, llama_cpp_parameters, easy cleanGpuUsed, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, Reroute, TTP_Image_Tile_Batch, VAEDecode, LayerUtility: PurgeVRAM V2, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, ShowText|pysssss, TTP_Image_Assy, PreviewImage, Image Comparer (rgthree), Miaoshouai_Tagger, easy imageBatchToImageList, TTP_Tile_image_size, SaveImage, ImageLoader, Text]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 966957250604545, "steps": 9, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
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
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Miaoshouai_Tagger`
- `easy imageBatchToImageList`
- `TTP_Tile_image_size`
- `SaveImage`
- `ImageLoader`
- `Text`

**识别到的模式**：lora

## 关键参数

- `seed` = `966957250604545`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7500000000000001`
- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`

## 知识

覆盖率 **88%**（37/42）

**有卡**：`VAELoader`、`UpscaleModelLoader`、`VAEEncode`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`CLIPLoader`、`VAEDecodeTiled`、`KSampler`、`UNETLoader`、`LoraLoader`、`easy imageListToImageBatch`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`TTP_Image_Tile_Batch`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`TTP_Image_Assy`、`Miaoshouai_Tagger`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`SaveImage`、`ImageLoader`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
