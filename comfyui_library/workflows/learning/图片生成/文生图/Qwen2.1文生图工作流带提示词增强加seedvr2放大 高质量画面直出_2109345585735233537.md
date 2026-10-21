---
key: 图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json
name: Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json
hash: c73dea76a1976521
coverage: 0.892857
learned_at: 2026-10-21 02:54:45
nodes: [VAELoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, SeedVR2VideoUpscaler, ConditioningZeroOut, TextEncodeQwenImage21, CLIPLoader, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, QwenImage21Cache, QwenImage21SageAttentionT8, EmptyLatentImage, LoraLoaderModelOnly, SaveImage, StringConstantMultiline, ResolutionSelector, CLIPLoader, easy int, Fast Groups Muter (rgthree), UNETLoader, TextGenerate, SaveImage, KSampler, easy clearCacheAll, VAEDecode, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
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
- `SaveImage`
- `StringConstantMultiline`
- `ResolutionSelector`
- `CLIPLoader`
- `easy int`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `TextGenerate`
- `SaveImage`
- `KSampler` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`ConditioningZeroOut`、`TextEncodeQwenImage21`、`CLIPLoader`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`QwenImage21Cache`、`QwenImage21SageAttentionT8`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`SaveImage`、`StringConstantMultiline`、`ResolutionSelector`、`easy int`、`UNETLoader`、`TextGenerate`、`KSampler`、`easy clearCacheAll`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
