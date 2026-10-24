---
key: 图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json
name: QWEN3.5反推Z-image洗图高相似度_2079104428015185922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json
hash: 2a2c4baf0aa2a4cf
coverage: 0.769231
learned_at: 2026-10-23 11:11:17
nodes: [ConditioningZeroOut, CLIPLoader, VAEEncode, CLIPTextEncode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, VAELoader, ImageResizeKJ, VAEDecode, UNETLoader, LoraLoaderModelOnly, PrimitiveFloat, KSampler, SeedVR2VideoUpscaler, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, PrimitiveStringMultiline, easy showAnything, SaveImage, PrimitiveFloat, PreviewImage, LoadImage, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 558904243608776, "steps": 10}
---

# 图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN3.5反推Z-image洗图高相似度_2079104428015185922.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `VAELoader`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `KSampler` ★核心
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `SaveImage`
- `PrimitiveFloat`
- `PreviewImage`
- `LoadImage`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `558904243608776`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`VAEEncode`、`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`VAELoader`、`ImageResizeKJ`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`SeedVR2VideoUpscaler`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
