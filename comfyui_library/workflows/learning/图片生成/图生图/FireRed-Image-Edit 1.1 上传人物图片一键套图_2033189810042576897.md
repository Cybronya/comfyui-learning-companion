---
key: 图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json
name: FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json
hash: 578a80206125ee8f
coverage: 0.964286
learned_at: 2026-10-23 10:55:31
nodes: [LoadImage, CR Text Replace, CR Text, CR Text, ProcessString, JDCN_StringToList, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, ShowText|pysssss, KSampler, EmptySD3LatentImage, ModelSamplingAuraFlow, CFGNorm, VAEDecode, SaveImage, CustomAddLabel, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 74584826546263, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `LoadImage`
- `CR Text Replace`
- `CR Text`
- `CR Text`
- `ProcessString`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `ShowText|pysssss`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `SaveImage`
- `CustomAddLabel`
- `SaveImage`

## 关键参数

- `seed` = `74584826546263`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`LoadImage`、`CR Text Replace`、`CR Text`、`ProcessString`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`KSampler`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`SaveImage`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
