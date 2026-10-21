---
key: 图片生成/图生图/Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586.json
name: Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586.json
hash: 45f13bf67c27c8dd
coverage: 0.870968
learned_at: 2026-10-21 00:44:46
nodes: [KSampler, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, VAEDecode, ImpactInt, ImpactInt, SaveImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, Image Comparer (rgthree), easy cleanGpuUsed, CR Prompt List, easy showAnything, RegexReplace, RegexReplace, RegexReplace, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, String Literal, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, CR Text, LoadImage, Fast Groups Bypasser (rgthree), easy showAnything, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta57", "seed": 581493387965875, "steps": 15, "width": 720}
---

# 图片生成/图生图/Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586.json`

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
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `easy showAnything`
- `SaveImage`

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
