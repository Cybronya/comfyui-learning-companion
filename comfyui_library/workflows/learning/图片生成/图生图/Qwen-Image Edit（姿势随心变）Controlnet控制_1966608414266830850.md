---
key: 图片生成/图生图/Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850.json
name: Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850.json
hash: 148c92d91bd65103
coverage: 0.913043
learned_at: 2026-10-23 11:16:20
nodes: [VAELoader, UNETLoader, ImageScaleToTotalPixels, VAEEncode, TextEncodeQwenImageEdit, PreviewImage, ModelSamplingAuraFlow, CFGNorm, VAEDecode, ControlNetApplySD3, ImageConcatMulti, CLIPLoader, KSampler, EmptySD3LatentImage, LoadImage, TextEncodeQwenImageEdit, PreviewImage, LoadImage, AIO_Preprocessor, SetUnionControlNetType, LoraLoaderModelOnly, ControlNetLoader, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.2, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 116185590626487, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image Edit（姿势随心变）Controlnet控制_1966608414266830850.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEdit`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `ControlNetApplySD3` ★核心
- `ImageConcatMulti`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `PreviewImage`
- `LoadImage`
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.2`
- `seed` = `116185590626487`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEEncode`、`TextEncodeQwenImageEdit`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`ControlNetApplySD3`、`ImageConcatMulti`、`CLIPLoader`、`KSampler`、`EmptySD3LatentImage`、`LoadImage`、`AIO_Preprocessor`、`SetUnionControlNetType`、`LoraLoaderModelOnly`、`ControlNetLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
