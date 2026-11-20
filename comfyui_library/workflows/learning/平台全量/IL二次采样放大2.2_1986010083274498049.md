---
key: 平台全量/IL二次采样放大2.2_1986010083274498049.json
name: IL二次采样放大2.2_1986010083274498049
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/IL二次采样放大2.2_1986010083274498049.json
hash: ccabf522ed222e56
coverage: 0.705882
learned_at: 2026-11-14 00:32:24
nodes: [LoraLoader|pysssss, VAEDecodeTiled, PreviewImage, PreviewImage, UpscaleModelLoader, CLIPTextEncode, Note, VAEEncode, VAEDecodeTiled, Note, easy imageScaleDownToSize, ImageScaleBy, KSampler, ImageUpscaleWithModel, VAEEncodeTiled, CheckpointLoaderSimple, CLIPSetLastLayer, LoadImage, KSampler, Note, Note, SaveImage, Image Comparer (rgthree), WD14Tagger|pysssss, ShowText|pysssss, Joy_caption_two_load, Joy_caption_two, ShowText|pysssss, LoraLoader|pysssss, Fast Groups Muter (rgthree), ConditioningCombine, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5.8, "checkpoint": "waiNSFWIllustrious_v140.safetensors", "denoise": 0.45000000000000007, "lora_name": "anime_screencap-IllustriousV2.safetensors", "sampler_name": "dpmpp_3m_sde", "scheduler": "karras", "seed": 70634031580945, "steps": 20, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/IL二次采样放大2.2_1986010083274498049.json

> 来源文件 `comfyui_library/workflows/平台全量/IL二次采样放大2.2_1986010083274498049.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoraLoader|pysssss` ★核心
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `PreviewImage`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `easy imageScaleDownToSize`
- `ImageScaleBy`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `VAEEncodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPSetLastLayer`
- `LoadImage`
- `KSampler` ★核心
- `Note`
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `ShowText|pysssss`
- `LoraLoader|pysssss` ★核心
- `Fast Groups Muter (rgthree)`
- `ConditioningCombine`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `lora_name` = `anime_screencap-IllustriousV2.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `70634031580945`
- `steps` = `20`
- `cfg` = `5.8`
- `sampler_name` = `dpmpp_3m_sde`
- `scheduler` = `karras`
- `denoise` = `0.45000000000000007`
- `checkpoint` = `waiNSFWIllustrious_v140.safetensors`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`LoraLoader|pysssss`、`VAEDecodeTiled`、`UpscaleModelLoader`、`CLIPTextEncode`、`VAEEncode`、`easy imageScaleDownToSize`、`ImageScaleBy`、`KSampler`、`ImageUpscaleWithModel`、`VAEEncodeTiled`、`CheckpointLoaderSimple`、`CLIPSetLastLayer`、`LoadImage`、`SaveImage`、`WD14Tagger|pysssss`、`Joy_caption_two_load`、`Joy_caption_two`、`ConditioningCombine`、`easy cleanGpuUsed`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEDecodeTiled、VAEEncode、VAEEncodeTiled、LoraLoader|pysssss

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
