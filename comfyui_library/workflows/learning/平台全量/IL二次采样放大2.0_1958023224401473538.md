---
key: 平台全量/IL二次采样放大2.0_1958023224401473538.json
name: IL二次采样放大2.0_1958023224401473538
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/IL二次采样放大2.0_1958023224401473538.json
hash: e01ba72bcdc8c653
coverage: 0.851852
learned_at: 2026-11-14 00:32:23
nodes: [CLIPSetLastLayer, LoraLoader|pysssss, ImageUpscaleWithModel, UpscaleModelLoader, PreviewImage, SaveImage, PreviewImage, VAEEncode, KSampler, VAEDecodeTiled, easy cleanGpuUsed, VAEEncodeTiled, Note, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), KSampler, VAEDecodeTiled, ImageScaleBy, CheckpointLoaderSimple, LoraLoader|pysssss, LoadImage, ConditioningCombine, Joy_caption_two_load, Joy_caption_two, ShowText, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5.8, "checkpoint": "WAI_NSFW-illustrious-SDXL_v14.safetensors", "denoise": 0.4, "lora_name": "anime_screencap-IllustriousV2.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "normal", "seed": 71552544484631, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/IL二次采样放大2.0_1958023224401473538.json

> 来源文件 `comfyui_library/workflows/平台全量/IL二次采样放大2.0_1958023224401473538.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPSetLastLayer`
- `LoraLoader|pysssss` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `VAEEncodeTiled` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `ImageScaleBy`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader|pysssss` ★核心
- `LoadImage`
- `ConditioningCombine`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `ShowText`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `lora_name` = `anime_screencap-IllustriousV2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `71552544484631`
- `steps` = `20`
- `cfg` = `5.8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `normal`
- `denoise` = `0.4`
- `checkpoint` = `WAI_NSFW-illustrious-SDXL_v14.safetensors`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPSetLastLayer`、`LoraLoader|pysssss`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SaveImage`、`VAEEncode`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`VAEEncodeTiled`、`CLIPTextEncode`、`ImageScaleBy`、`CheckpointLoaderSimple`、`LoadImage`、`ConditioningCombine`、`Joy_caption_two_load`、`Joy_caption_two`、`ShowText`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEDecodeTiled、VAEEncode、VAEEncodeTiled、LoraLoader|pysssss

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
