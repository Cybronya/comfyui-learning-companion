---
key: 平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json
name: 一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json
hash: 1944242ddfde8cde
coverage: 0.857143
learned_at: 2026-11-14 01:30:11
nodes: [PreviewImage, ModelSamplingAuraFlow, Prompts Everywhere, CLIPTextEncode, GetImageSize, CLIPTextEncode, ImageConcanate, PreviewImage, ControlNetLoader, LoraLoaderModelOnly, CLIPLoader, ControlNetInpaintingAliMamaApply, VAELoader, ImagePadForOutpaint, UNETLoader, EmptyLatentImage, KSampler (Efficient), LoadImage, SaveImage, LayerFilter: HDREffects, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 555828933637924, "steps": 20, "width": 512}
---

# 平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Qwen-Image-ControlNet-Inpainting  扩图 ，修复_1967768450057854978.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（21 个）：
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `PreviewImage`
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ControlNetInpaintingAliMamaApply`
- `VAELoader`
- `ImagePadForOutpaint`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `SaveImage`
- `LayerFilter: HDREffects`
- `MarkdownNote`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `555828933637924`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ModelSamplingAuraFlow`、`Prompts Everywhere`、`CLIPTextEncode`、`GetImageSize`、`ImageConcanate`、`ControlNetLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ControlNetInpaintingAliMamaApply`、`VAELoader`、`ImagePadForOutpaint`、`UNETLoader`、`EmptyLatentImage`、`KSampler (Efficient)`、`LoadImage`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply
