---
key: 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530.json
name: FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530.json
hash: 074c1d7158d06b1e
coverage: 0.969697
learned_at: 2026-10-23 10:55:42
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlus, KSampler, CR Text Replace, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, EmptySD3LatentImage, llama_cpp_parameters, VAEDecode, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage, CustomAddLabel, llama_cpp_model_loader, llama_cpp_instruct_adv, JDCN_StringToList, ProcessString, SaveImage, SaveImage, RH_Utils, Int, MultiTextConcatenate, Text, CR Text, ShowText|pysssss, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 912636019354196, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
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
- `CustomAddLabel`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `JDCN_StringToList`
- `ProcessString`
- `SaveImage`
- `SaveImage`
- `RH_Utils`
- `Int`
- `MultiTextConcatenate`
- `Text`
- `CR Text`
- `ShowText|pysssss`
- `Text`

## 关键参数

- `seed` = `912636019354196`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CR Text Replace`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`EmptySD3LatentImage`、`llama_cpp_parameters`、`VAEDecode`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`、`CustomAddLabel`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`JDCN_StringToList`、`ProcessString`、`SaveImage`、`RH_Utils`、`MultiTextConcatenate`、`Text`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
