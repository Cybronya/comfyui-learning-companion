---
key: 平台全量/Qwen_edit_2511 场景-人物-多角度一致性 Qwen Multiangle Camera_2009806612675960833.json
name: Qwen_edit_2511 场景-人物-多角度一致性 Qwen Multiangle Camera_2009806612675960833
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen_edit_2511 场景-人物-多角度一致性 Qwen Multiangle Camera_2009806612675960833.json
hash: 03ae31e67744195f
coverage: 1
learned_at: 2026-11-14 00:53:30
nodes: [LoraLoaderModelOnly, CLIPLoader, ModelSamplingAuraFlow, VAELoader, VAEDecode, VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, KSampler, CR Text, CFGNorm, QwenMultiangleCameraNode, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlus, LoadImage, ImageColorMatch+, SaveImage, Text Concatenate]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 577260705807366, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen_edit_2511 场景-人物-多角度一致性 Qwen Multiangle Camera_2009806612675960833.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen_edit_2511 场景-人物-多角度一致性 Qwen Multiangle Camera_2009806612675960833.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler` ★核心
- `CR Text`
- `CFGNorm`
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `ImageColorMatch+`
- `SaveImage`
- `Text Concatenate`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `577260705807366`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`VAEDecode`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`KSampler`、`CR Text`、`CFGNorm`、`QwenMultiangleCameraNode`、`TextEncodeQwenImageEditPlus`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoadImage`、`ImageColorMatch+`、`SaveImage`、`Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
