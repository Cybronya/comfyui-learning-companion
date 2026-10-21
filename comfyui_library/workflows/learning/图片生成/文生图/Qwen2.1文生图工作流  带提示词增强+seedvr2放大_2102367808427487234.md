---
key: 图片生成/文生图/Qwen2.1文生图工作流  带提示词增强+seedvr2放大_2102367808427487234.json
name: Qwen2.1文生图工作流  带提示词增强+seedvr2放大_2102367808427487234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图工作流  带提示词增强+seedvr2放大_2102367808427487234.json
hash: 6b194b14b9d923a0
coverage: 0.903226
learned_at: 2026-10-20 01:51:24
nodes: [VAELoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, SeedVR2VideoUpscaler, ConditioningZeroOut, TextEncodeQwenImage21, CLIPLoader, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21Cache, QwenImage21SageAttentionT8, EmptyLatentImage, LoraLoaderModelOnly, LoadImage, LoadImage, SaveImage, StringConstantMultiline, ResolutionSelector, CLIPLoader, easy int, LoadImage, Fast Groups Muter (rgthree), UNETLoader, TextGenerate, SaveImage, Note, KSampler, easy clearCacheAll, VAEDecode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 496263248741195, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图工作流  带提示词增强+seedvr2放大_2102367808427487234.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图工作流  带提示词增强+seedvr2放大_2102367808427487234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `ConditioningZeroOut`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `QwenImage21Cache`
- `QwenImage21SageAttentionT8`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `StringConstantMultiline`
- `ResolutionSelector`
- `CLIPLoader`
- `easy int`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `TextGenerate`
- `SaveImage`
- `Note`
- `KSampler` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `496263248741195`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`ConditioningZeroOut`、`TextEncodeQwenImage21`、`CLIPLoader`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21Cache`、`QwenImage21SageAttentionT8`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`、`StringConstantMultiline`、`ResolutionSelector`、`easy int`、`UNETLoader`、`TextGenerate`、`KSampler`、`easy clearCacheAll`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
