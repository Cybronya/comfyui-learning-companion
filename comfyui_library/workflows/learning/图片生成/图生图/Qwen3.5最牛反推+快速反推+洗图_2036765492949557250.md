---
key: 图片生成/图生图/Qwen3.5最牛反推+快速反推+洗图_2036765492949557250.json
name: Qwen3.5最牛反推+快速反推+洗图_2036765492949557250
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3.5最牛反推+快速反推+洗图_2036765492949557250.json
hash: 35aacb843db60944
coverage: 0.833333
learned_at: 2026-10-23 11:19:49
nodes: [llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, CR Text, CheckpointLoaderSimple, VAEEncode, ConditioningZeroOut, ImpactInt, KSampler, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, WujiCleaner, SaveImage, Image Comparer (rgthree), CLIPTextEncode, easy showAnything, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "z-image-turbo-bf16-aio.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 611477634290891, "steps": 10}
---

# 图片生成/图生图/Qwen3.5最牛反推+快速反推+洗图_2036765492949557250.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3.5最牛反推+快速反推+洗图_2036765492949557250.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CR Text`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ImpactInt`
- `KSampler` ★核心
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `WujiCleaner`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `z-image-turbo-bf16-aio.safetensors`
- `seed` = `611477634290891`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`CR Text`、`CheckpointLoaderSimple`、`VAEEncode`、`ConditioningZeroOut`、`ImpactInt`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`WujiCleaner`、`SaveImage`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、VAEEncode、SaveImage
