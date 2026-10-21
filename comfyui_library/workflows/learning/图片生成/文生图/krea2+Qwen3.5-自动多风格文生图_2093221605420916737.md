---
key: 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json
name: krea2+Qwen3.5-自动多风格文生图_2093221605420916737
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json
hash: 994d226c7db7a13e
coverage: 0.913043
learned_at: 2026-10-20 01:19:41
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), KSampler, VAEDecode, SaveImage, ConditioningZeroOut, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, llama_cpp_model_loader, LoraLoaderModelOnly, CLIPTextEncode, llama_cpp_instruct_adv, ShowText|pysssss, Label (rgthree), Fast Groups Bypasser (rgthree), llama_cpp_parameters, TTResolutionSelector, CR Prompt Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 185656107928773, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json`

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
- `llama_cpp_parameters`
- `TTResolutionSelector`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `185656107928773`
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

**有卡**：`Label (rgthree)`、`KSampler`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`llama_cpp_model_loader`、`CLIPTextEncode`、`llama_cpp_instruct_adv`、`llama_cpp_parameters`、`TTResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
