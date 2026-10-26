---
key: 数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json
name: Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json
hash: ac969ccd2e13c5f0
coverage: 0.789474
learned_at: 2026-10-26 01:58:01
nodes: [UNETLoader, UNETLoader, UpscaleModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Anything Everywhere, VAELoader, Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ClownsharKSampler_Beta, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, ClownsharKSampler_Beta, ModelSamplingSD3, ClownsharKSampler_Beta, String, UpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, StringConcatenate, CLIPLoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), VAEDecode, EmptyHunyuanLatentVideo, Text Multiline, VAEDecode, ImageUpscaleWithModel, SaveImage, LayerFilter: AddGrain]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": 3.500000000000001, "sampler_name": 4, "scheduler": 1, "seed": 0.7500000000000001, "steps": "beta57"}
---

# 数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2真实摄影-Instareal+Lenovo_1979374680974987266.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `ModelSamplingSD3`
- `ClownsharKSampler_Beta` ★核心
- `String`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `CLIPLoader`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `Text Multiline`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `SaveImage`
- `LayerFilter: AddGrain`

## 关键参数

- `seed` = `0.7500000000000001`
- `steps` = `beta57`
- `cfg` = `12`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `3.500000000000001`

## 知识

覆盖率 **79%**（30/38）

**有卡**：`UNETLoader`、`UpscaleModelLoader`、`VAELoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`ClownsharKSampler_Beta`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncode`、`String`、`CLIPTextEncode`、`StringConcatenate`、`CLIPLoader`、`Power Lora Loader (rgthree)`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`Text Multiline`、`SaveImage`、`LayerFilter: AddGrain`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、ClownsharKSampler_Beta、VAEEncode、EmptyHunyuanLatentVideo
