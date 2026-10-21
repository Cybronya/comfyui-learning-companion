---
key: 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json
name: krea2+Qwen3.5-自动多风格文生图_2072869610650689537
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json
hash: dfe214a2f7d78556
coverage: 0.913043
learned_at: 2026-10-20 00:02:03
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), KSampler, VAEDecode, SaveImage, ConditioningZeroOut, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, llama_cpp_model_loader, LoraLoaderModelOnly, CLIPTextEncode, llama_cpp_instruct_adv, ShowText|pysssss, Label (rgthree), Fast Groups Bypasser (rgthree), CR Prompt Text, llama_cpp_parameters, TTResolutionSelector]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 688602939191126, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
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
- `CR Prompt Text`
- `llama_cpp_parameters`
- `TTResolutionSelector`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `688602939191126`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`Label (rgthree)`、`KSampler`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`CR Prompt Text`、`llama_cpp_parameters`、`TTResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
