---
key: 平台全量/sd1.5-老照片修复上色_1887073323971670017.json
name: sd1.5-老照片修复上色_1887073323971670017
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/sd1.5-老照片修复上色_1887073323971670017.json
hash: 8e3600f057554d68
coverage: 0.857143
learned_at: 2026-11-14 01:17:15
nodes: [SaveImage, Image Comparer (rgthree), SaveImage, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetApplyAdvanced, KSampler, ReActorFaceSwap, OpenposePreprocessor, ControlNetLoader, LineArtPreprocessor, ControlNetLoader, VAEEncode, VAEDecode, ImageUpscaleWithModel, PreviewImage, PreviewImage, UpscaleModelLoader, VAELoader, CLIPTextEncode, Zoe-DepthMapPreprocessor, LoadImage, Joy_caption_two, Joy_caption_two_load, CheckpointLoaderSimple, PreviewImage, ControlNetLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7.5, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 0.4, "denoise": 0.6, "sampler_name": "euler", "scheduler": "karras", "seed": 451038105179118, "steps": 25}
---

# 平台全量/sd1.5-老照片修复上色_1887073323971670017.json

> 来源文件 `comfyui_library/workflows/平台全量/sd1.5-老照片修复上色_1887073323971670017.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `ReActorFaceSwap`
- `OpenposePreprocessor`
- `ControlNetLoader`
- `LineArtPreprocessor`
- `ControlNetLoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `PreviewImage`
- `PreviewImage`
- `UpscaleModelLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Zoe-DepthMapPreprocessor`
- `LoadImage`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.4`
- `seed` = `451038105179118`
- `steps` = `25`
- `cfg` = `7.5`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `0.6`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`SaveImage`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`KSampler`、`ReActorFaceSwap`、`OpenposePreprocessor`、`ControlNetLoader`、`LineArtPreprocessor`、`VAEEncode`、`VAEDecode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VAELoader`、`Zoe-DepthMapPreprocessor`、`LoadImage`、`Joy_caption_two`、`Joy_caption_two_load`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
