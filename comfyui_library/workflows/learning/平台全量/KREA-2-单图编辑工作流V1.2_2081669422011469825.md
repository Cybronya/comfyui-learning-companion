---
key: 平台全量/KREA-2-单图编辑工作流V1.2_2081669422011469825.json
name: KREA-2-单图编辑工作流V1.2_2081669422011469825
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/KREA-2-单图编辑工作流V1.2_2081669422011469825.json
hash: 0a0c318b2f711c4e
coverage: 0.9
learned_at: 2026-11-14 00:33:20
nodes: [ConditioningZeroOut, KSampler, VAEEncode, CLIPLoader, llama_cpp_model_loader, EmptySD3LatentImage, GetImageSize, ResizeImageMaskNode, LoadImage, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, UNETLoader, VAEDecode, llama_cpp_instruct_adv, PreviewAny, CR Text, Krea2EditGroundedEncode, VAELoader, Krea2EditModelPatch]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1038847628311833, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/KREA-2-单图编辑工作流V1.2_2081669422011469825.json

> 来源文件 `comfyui_library/workflows/平台全量/KREA-2-单图编辑工作流V1.2_2081669422011469825.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `llama_cpp_model_loader`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ResizeImageMaskNode`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `CR Text`
- `Krea2EditGroundedEncode`
- `VAELoader`
- `Krea2EditModelPatch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1038847628311833`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEEncode`、`CLIPLoader`、`llama_cpp_model_loader`、`EmptySD3LatentImage`、`GetImageSize`、`ResizeImageMaskNode`、`LoadImage`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`llama_cpp_instruct_adv`、`CR Text`、`Krea2EditGroundedEncode`、`VAELoader`、`Krea2EditModelPatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
