---
key: 平台全量/LoFi Neko Geisha Wallpaper Generator_1863845137196711938.json
name: LoFi Neko Geisha Wallpaper Generator_1863845137196711938
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/LoFi Neko Geisha Wallpaper Generator_1863845137196711938.json
hash: c36a7a78afb52428
coverage: 0.83871
learned_at: 2026-11-14 00:39:23
nodes: [TextInput_, TextInput_, TextInput_, CLIPTextEncode, UltralyticsDetectorProvider, SAMLoader, CLIPTextEncode, StringFunction|pysssss, CheckpointLoaderSimple, LatentUpscaleBy, VAEDecode, CLIPSetLastLayer, LoraLoader, FaceDetailer, UltimateSDUpscale, UpscaleModelLoader, Image Filter Adjustments, SaveImage, PreviewImage, ShowText|pysssss, StringFunction|pysssss, Text Random Line, Text Multiline, EmptyLatentImage, VAELoader, VAEDecode, PreviewImage, KSampler, Reroute, KSampler, PreviewImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 6.5, "checkpoint": "ghostmix_v20Bakedvae.safetensors", "denoise": 0.55, "height": 640, "lora_name": "SDXL_offset_example-lora_1.0.safetensors", "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 51133915093576, "steps": 25, "strength_clip": 0.3, "strength_model": 0.3, "width": 960}
---

# 平台全量/LoFi Neko Geisha Wallpaper Generator_1863845137196711938.json

> 来源文件 `comfyui_library/workflows/平台全量/LoFi Neko Geisha Wallpaper Generator_1863845137196711938.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `CLIPTextEncode` ★核心
- `StringFunction|pysssss`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleBy`
- `VAEDecode` ★核心
- `CLIPSetLastLayer`
- `LoraLoader` ★核心
- `FaceDetailer`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `Image Filter Adjustments`
- `SaveImage`
- `PreviewImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Random Line`
- `Text Multiline`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `Reroute`
- `KSampler` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `checkpoint` = `ghostmix_v20Bakedvae.safetensors`
- `lora_name` = `SDXL_offset_example-lora_1.0.safetensors`
- `strength_model` = `0.3`
- `strength_clip` = `0.3`
- `width` = `960`
- `height` = `640`
- `batch_size` = `1`
- `seed` = `51133915093576`
- `steps` = `25`
- `cfg` = `6.5`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `0.55`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`TextInput_`、`CLIPTextEncode`、`UltralyticsDetectorProvider`、`SAMLoader`、`StringFunction|pysssss`、`CheckpointLoaderSimple`、`LatentUpscaleBy`、`VAEDecode`、`CLIPSetLastLayer`、`LoraLoader`、`FaceDetailer`、`UltimateSDUpscale`、`UpscaleModelLoader`、`Image Filter Adjustments`、`SaveImage`、`Text Random Line`、`Text Multiline`、`EmptyLatentImage`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LatentUpscaleBy、LoraLoader
