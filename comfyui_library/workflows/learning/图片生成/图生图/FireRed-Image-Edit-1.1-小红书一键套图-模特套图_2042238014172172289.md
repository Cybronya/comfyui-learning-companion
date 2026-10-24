---
key: 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289.json
name: FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289.json
hash: 03957631b5b5da8c
coverage: 0.965517
learned_at: 2026-10-23 10:55:43
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlus, KSampler, CR Text Replace, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, EmptySD3LatentImage, llama_cpp_parameters, VAEDecode, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage, CR Text, CustomAddLabel, llama_cpp_model_loader, llama_cpp_instruct_adv, JDCN_StringToList, ShowText|pysssss, CR Text, ProcessString, SaveImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 38882299508015, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `CR Text Replace`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `llama_cpp_parameters`
- `VAEDecode` ★核心
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoadImage`
- `CR Text`
- `CustomAddLabel`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `JDCN_StringToList`
- `ShowText|pysssss`
- `CR Text`
- `ProcessString`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `38882299508015`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CR Text Replace`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`llama_cpp_parameters`、`VAEDecode`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`、`CR Text`、`CustomAddLabel`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`JDCN_StringToList`、`ProcessString`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
