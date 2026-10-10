---
key: Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json
name: Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json
hash: d8d4e1591c27f131
coverage: 0.62
learned_at: 2026-10-10 20:59:15
nodes: [UNETLoader, UNETLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Anything Everywhere, VAELoader, PathchSageAttentionKJ, CLIPLoader, PreviewImage, ClownsharKSampler_Beta, Note, String, WanVideoNAG, StringConcatenate, ModelSamplingSD3, Reroute, CR SDXL Aspect Ratio, EmptyHunyuanLatentVideo, ClownsharKSampler_Beta, VAEEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleBy, ImageUpscaleWithModel, LayerFilter: AddGrain, UpscaleModelLoader, VAEDecode, VAEDecode, ClownsharKSampler_Beta, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), PathchSageAttentionKJ, ModelSamplingSD3, Power Lora Loader (rgthree), Power Lora Loader (rgthree), RH_Translator, CLIPTextEncode, CLIPTextEncode, LoadImage, Joy_caption_two_load, easy textSwitch, Int, Note, ShowText|pysssss, Joy_caption_two]
patterns: []
missing: [LayerFilter: AddGrain, easy textSwitch, CR SDXL Aspect Ratio, Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
parameters: {"cfg": 3, "denoise": 2.0000000000000004, "sampler_name": -1, "scheduler": 0.30000000000000004, "seed": 0.30000000000000004, "steps": "bong_tangent"}
discoveries: [次要节点 `LayerFilter: AddGrain` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2超真实摄影-Instareal+Lenovo【LORA】_1960338805641441282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Anything Everywhere`
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `PreviewImage`
- `ClownsharKSampler_Beta` ★核心
- `Note`
- `String`
- `WanVideoNAG`
- `StringConcatenate`
- `ModelSamplingSD3`
- `Reroute`
- `CR SDXL Aspect Ratio`
- `EmptyHunyuanLatentVideo`
- `ClownsharKSampler_Beta` ★核心
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LayerFilter: AddGrain`
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ClownsharKSampler_Beta` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Joy_caption_two_load`
- `easy textSwitch`
- `Int`
- `Note`
- `ShowText|pysssss`
- `Joy_caption_two`

## 关键参数

- `seed` = `0.30000000000000004`
- `steps` = `bong_tangent`
- `cfg` = `3`
- `sampler_name` = `-1`
- `scheduler` = `0.30000000000000004`
- `denoise` = `2.0000000000000004`

## 知识

覆盖率 **62%**（31/50）

**有卡**：`UNETLoader`、`VAELoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`ClownsharKSampler_Beta`、`String`、`WanVideoNAG`、`StringConcatenate`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`VAEEncode`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleBy`、`VAEDecode`、`SaveImage`、`RH_Translator`、`CLIPTextEncode`、`LoadImage`、`Joy_caption_two_load`、`Int`、`Joy_caption_two`

**缺卡**（5）：`LayerFilter: AddGrain`、`easy textSwitch`、`CR SDXL Aspect Ratio`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、ClownsharKSampler_Beta、VAEEncode

## 学习发现

- 次要节点 `LayerFilter: AddGrain` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
