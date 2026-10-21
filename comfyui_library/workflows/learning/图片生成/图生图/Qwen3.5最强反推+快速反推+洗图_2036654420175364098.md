---
key: 图片生成/图生图/Qwen3.5最强反推+快速反推+洗图_2036654420175364098.json
name: Qwen3.5最强反推+快速反推+洗图_2036654420175364098
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3.5最强反推+快速反推+洗图_2036654420175364098.json
hash: f6accfb142ab5437
coverage: 0.833333
learned_at: 2026-10-21 00:43:46
nodes: [CR Text, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, Image Comparer (rgthree), easy cleanGpuUsed, PrimitiveFloat, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, CheckpointLoaderSimple, CLIPTextEncode, easy showAnything, LoadImage, ImpactInt, VAEEncode, KSampler, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "z-image-turbo-bf16-aio.safetensors", "denoise": 0.9000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 27432532895198, "steps": 10}
---

# 图片生成/图生图/Qwen3.5最强反推+快速反推+洗图_2036654420175364098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3.5最强反推+快速反推+洗图_2036654420175364098.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CR Text`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoadImage`
- `ImpactInt`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `z-image-turbo-bf16-aio.safetensors`
- `seed` = `27432532895198`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.9000000000000001`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CR Text`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LoadImage`、`ImpactInt`、`VAEEncode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、VAEEncode、SaveImage
