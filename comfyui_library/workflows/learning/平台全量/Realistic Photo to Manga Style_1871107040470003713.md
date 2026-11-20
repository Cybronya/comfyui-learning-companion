---
key: 平台全量/Realistic Photo to Manga Style_1871107040470003713.json
name: Realistic Photo to Manga Style_1871107040470003713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Realistic Photo to Manga Style_1871107040470003713.json
hash: e6802c259416d9e1
coverage: 0.814815
learned_at: 2026-11-14 00:54:37
nodes: [EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, PortraitMaster_中文版, KSampler, KSampler, CLIPTextEncode, CLIPTextEncode, ControlNetApply, PreviewImage, ShowText|pysssss, CheckpointLoaderSimple, easy promptConcat, easy positive, RH_Captioner, VAEDecode, LoraLoader, DepthAnythingPreprocessor, ControlNetLoader, SaveImage, PreviewImage, CheckpointLoaderSimple, SDXLPromptStyler, VAEEncode, VAEDecode, PreviewImage, Image Comparer (rgthree)]
patterns: [text_to_image, controlnet, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "animagineXLV31_v31.safetensors", "controlnet_strength": 0.6, "denoise": 1, "height": 1368, "lora_name": "残照金 SDXL - Hoko Manga Style_Hoko v1.0.safetensors", "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 355557401450789, "steps": 30, "strength_clip": 1, "strength_model": 0.75, "width": 1024}
---

# 平台全量/Realistic Photo to Manga Style_1871107040470003713.json

> 来源文件 `comfyui_library/workflows/平台全量/Realistic Photo to Manga Style_1871107040470003713.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（27 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PortraitMaster_中文版`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApply` ★核心
- `PreviewImage`
- `ShowText|pysssss`
- `CheckpointLoaderSimple` ★核心
- `easy promptConcat`
- `easy positive`
- `RH_Captioner`
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `DepthAnythingPreprocessor`
- `ControlNetLoader`
- `SaveImage`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `SDXLPromptStyler`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image、controlnet、lora

## 关键参数

- `width` = `1024`
- `height` = `1368`
- `batch_size` = `1`
- `seed` = `355557401450789`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `0.6`
- `checkpoint` = `animagineXLV31_v31.safetensors`
- `lora_name` = `残照金 SDXL - Hoko Manga Style_Hoko v1.0.safetensors`
- `strength_model` = `0.75`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`PortraitMaster_中文版`、`KSampler`、`ControlNetApply`、`CheckpointLoaderSimple`、`easy promptConcat`、`easy positive`、`RH_Captioner`、`VAEDecode`、`LoraLoader`、`DepthAnythingPreprocessor`、`ControlNetLoader`、`SaveImage`、`SDXLPromptStyler`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、ControlNetApply、ControlNetLoader、DepthAnythingPreprocessor
