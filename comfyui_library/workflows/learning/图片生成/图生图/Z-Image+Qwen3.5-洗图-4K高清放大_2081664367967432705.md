---
key: 图片生成/图生图/Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705.json
name: Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705.json
hash: 12df1fd165949d1b
coverage: 0.906977
learned_at: 2026-10-23 11:29:30
nodes: [easy cleanGpuUsed, Reroute, VAEDecode, LayerUtility: PurgeVRAM V2, VAEEncode, llama_cpp_model_loader, llama_cpp_parameters, Text, ImageLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, CLIPLoader, VAELoader, ModelSamplingAuraFlow, VAEEncode, Miaoshouai_Tagger, CLIPLoader, VAELoader, UpscaleModelLoader, CLIPTextEncode, LoraLoader, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleToTotalPixels, CLIPTextEncode, UNETLoader, easy imageBatchToImageList, CLIPTextEncode, CLIPTextEncode, SaveImage, ImageUpscaleWithModel, ShowText|pysssss, KSampler, Image Comparer (rgthree), easy imageListToImageBatch, VAEDecodeTiled, TTP_Image_Assy, AddLabel, SaveImage, KSampler, llama_cpp_instruct_adv, easy showAnything]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Gundam_RX78_Flux.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 389217164952951, "steps": 9, "strength_clip": 0.85, "strength_model": 0.85}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `easy cleanGpuUsed`
- `Reroute`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `Text`
- `ImageLoader`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `Miaoshouai_Tagger`
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageUpscaleWithModel`
- `ShowText|pysssss`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `easy imageListToImageBatch`
- `VAEDecodeTiled` ★核心
- `TTP_Image_Assy`
- `AddLabel`
- `SaveImage`
- `KSampler` ★核心
- `llama_cpp_instruct_adv`
- `easy showAnything`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Gundam_RX78_Flux.safetensors`
- `strength_model` = `0.85`
- `strength_clip` = `0.85`
- `seed` = `389217164952951`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（39/43）

**有卡**：`easy cleanGpuUsed`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`Text`、`ImageLoader`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Miaoshouai_Tagger`、`UpscaleModelLoader`、`CLIPTextEncode`、`LoraLoader`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`easy imageBatchToImageList`、`SaveImage`、`ImageUpscaleWithModel`、`KSampler`、`easy imageListToImageBatch`、`VAEDecodeTiled`、`TTP_Image_Assy`、`AddLabel`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
