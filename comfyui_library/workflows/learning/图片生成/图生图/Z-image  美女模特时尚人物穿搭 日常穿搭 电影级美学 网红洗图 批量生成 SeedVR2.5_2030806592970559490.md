---
key: 图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json
name: Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json
hash: 48534dbac03ac25b
coverage: 0.84
learned_at: 2026-10-23 11:30:08
nodes: [KSampler, CLIPTextEncode, ConditioningZeroOut, VAEDecode, ImpactInt, ImpactInt, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, Image Comparer (rgthree), easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, SaveImage, easy showAnything, easy showAnything, String Literal, easy textSwitch, LoadImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), SaveImage, Qwen3_VQA]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "beta57", "seed": 581493387965875, "steps": 10, "width": 720}
---

# 图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `easy showAnything`
- `easy showAnything`
- `String Literal`
- `easy textSwitch`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Qwen3_VQA`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `581493387965875`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`KSampler`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`ImpactInt`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`SaveImage`、`String Literal`、`easy textSwitch`、`LoadImage`、`EmptyLatentImage`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
