---
key: 图片生成/图生图/图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642.json
name: 图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642.json
hash: c117a5216be09835
coverage: 0.870968
learned_at: 2026-10-23 12:41:38
nodes: [KSampler, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, Image Comparer (rgthree), easy cleanGpuUsed, CR Prompt List, easy showAnything, RegexReplace, RegexReplace, RegexReplace, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, String Literal, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, CR Text, SaveImage, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta57", "seed": 581493387965875, "steps": 15, "width": 720}
---

# 图片生成/图生图/图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `CR Prompt List`
- `easy showAnything`
- `RegexReplace`
- `RegexReplace`
- `RegexReplace`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `String Literal`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `581493387965875`
- `steps` = `15`
- `cfg` = `1.1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`KSampler`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VAEDecode`、`ImpactInt`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`CR Prompt List`、`RegexReplace`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`String Literal`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
