---
key: 图片生成/图生图/8步Lightning+Controlnet+upscale_1899406787970514946.json
name: 8步Lightning+Controlnet+upscale_1899406787970514946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/8步Lightning+Controlnet+upscale_1899406787970514946.json
hash: 15938f552bcca54e
coverage: 0.961538
learned_at: 2026-10-23 10:50:05
nodes: [ImageScaleToMegapixels, RepeatLatentBatch, VAEEncode, VAEDecode, VAEEncode, CLIPTextEncode, CLIPTextEncode, ImageScaleToMegapixels, KSampler, UpscaleModelLoader, AIO_Preprocessor, EmptyLatentImage, SetUnionControlNetType, ControlNetApplySD3, KSampler, AIO_Preprocessor, LoadImage, DeepTranslatorTextNode, ControlNetLoader, ControlNetLoader, CheckpointLoaderSimple, easy imageChooser, ControlNetApplySD3, PreviewImage, VAEDecodeTiled, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 8, "cfg": 1.2, "checkpoint": "juggernautXL_juggXILightningByRD.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1032, "steps": 10, "width": 1280}
---

# 图片生成/图生图/8步Lightning+Controlnet+upscale_1899406787970514946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/8步Lightning+Controlnet+upscale_1899406787970514946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ImageScaleToMegapixels`
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `AIO_Preprocessor`
- `EmptyLatentImage` ★核心
- `SetUnionControlNetType`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `DeepTranslatorTextNode`
- `ControlNetLoader`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `easy imageChooser`
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1032`
- `steps` = `10`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `8`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `juggernautXL_juggXILightningByRD.safetensors`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ImageScaleToMegapixels`、`RepeatLatentBatch`、`VAEEncode`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`UpscaleModelLoader`、`AIO_Preprocessor`、`EmptyLatentImage`、`SetUnionControlNetType`、`ControlNetApplySD3`、`LoadImage`、`DeepTranslatorTextNode`、`ControlNetLoader`、`CheckpointLoaderSimple`、`easy imageChooser`、`VAEDecodeTiled`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、SetUnionControlNetType
