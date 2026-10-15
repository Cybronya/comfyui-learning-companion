---
key: 图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json
name: 商K-真实摄影Wan2.2_1982596622628593665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json
hash: 5cb6a8b1a170c593
coverage: 0.738095
learned_at: 2026-10-15 22:28:23
nodes: [UNETLoader, UNETLoader, UpscaleModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Anything Everywhere, VAELoader, Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, ClownsharKSampler_Beta, VAEDecode, ImageUpscaleWithModel, CR SDXL Aspect Ratio, EmptyHunyuanLatentVideo, ModelSamplingSD3, ClownsharKSampler_Beta, Image Comparer (rgthree), String, Fast Groups Bypasser (rgthree), UpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, StringConcatenate, CLIPLoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), LayerFilter: AddGrain, SaveImage, PreviewImage, VAEDecode, Text Multiline, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": 3.500000000000001, "sampler_name": 4, "scheduler": 1, "seed": 0.7500000000000001, "steps": "beta57"}
---

# 图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Anything Everywhere`
- `VAELoader`
- `Reroute`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `CR SDXL Aspect Ratio`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ClownsharKSampler_Beta` ★核心
- `Image Comparer (rgthree)`
- `String`
- `Fast Groups Bypasser (rgthree)`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `CLIPLoader`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `LayerFilter: AddGrain`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `Text Multiline`
- `RHHiddenNodes`

## 关键参数

- `seed` = `0.7500000000000001`
- `steps` = `beta57`
- `cfg` = `12`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `3.500000000000001`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`UNETLoader`、`UpscaleModelLoader`、`VAELoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncode`、`ClownsharKSampler_Beta`、`VAEDecode`、`CR SDXL Aspect Ratio`、`EmptyHunyuanLatentVideo`、`String`、`CLIPTextEncode`、`StringConcatenate`、`CLIPLoader`、`Power Lora Loader (rgthree)`、`LayerFilter: AddGrain`、`SaveImage`、`Text Multiline`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ClownsharKSampler_Beta、VAEEncode、EmptyHunyuanLatentVideo
