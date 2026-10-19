---
key: 图片生成/文生图/会展空间设计 任意角度 3D交互 QwenImage-Edit-2511-Multiple-Angles-LoRA_2010060728585166849.json
name: 会展空间设计 任意角度 3D交互 QwenImage-Edit-2511-Multiple-Angles-LoRA_2010060728585166849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/会展空间设计 任意角度 3D交互 QwenImage-Edit-2511-Multiple-Angles-LoRA_2010060728585166849.json
hash: 6fcd58c79ed81b36
coverage: 0.9375
learned_at: 2026-10-19 22:01:25
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Text Concatenate, Text Concatenate, Text Concatenate, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, CFGNorm, KSampler, VAEDecode, QwenMultiangleCameraNode, LoraLoaderModelOnly, MemoryCleaner, VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, easy showAnything, GetNode, TextEncodeQwenImageEditPlus, PreviewImage, CR Text, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, JDCN_StringToList, SaveImage, SaveImage, RHHiddenNodes, RH_Nano_Banana2_Image2Image, Text Multiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 804510866915356, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/会展空间设计 任意角度 3D交互 QwenImage-Edit-2511-Multiple-Angles-LoRA_2010060728585166849.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/会展空间设计 任意角度 3D交互 QwenImage-Edit-2511-Multiple-Angles-LoRA_2010060728585166849.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Text Concatenate`
- `Text Concatenate`
- `Text Concatenate`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `CFGNorm`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenMultiangleCameraNode`
- `LoraLoaderModelOnly` ★核心
- `MemoryCleaner`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `easy showAnything`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `JDCN_StringToList`
- `SaveImage`
- `SaveImage`
- `RHHiddenNodes`
- `RH_Nano_Banana2_Image2Image`
- `Text Multiline`

## 关键参数

- `seed` = `804510866915356`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（45/48）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CR Text Concatenate`、`Text Concatenate`、`QwenMultiangleCameraNode`、`CFGNorm`、`KSampler`、`VAEDecode`、`MemoryCleaner`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`TextEncodeQwenImageEditPlus`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`JDCN_StringToList`、`SaveImage`、`RHHiddenNodes`、`RH_Nano_Banana2_Image2Image`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CFGNorm、FluxKontextMultiReferenceLatentMethod

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
