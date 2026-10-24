---
key: 图片生成/图生图/FireRed-Image-edit1.1电商模特出图_2031377996577251330.json
name: FireRed-Image-edit1.1电商模特出图_2031377996577251330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1电商模特出图_2031377996577251330.json
hash: 126f485b438bfccc
coverage: 0.925926
learned_at: 2026-10-23 10:55:52
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, CFGNorm, EmptySD3LatentImage, llama_cpp_model_loader, llama_cpp_parameters, CR Text Replace, llama_cpp_instruct_adv, MemoryCleaner, CR Text, ProcessString, JDCN_StringToList, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ShowText|pysssss, KSampler, UNETLoader, VAEDecode, LoadImage, PreviewImage, SaveImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1007281521062450, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1电商模特出图_2031377996577251330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1电商模特出图_2031377996577251330.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CFGNorm`
- `EmptySD3LatentImage`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text Replace`
- `llama_cpp_instruct_adv`
- `MemoryCleaner`
- `CR Text`
- `ProcessString`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ShowText|pysssss`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `CR Text`

## 关键参数

- `seed` = `1007281521062450`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`CFGNorm`、`EmptySD3LatentImage`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text Replace`、`llama_cpp_instruct_adv`、`MemoryCleaner`、`CR Text`、`ProcessString`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`KSampler`、`UNETLoader`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
