---
key: 平台全量/Portrait Re-imagined Upscaler_1868565425884905474.json
name: Portrait Re-imagined Upscaler_1868565425884905474
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Portrait Re-imagined Upscaler_1868565425884905474.json
hash: 60b6ca240a98a2a4
coverage: 0.8
learned_at: 2026-11-14 00:48:30
nodes: [ImageUpscaleWithModel, Image Filter Adjustments, PreviewImage, ControlNetApply, CLIPTextEncode, CLIPTextEncode, KSampler, ControlNetApply, Canny, Reroute, AV_ControlNetPreprocessor, Reroute, MiDaS-DepthMapPreprocessor, ImageUpscaleWithModel, VAEEncode, VAEDecode, UltimateSDUpscale, Float, VAEDecode, KSampler, PreviewImage, PreviewImage, ResizeImageMixlab, LoadImage, PreviewImage, Float, ImageScaleDownToSize, PreviewImage, PreviewImage, LatentUpscaleBy, PreviewImage, UltimateSDUpscale, UpscaleModelLoader, ResizeImageMixlab, UpscaleModelLoader, VAELoader, CheckpointLoaderSimple, AV_ControlNetPreprocessor, ControlNetLoader, ControlNetLoader, UpscaleModelLoader, TextInput_, TextInput_, StringFunction|pysssss, SaveImage]
patterns: [image_to_image, controlnet]
missing: []
parameters: {"cfg": 8, "checkpoint": "realisticVisionV30_v30VAE    _realisticVision.safetensors", "controlnet_strength": 0.8, "denoise": 0.02, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "seed": 581660958803120, "steps": 40}
---

# 平台全量/Portrait Re-imagined Upscaler_1868565425884905474.json

> 来源文件 `comfyui_library/workflows/平台全量/Portrait Re-imagined Upscaler_1868565425884905474.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ImageUpscaleWithModel`
- `Image Filter Adjustments`
- `PreviewImage`
- `ControlNetApply` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ControlNetApply` ★核心
- `Canny`
- `Reroute`
- `AV_ControlNetPreprocessor`
- `Reroute`
- `MiDaS-DepthMapPreprocessor`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `UltimateSDUpscale`
- `Float`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `ResizeImageMixlab`
- `LoadImage`
- `PreviewImage`
- `Float`
- `ImageScaleDownToSize`
- `PreviewImage`
- `PreviewImage`
- `LatentUpscaleBy`
- `PreviewImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `ResizeImageMixlab`
- `UpscaleModelLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `AV_ControlNetPreprocessor`
- `ControlNetLoader`
- `ControlNetLoader`
- `UpscaleModelLoader`
- `TextInput_`
- `TextInput_`
- `StringFunction|pysssss`
- `SaveImage`

**识别到的模式**：image_to_image、controlnet

## 关键参数

- `controlnet_strength` = `0.8`
- `seed` = `581660958803120`
- `steps` = `40`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `karras`
- `denoise` = `0.02`
- `checkpoint` = `realisticVisionV30_v30VAE    _realisticVision.safetensors`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`ImageUpscaleWithModel`、`Image Filter Adjustments`、`ControlNetApply`、`CLIPTextEncode`、`KSampler`、`Canny`、`AV_ControlNetPreprocessor`、`MiDaS-DepthMapPreprocessor`、`VAEEncode`、`VAEDecode`、`UltimateSDUpscale`、`Float`、`ResizeImageMixlab`、`LoadImage`、`ImageScaleDownToSize`、`LatentUpscaleBy`、`UpscaleModelLoader`、`VAELoader`、`CheckpointLoaderSimple`、`ControlNetLoader`、`TextInput_`、`StringFunction|pysssss`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、AV_ControlNetPreprocessor、Canny
