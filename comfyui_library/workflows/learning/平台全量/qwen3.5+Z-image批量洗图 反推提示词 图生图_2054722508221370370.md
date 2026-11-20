---
key: 平台全量/qwen3.5+Z-image批量洗图 反推提示词 图生图_2054722508221370370.json
name: qwen3.5+Z-image批量洗图 反推提示词 图生图_2054722508221370370
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen3.5+Z-image批量洗图 反推提示词 图生图_2054722508221370370.json
hash: 1eddff62cf729d64
coverage: 0.870968
learned_at: 2026-11-14 01:16:35
nodes: [KSampler, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, Image Comparer (rgthree), easy cleanGpuUsed, CR Prompt List, easy showAnything, RegexReplace, RegexReplace, RegexReplace, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, String Literal, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, CR Text, Fast Groups Bypasser (rgthree), SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta57", "seed": 581493387965875, "steps": 15, "width": 720}
---

# 平台全量/qwen3.5+Z-image批量洗图 反推提示词 图生图_2054722508221370370.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen3.5+Z-image批量洗图 反推提示词 图生图_2054722508221370370.json`

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
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LoadImage`

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

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
