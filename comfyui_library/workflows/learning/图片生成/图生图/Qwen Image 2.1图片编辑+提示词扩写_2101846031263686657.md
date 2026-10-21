---
key: 图片生成/图生图/Qwen Image 2.1图片编辑+提示词扩写_2101846031263686657.json
name: Qwen Image 2.1图片编辑+提示词扩写_2101846031263686657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑+提示词扩写_2101846031263686657.json
hash: 9e8713bde9f8051e
coverage: 0.851852
learned_at: 2026-10-21 00:42:30
nodes: [CLIPLoader, TextEncodeQwenImage21, KSampler, VAEDecode, PathchSageAttentionKJ, QwenImage21Cache, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, BatchImagesNode, LoadImage, VAELoader, ImpactInt, Fast Groups Bypasser (rgthree), CR Text, RegexReplace, ComfySwitchNode, Compare, Int, ImpactInt, ImpactInt, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, easy showAnything, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 763622512274669, "steps": 30, "width": 864}
---

# 图片生成/图生图/Qwen Image 2.1图片编辑+提示词扩写_2101846031263686657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图片编辑+提示词扩写_2101846031263686657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `BatchImagesNode`
- `LoadImage`
- `VAELoader`
- `ImpactInt`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `RegexReplace`
- `ComfySwitchNode`
- `Compare`
- `Int`
- `ImpactInt`
- `ImpactInt`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `763622512274669`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `864`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPLoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`BatchImagesNode`、`LoadImage`、`VAELoader`、`ImpactInt`、`CR Text`、`RegexReplace`、`Compare`、`Int`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
