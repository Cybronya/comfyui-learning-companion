---
key: 平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json
name: 一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json
hash: f0e7b789cb53473b
coverage: 0.826087
learned_at: 2026-11-14 01:30:13
nodes: [PreviewImage, ModelSamplingAuraFlow, UNETLoader, KSampler (Efficient), Prompts Everywhere, PreviewImage, ControlNetInpaintingAliMamaApply, Anything Everywhere, GetImageSize, CLIPTextEncode, CLIPTextEncode, InvertMask, ControlNetLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, EmptyLatentImage, LoadImage, BiRefNet_Hugo, ImageConcanate, SaveImage, LayerFilter: HDREffects, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 257942774124721, "steps": 8, "width": 512}
---

# 平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：QwenImage-InstantX-ControlNet 一键换背，抠图洗图_1967428728403922946.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（23 个）：
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `KSampler (Efficient)` ★核心
- `Prompts Everywhere`
- `PreviewImage`
- `ControlNetInpaintingAliMamaApply`
- `Anything Everywhere`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `InvertMask`
- `ControlNetLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `BiRefNet_Hugo`
- `ImageConcanate`
- `SaveImage`
- `LayerFilter: HDREffects`
- `MarkdownNote`

## 关键参数

- `seed` = `257942774124721`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`ModelSamplingAuraFlow`、`UNETLoader`、`KSampler (Efficient)`、`Prompts Everywhere`、`ControlNetInpaintingAliMamaApply`、`GetImageSize`、`CLIPTextEncode`、`InvertMask`、`ControlNetLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LoadImage`、`BiRefNet_Hugo`、`ImageConcanate`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply
