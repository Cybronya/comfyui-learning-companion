---
key: 图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json
name: 百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json
hash: 32a861cf2b782128
coverage: 0.857143
learned_at: 2026-10-21 03:02:09
nodes: [UNETLoader, VAELoader, EmptyLatentImage, CLIPLoader, CLIPTextEncode, llama_cpp_model_loader, ConditioningZeroOut, SaveImage, KSampler, VAEDecode, PreviewImage, CR Prompt Text, ShowText|pysssss, llama_cpp_instruct_adv]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 874618786620111, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `ConditioningZeroOut`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `CR Prompt Text`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `874618786620111`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`CLIPTextEncode`、`llama_cpp_model_loader`、`ConditioningZeroOut`、`SaveImage`、`KSampler`、`VAEDecode`、`CR Prompt Text`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
