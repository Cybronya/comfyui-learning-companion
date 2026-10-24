---
key: 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2062492218727952386.json
name: ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2062492218727952386
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2062492218727952386.json
hash: 7e4be1ce000d153d
coverage: 0.705882
learned_at: 2026-10-23 11:33:38
nodes: [SetNode, SetNode, SetNode, easy promptLine, GetNode, ModelSamplingAuraFlow, CFGNorm, PlaySound|pysssss, PlaySound|pysssss, INTConstant, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, JjkText, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, UNETLoader, VAEDecode, LayerUtility: PurgeVRAM, SetNode, PlaySound|pysssss, LoadImage, LoadImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, JjkText, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 902836816090552, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2062492218727952386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ai动漫短剧ai短12种镜头场景生成多角度人物多角度多场景Qwen-multiple-angles版_2062492218727952386.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `easy promptLine`
- `GetNode`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `INTConstant`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `JjkText`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `PlaySound|pysssss`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JjkText`
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `902836816090552`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`easy promptLine`、`ModelSamplingAuraFlow`、`CFGNorm`、`PlaySound|pysssss`、`INTConstant`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
