---
key: 视频生成/图生视频/固定人物IP多场景生成V3.0（IP打造）人物一致性多图编辑_2041990716972343297.json
name: 固定人物IP多场景生成V3.0（IP打造）人物一致性多图编辑_2041990716972343297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041990716972343297.json
hash: e81c4b0a72f1e529
coverage: 0.896552
learned_at: 2026-10-15 22:36:23
nodes: [CLIPLoader, VAELoader, VAEDecode, Note, LoadImage, TextEncodeQwenImageEditPlus, Note, UNETLoader, CFGNorm, EmptySD3LatentImage, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, CR Text, ProcessString, TextEncodeQwenImageEditPlus, CR Text Replace, JDCN_StringToList, MemoryCleaner, llama_cpp_instruct_adv, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, llama_cpp_model_loader, llama_cpp_parameters, MemoryCleaner, CR Text, ShowText|pysssss, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 795981201643997, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/固定人物IP多场景生成V3.0（IP打造）人物一致性多图编辑_2041990716972343297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041990716972343297.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `UNETLoader` ★核心
- `CFGNorm`
- `EmptySD3LatentImage`
- `GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `ProcessString`
- `TextEncodeQwenImageEditPlus`
- `CR Text Replace`
- `JDCN_StringToList`
- `MemoryCleaner`
- `llama_cpp_instruct_adv`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `MemoryCleaner`
- `CR Text`
- `ShowText|pysssss`
- `SaveImage`

## 关键参数

- `seed` = `795981201643997`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`CFGNorm`、`EmptySD3LatentImage`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`ProcessString`、`CR Text Replace`、`JDCN_StringToList`、`MemoryCleaner`、`llama_cpp_instruct_adv`、`KSampler`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
