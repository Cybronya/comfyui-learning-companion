---
key: 图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json
name: Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json
hash: 87bfd9306be4d430
coverage: 0.857143
learned_at: 2026-10-21 02:51:42
nodes: [UNETLoader, ConditioningZeroOut, CLIPLoader, VAELoader, ConditioningZeroOut, CLIPTextEncode, ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEDecode, UNETLoader, llama_cpp_model_loader, ShowText|pysssss, CLIPTextEncode, EmptySD3LatentImage, EmptyLatentImage, KSampler, VAEDecode, PreviewImage, AddLabel, llama_cpp_instruct_adv, KSampler, PreviewImage, JDCN_StringToList, AddLabel, PreviewImage, ImageConcatMulti, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 152980574255591, "steps": 8, "width": 896}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ernie-image-turbo与Z-image-turbo对比工作流_2044632672093343745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `AddLabel`
- `llama_cpp_instruct_adv`
- `KSampler` ★核心
- `PreviewImage`
- `JDCN_StringToList`
- `AddLabel`
- `PreviewImage`
- `ImageConcatMulti`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `896`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `152980574255591`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAEDecode`、`llama_cpp_model_loader`、`EmptySD3LatentImage`、`EmptyLatentImage`、`KSampler`、`AddLabel`、`llama_cpp_instruct_adv`、`JDCN_StringToList`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
