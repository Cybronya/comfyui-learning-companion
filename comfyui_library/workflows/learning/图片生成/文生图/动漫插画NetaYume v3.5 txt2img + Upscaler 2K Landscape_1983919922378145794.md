---
key: 动漫插画NetaYume v3.5 txt2img + Upscaler 2K Landscape_1983919922378145794.json
name: 动漫插画NetaYume v3.5 txt2img + Upscaler 2K Landscape_1983919922378145794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/动漫插画NetaYume v3.5 txt2img + Upscaler 2K Landscape_1983919922378145794.json
hash: 95899ae44bca56a6
coverage: 0.62963
learned_at: 2026-10-10 20:59:37
nodes: [ModelSamplingAuraFlow, ImageUpscaleWithModel, ImageScaleBy, easy cleanGpuUsed, VAEDecode, VAEEncode, VAEDecode, Label (rgthree), easy cleanGpuUsed, MarkdownNote, TiledDiffusion, CLIPTextEncode, Label (rgthree), CLIPTextEncode, KSampler, UpscaleModelLoader, EmptySD3LatentImage, Label (rgthree), SaveImage, StringConcatenate, SaveImage, Image Comparer (rgthree), Fast Groups Muter (rgthree), KSampler, CheckpointLoaderSimple, MarkdownNote, Note]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"cfg": 4, "checkpoint": "netayumeLuminaNetaLumina_v30.safetensors", "denoise": 0.1, "sampler_name": "res_multistep", "scheduler": "linear_quadratic", "seed": 39155128674899, "steps": 15}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 动漫插画NetaYume v3.5 txt2img + Upscaler 2K Landscape_1983919922378145794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/动漫插画NetaYume v3.5 txt2img + Upscaler 2K Landscape_1983919922378145794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Label (rgthree)`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `TiledDiffusion`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UpscaleModelLoader`
- `EmptySD3LatentImage`
- `Label (rgthree)`
- `SaveImage`
- `StringConcatenate`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `Note`

## 关键参数

- `seed` = `39155128674899`
- `steps` = `15`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `linear_quadratic`
- `denoise` = `0.1`
- `checkpoint` = `netayumeLuminaNetaLumina_v30.safetensors`

## 知识

覆盖率 **63%**（17/27）

**有卡**：`ModelSamplingAuraFlow`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEDecode`、`VAEEncode`、`TiledDiffusion`、`CLIPTextEncode`、`KSampler`、`UpscaleModelLoader`、`EmptySD3LatentImage`、`SaveImage`、`StringConcatenate`、`CheckpointLoaderSimple`

**缺卡**（5）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、VAEEncode、ImageUpscaleWithModel、UpscaleModelLoader、UpscaleModelLoader

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
