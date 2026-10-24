---
key: 图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json
name: krea2+Qwen3.5-自动多风格文生图_2084922609443102721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json
hash: 9cabe10057d01f82
coverage: 0.9
learned_at: 2026-10-23 11:40:17
nodes: [Label (rgthree), ConditioningZeroOut, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, llama_cpp_model_loader, LoraLoaderModelOnly, CLIPTextEncode, llama_cpp_instruct_adv, ShowText|pysssss, llama_cpp_parameters, TTResolutionSelector, Fast Groups Bypasser (rgthree), CR Prompt Text, KSampler, Label (rgthree), SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 177623707248379, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Output → Other

**节点**（20 个）：
- `Label (rgthree)`
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
- `llama_cpp_parameters`
- `TTResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `KSampler` ★核心
- `Label (rgthree)`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `177623707248379`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`Label (rgthree)`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`TTResolutionSelector`、`CR Prompt Text`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
