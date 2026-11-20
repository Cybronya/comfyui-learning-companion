---
key: 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json
name: 一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json
hash: 7b2f30031066ad34
coverage: 0.863636
learned_at: 2026-11-14 01:30:05
nodes: [PreviewImage, ModelSamplingAuraFlow, Prompts Everywhere, CLIPTextEncode, CLIPTextEncode, PreviewImage, UNETLoader, ImageConcanate, KSampler (Efficient), ControlNetInpaintingAliMamaApply, ImagePadForOutpaint, LoadImage, ApplyFBCacheOnModel, DualCLIPLoader, VAELoader, EmptyLatentImage, GetImageSize, ControlNetLoader, LoraLoaderModelOnly, SaveImage, LayerFilter: HDREffects, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 381020040323994, "steps": 20, "width": 512}
---

# 平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Flux-dev-fp8-ControlNet-Inpainting 扩图工作流图像修复_1970313299302772737.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（22 个）：
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `ImageConcanate`
- `KSampler (Efficient)` ★核心
- `ControlNetInpaintingAliMamaApply`
- `ImagePadForOutpaint`
- `LoadImage`
- `ApplyFBCacheOnModel`
- `DualCLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LayerFilter: HDREffects`
- `MarkdownNote`

## 关键参数

- `seed` = `381020040323994`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`ModelSamplingAuraFlow`、`Prompts Everywhere`、`CLIPTextEncode`、`UNETLoader`、`ImageConcanate`、`KSampler (Efficient)`、`ControlNetInpaintingAliMamaApply`、`ImagePadForOutpaint`、`LoadImage`、`ApplyFBCacheOnModel`、`DualCLIPLoader`、`VAELoader`、`EmptyLatentImage`、`GetImageSize`、`ControlNetLoader`、`LoraLoaderModelOnly`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply、ControlNetLoader
