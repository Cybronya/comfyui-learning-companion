---
key: 平台全量/IL二次采样放大2.1_1972146629300121601.json
name: IL二次采样放大2.1_1972146629300121601
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/IL二次采样放大2.1_1972146629300121601.json
hash: 8d421c656ac39567
coverage: 0.827586
learned_at: 2026-11-14 00:32:23
nodes: [CLIPSetLastLayer, LoraLoader|pysssss, ImageUpscaleWithModel, UpscaleModelLoader, PreviewImage, SaveImage, PreviewImage, VAEDecodeTiled, easy cleanGpuUsed, VAEEncodeTiled, Image Comparer (rgthree), KSampler, ImageScaleBy, CheckpointLoaderSimple, LoraLoader|pysssss, ConditioningCombine, Joy_caption_two_load, Joy_caption_two, ShowText, VAEDecodeTiled, VAEEncode, easy imageScaleDownToSize, Note, KSampler, Note, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5.8, "checkpoint": "WAI_NSFW-illustrious-SDXL_v14.safetensors", "denoise": 0.4, "lora_name": "anime_screencap-IllustriousV2.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "normal", "seed": 565291438495078, "steps": 36, "strength_clip": 1, "strength_model": 1}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/IL二次采样放大2.1_1972146629300121601.json

> 来源文件 `comfyui_library/workflows/平台全量/IL二次采样放大2.1_1972146629300121601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPSetLastLayer`
- `LoraLoader|pysssss` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `VAEEncodeTiled` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `ImageScaleBy`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader|pysssss` ★核心
- `ConditioningCombine`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `ShowText`
- `VAEDecodeTiled` ★核心
- `VAEEncode` ★核心
- `easy imageScaleDownToSize`
- `Note`
- `KSampler` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `lora_name` = `anime_screencap-IllustriousV2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `565291438495078`
- `steps` = `36`
- `cfg` = `5.8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `normal`
- `denoise` = `0.4`
- `checkpoint` = `WAI_NSFW-illustrious-SDXL_v14.safetensors`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`CLIPSetLastLayer`、`LoraLoader|pysssss`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SaveImage`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`VAEEncodeTiled`、`KSampler`、`ImageScaleBy`、`CheckpointLoaderSimple`、`ConditioningCombine`、`Joy_caption_two_load`、`Joy_caption_two`、`ShowText`、`VAEEncode`、`easy imageScaleDownToSize`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEDecodeTiled、VAEEncode、VAEEncodeTiled、LoraLoader|pysssss

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
