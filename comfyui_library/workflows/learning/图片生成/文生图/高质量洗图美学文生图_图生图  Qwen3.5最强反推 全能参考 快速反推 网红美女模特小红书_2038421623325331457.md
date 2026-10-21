---
key: 图片生成/文生图/高质量洗图美学文生图_图生图  Qwen3.5最强反推 全能参考 快速反推 网红美女模特小红书_2038421623325331457.json
name: 高质量洗图美学文生图_图生图  Qwen3.5最强反推 全能参考 快速反推 网红美女模特小红书_2038421623325331457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/高质量洗图美学文生图_图生图  Qwen3.5最强反推 全能参考 快速反推 网红美女模特小红书_2038421623325331457.json
hash: 3ae793a91811105e
coverage: 0.833333
learned_at: 2026-10-21 03:03:24
nodes: [CR Text, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, PrimitiveFloat, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, CheckpointLoaderSimple, CLIPTextEncode, easy showAnything, ImpactInt, VAEEncode, KSampler, SaveImage, easy cleanGpuUsed, LoadImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "z-image-turbo-bf16-aio.safetensors", "denoise": 0.9000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 961595414279112, "steps": 10}
---

# 图片生成/文生图/高质量洗图美学文生图_图生图  Qwen3.5最强反推 全能参考 快速反推 网红美女模特小红书_2038421623325331457.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/高质量洗图美学文生图_图生图  Qwen3.5最强反推 全能参考 快速反推 网红美女模特小红书_2038421623325331457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CR Text`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `PrimitiveFloat`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `ImpactInt`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `easy cleanGpuUsed`
- `LoadImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `z-image-turbo-bf16-aio.safetensors`
- `seed` = `961595414279112`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.9000000000000001`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CR Text`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ImpactInt`、`VAEEncode`、`KSampler`、`SaveImage`、`easy cleanGpuUsed`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、VAEEncode、SaveImage
