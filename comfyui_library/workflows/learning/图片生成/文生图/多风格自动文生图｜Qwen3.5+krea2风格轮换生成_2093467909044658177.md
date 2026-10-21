---
key: 图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json
name: 多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json
hash: 2fd25526ed9e51ef
coverage: 0.875
learned_at: 2026-10-20 01:20:09
nodes: [KSampler, VAEDecode, SaveImage, ConditioningZeroOut, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, llama_cpp_model_loader, LoraLoaderModelOnly, CLIPTextEncode, llama_cpp_instruct_adv, ShowText|pysssss, Fast Groups Bypasser (rgthree), llama_cpp_parameters, TTResolutionSelector, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（48 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `llama_cpp_model_loader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_parameters`
- `TTResolutionSelector`
- `CR Prompt Text`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（42/48）

**有卡**：`KSampler`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`TTResolutionSelector`、`CR Prompt Text`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
