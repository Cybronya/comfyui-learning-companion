---
key: 图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA 任意角度-3D交互_2013984068286812161.json
name: Qwen-Image-Edit-2511-Multiple-Angles-LoRA 任意角度-3D交互_2013984068286812161
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA 任意角度-3D交互_2013984068286812161.json
hash: 56e7a5d032672208
coverage: 0.954545
learned_at: 2026-10-23 11:16:50
nodes: [LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, CFGNorm, FluxKontextMultiReferenceLatentMethod, KSampler, VAEEncode, FluxKontextMultiReferenceLatentMethod, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Text Concatenate, Text Concatenate, JDCN_StringToList, easy showAnything, PreviewImage, LoadImage, CR Text Concatenate, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text Concatenate, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, TextEncodeQwenImageEditPlus, Text Concatenate, MemoryCleaner, VAEDecode, SaveImage, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, LoraLoaderModelOnly, ModelSamplingAuraFlow]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 258952739891807, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA 任意角度-3D交互_2013984068286812161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-2511-Multiple-Angles-LoRA 任意角度-3D交互_2013984068286812161.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Text Concatenate`
- `Text Concatenate`
- `JDCN_StringToList`
- `easy showAnything`
- `PreviewImage`
- `LoadImage`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `CR Text Concatenate`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `Text Concatenate`
- `MemoryCleaner`
- `VAEDecode` ★核心
- `SaveImage`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `258952739891807`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`VAEEncode`、`CR Text Concatenate`、`Text Concatenate`、`JDCN_StringToList`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`QwenMultiangleCameraNode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`MemoryCleaner`、`VAEDecode`、`SaveImage`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
