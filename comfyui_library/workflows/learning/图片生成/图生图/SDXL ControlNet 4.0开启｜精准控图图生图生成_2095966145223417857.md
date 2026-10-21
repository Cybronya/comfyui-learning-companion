---
key: 图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json
name: SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json
hash: fe8a85b77332f308
coverage: 0.904762
learned_at: 2026-10-21 00:44:16
nodes: [CLIPTextEncode, CLIPTextEncode, VAEEncode, AIO_Preprocessor, ControlNetApplySD3, ControlNetLoader, VAEDecode, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, CheckpointLoaderSimple, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SDXL ControlNet 4.0开启｜精准控图图生图生成_2095966145223417857.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `AIO_Preprocessor`
- `ControlNetApplySD3` ★核心
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `真境写真XL Apex _ 商业电商摄影真实写实大师_真境写真XL_v4.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`AIO_Preprocessor`、`ControlNetApplySD3`、`ControlNetLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
