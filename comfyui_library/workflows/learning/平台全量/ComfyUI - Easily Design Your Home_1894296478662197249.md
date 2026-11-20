---
key: 平台全量/ComfyUI - Easily Design Your Home_1894296478662197249.json
name: ComfyUI - Easily Design Your Home_1894296478662197249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI - Easily Design Your Home_1894296478662197249.json
hash: a8d3a5c6790e900c
coverage: 0.764706
learned_at: 2026-11-14 00:22:16
nodes: [LineArtPreprocessor, ControlNetLoader, PreviewImage, Seed Everywhere, KSampler, Anything Everywhere, Anything Everywhere, CLIPTextEncode, ControlNetLoader, MiDaS-DepthMapPreprocessor, ControlNetLoader, PreviewImage, VAEEncode, VAEDecode, Anything Everywhere, CheckpointLoaderSimple, EmptyLatentImage, SaveImage, VAEDecode, PreviewImage, LoadImage, KSampler, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ControlNetApply, ControlNetApply, ControlNetApply, PreviewImage, CannyEdgePreprocessor, PreviewImage, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image, image_to_image, controlnet]
missing: []
parameters: {"batch_size": 1, "cfg": 12, "checkpoint": "pirsusEpicRealism_pirsusEpicRealismV50.safetensors", "controlnet_strength": 0.89, "denoise": 0.8, "height": 1024, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 407360270760615, "steps": 35, "width": 768}
---

# 平台全量/ComfyUI - Easily Design Your Home_1894296478662197249.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI - Easily Design Your Home_1894296478662197249.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LineArtPreprocessor`
- `ControlNetLoader`
- `PreviewImage`
- `Seed Everywhere`
- `KSampler` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `MiDaS-DepthMapPreprocessor`
- `ControlNetLoader`
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ControlNetApply` ★核心
- `ControlNetApply` ★核心
- `ControlNetApply` ★核心
- `PreviewImage`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、image_to_image、controlnet

## 关键参数

- `seed` = `407360270760615`
- `steps` = `35`
- `cfg` = `12`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`
- `checkpoint` = `pirsusEpicRealism_pirsusEpicRealismV50.safetensors`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.89`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`LineArtPreprocessor`、`ControlNetLoader`、`Seed Everywhere`、`KSampler`、`CLIPTextEncode`、`MiDaS-DepthMapPreprocessor`、`VAEEncode`、`VAEDecode`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`SaveImage`、`LoadImage`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ControlNetApply`、`CannyEdgePreprocessor`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、CannyEdgePreprocessor、ControlNetApply
