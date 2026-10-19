---
key: 图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json
name: Wan2.2真实摄影_1994369665260457985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json
hash: 913707d5ccd03864
coverage: 0.738095
learned_at: 2026-10-19 21:32:44
nodes: [UNETLoader, UNETLoader, UpscaleModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Anything Everywhere, VAELoader, Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ClownsharKSampler_Beta, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, ClownsharKSampler_Beta, VAEDecode, ImageUpscaleWithModel, CR SDXL Aspect Ratio, EmptyHunyuanLatentVideo, ModelSamplingSD3, ClownsharKSampler_Beta, String, Fast Groups Bypasser (rgthree), UpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, StringConcatenate, CLIPLoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), LayerFilter: AddGrain, PreviewImage, VAEDecode, Text Multiline, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": 3.500000000000001, "sampler_name": 4, "scheduler": 1, "seed": 0.7500000000000001, "steps": "beta57"}
---

# 图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2真实摄影_1994369665260457985.json`

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
- `ClownsharKSampler_Beta` ★核心
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
- `PreviewImage`
- `VAEDecode` ★核心
- `Text Multiline`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `0.7500000000000001`
- `steps` = `beta57`
- `cfg` = `12`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `3.500000000000001`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`UNETLoader`、`UpscaleModelLoader`、`VAELoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`ClownsharKSampler_Beta`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncode`、`VAEDecode`、`CR SDXL Aspect Ratio`、`EmptyHunyuanLatentVideo`、`String`、`CLIPTextEncode`、`StringConcatenate`、`CLIPLoader`、`Power Lora Loader (rgthree)`、`LayerFilter: AddGrain`、`Text Multiline`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ClownsharKSampler_Beta、VAEEncode、EmptyHunyuanLatentVideo
