---
key: 图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json
name: 多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json
hash: 6765943e97f3b018
coverage: 0.884615
learned_at: 2026-10-20 01:00:33
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), KSampler, VAEDecode, SaveImage, ConditioningZeroOut, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, llama_cpp_model_loader, LoraLoaderModelOnly, CLIPTextEncode, llama_cpp_instruct_adv, ShowText|pysssss, Label (rgthree), Fast Groups Bypasser (rgthree), llama_cpp_parameters, TTResolutionSelector, CR Prompt Text, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
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
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_parameters`
- `TTResolutionSelector`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **88%**（46/52）

**有卡**：`Label (rgthree)`、`KSampler`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`TTResolutionSelector`、`CR Prompt Text`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
