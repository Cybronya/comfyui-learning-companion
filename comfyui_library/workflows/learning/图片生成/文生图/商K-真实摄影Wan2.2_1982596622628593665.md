---
key: 图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json
name: 商K-真实摄影Wan2.2_1982596622628593665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json
hash: 5cb6a8b1a170c593
coverage: 0.619048
learned_at: 2026-10-10 20:59:40
nodes: [UNETLoader, UNETLoader, UpscaleModelLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Anything Everywhere, VAELoader, Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoNAG, ModelSamplingSD3, ImageUpscaleWithModel, ImageScaleBy, VAEEncode, ClownsharKSampler_Beta, VAEDecode, ImageUpscaleWithModel, CR SDXL Aspect Ratio, EmptyHunyuanLatentVideo, ModelSamplingSD3, ClownsharKSampler_Beta, Image Comparer (rgthree), String, Fast Groups Bypasser (rgthree), UpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, StringConcatenate, CLIPLoader, Power Lora Loader (rgthree), Power Lora Loader (rgthree), LayerFilter: AddGrain, SaveImage, PreviewImage, VAEDecode, Text Multiline, RHHiddenNodes]
patterns: []
missing: [LayerFilter: AddGrain, Text Multiline, CR SDXL Aspect Ratio, Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
parameters: {"cfg": 12, "denoise": 3.500000000000001, "sampler_name": 4, "scheduler": 1, "seed": 0.7500000000000001, "steps": "beta57"}
discoveries: [次要节点 `LayerFilter: AddGrain` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/商K-真实摄影Wan2.2_1982596622628593665.json`

## 结构

**节点**（42 个）：
- `UNETLoader`
- `UNETLoader`
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
- `VAEEncode`
- `ClownsharKSampler_Beta`
- `VAEDecode`
- `ImageUpscaleWithModel`
- `CR SDXL Aspect Ratio`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ClownsharKSampler_Beta`
- `Image Comparer (rgthree)`
- `String`
- `Fast Groups Bypasser (rgthree)`
- `UpscaleModelLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `StringConcatenate`
- `CLIPLoader`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `LayerFilter: AddGrain`
- `SaveImage`
- `PreviewImage`
- `VAEDecode`
- `Text Multiline`
- `RHHiddenNodes`

## 关键参数

- `cfg` = `12`
- `denoise` = `3.500000000000001`
- `sampler_name` = `4`
- `scheduler` = `1`
- `seed` = `0.7500000000000001`
- `steps` = `beta57`

## 知识

覆盖率 **62%**（26/42）

**有卡**：`UNETLoader`、`UpscaleModelLoader`、`Reroute`、`Anything Everywhere`、`VAELoader`、`PathchSageAttentionKJ`、`WanVideoNAG`、`ModelSamplingSD3`、`ImageUpscaleWithModel`、`ImageScaleBy`、`VAEEncode`、`ClownsharKSampler_Beta`、`VAEDecode`、`CR SDXL Aspect Ratio`、`EmptyHunyuanLatentVideo`

**缺卡**（5）：`LayerFilter: AddGrain`、`Text Multiline`、`CR SDXL Aspect Ratio`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

## 学习发现

- 次要节点 `LayerFilter: AddGrain` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
