---
key: 图片生成/图生图/FireRED-image-edit-1.1-for循环测试lora强度_2030842101193252865.json
name: FireRED-image-edit-1.1-for循环测试lora强度_2030842101193252865
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRED-image-edit-1.1-for循环测试lora强度_2030842101193252865.json
hash: 32ed49355ed35176
coverage: 0.852941
learned_at: 2026-10-23 10:55:23
nodes: [CFGNorm, easy forLoopStart, MathExpression|pysssss, easy batchAnything, CR Text, Float, Note, Seed (rgthree), ModelSamplingAuraFlow, LoadImage, LoadImage, easy convertAnything, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextImageScale, VAEEncode, KSampler, VAEDecode, AddLabel, easy forLoopEnd, easy promptConcat, easy showAnything, PreviewImage, SaveImage, LoadImage, PreviewImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 640548578031595, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRED-image-edit-1.1-for循环测试lora强度_2030842101193252865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRED-image-edit-1.1-for循环测试lora强度_2030842101193252865.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（34 个）：
- `CFGNorm`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `easy batchAnything`
- `CR Text`
- `Float`
- `Note`
- `Seed (rgthree)`
- `ModelSamplingAuraFlow`
- `LoadImage`
- `LoadImage`
- `easy convertAnything`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `easy forLoopEnd`
- `easy promptConcat`
- `easy showAnything`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `640548578031595`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`CFGNorm`、`easy forLoopStart`、`MathExpression|pysssss`、`easy batchAnything`、`CR Text`、`Float`、`Seed (rgthree)`、`ModelSamplingAuraFlow`、`LoadImage`、`easy convertAnything`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`FluxKontextImageScale`、`VAEEncode`、`KSampler`、`VAEDecode`、`AddLabel`、`easy forLoopEnd`、`easy promptConcat`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
