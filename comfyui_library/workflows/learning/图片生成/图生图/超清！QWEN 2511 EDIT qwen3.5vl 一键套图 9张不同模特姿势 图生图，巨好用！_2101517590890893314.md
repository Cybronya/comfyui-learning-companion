---
key: 图片生成/图生图/超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314.json
name: 超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314.json
hash: 694de7e234eb2add
coverage: 0.925926
learned_at: 2026-10-21 00:56:37
nodes: [llama_cpp_parameters, CR Text, JDCN_StringToList, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SaveImage, EmptySD3LatentImage, CFGNorm, KSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, ModelSamplingAuraFlow, LoadImage, llama_cpp_model_loader, ShowText|pysssss, ProcessString, PreviewImage, GetImageSize, llama_cpp_instruct_adv, CR Text Replace, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 213129027014620, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `llama_cpp_parameters`
- `CR Text`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `CFGNorm`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `LoadImage`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `ProcessString`
- `PreviewImage`
- `GetImageSize`
- `llama_cpp_instruct_adv`
- `CR Text Replace`
- `CR Text`

## 关键参数

- `seed` = `213129027014620`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`llama_cpp_parameters`、`CR Text`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SaveImage`、`EmptySD3LatentImage`、`CFGNorm`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`LoadImage`、`llama_cpp_model_loader`、`ProcessString`、`GetImageSize`、`llama_cpp_instruct_adv`、`CR Text Replace`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
