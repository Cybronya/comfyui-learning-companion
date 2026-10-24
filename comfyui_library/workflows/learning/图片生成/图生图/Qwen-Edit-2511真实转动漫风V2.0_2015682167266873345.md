---
key: 图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json
name: Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json
hash: 9860b31c772d7d98
coverage: 0.952381
learned_at: 2026-10-23 11:15:57
nodes: [ModelSamplingAuraFlow, VAELoader, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, CFGNorm, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextImageScale, VAEEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, SaveImage, VAEDecode, LoadImage, PreviewImage, AddLabel, AddLabel, ImageConcatMulti]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 958349171877359, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit-2511真实转动漫风V2.0_2015682167266873345.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `VAELoader`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `CFGNorm`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `958349171877359`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ModelSamplingAuraFlow`、`VAELoader`、`FluxKontextMultiReferenceLatentMethod`、`CFGNorm`、`KSampler`、`TextEncodeQwenImageEditPlus`、`FluxKontextImageScale`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`、`VAEDecode`、`LoadImage`、`AddLabel`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
