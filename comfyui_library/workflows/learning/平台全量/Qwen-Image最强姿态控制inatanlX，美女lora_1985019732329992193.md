---
key: 平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json
name: Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json
hash: f8e936c273977a4f
coverage: 0.793103
learned_at: 2026-11-14 00:51:54
nodes: [SetUnionControlNetType, AIO_Preprocessor, AIO_Preprocessor, PreviewImage, PreviewImage, PreviewImage, LoraLoaderModelOnly, ControlNetLoader, UNETLoader, LoraLoaderModelOnly, ImageScaleToTotalPixels, AIO_Preprocessor, VAEDecode, KSampler, Image Comparer (rgthree), Int, GetImageSize, ImpactSwitch, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoadImage, EmptySD3LatentImage, ControlNetApplyAdvanced, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, SaveImage, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1062937138191704, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image最强姿态控制inatanlX，美女lora_1985019732329992193.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Int`
- `GetImageSize`
- `ImpactSwitch`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `EmptySD3LatentImage`
- `ControlNetApplyAdvanced` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `1062937138191704`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`SetUnionControlNetType`、`AIO_Preprocessor`、`LoraLoaderModelOnly`、`ControlNetLoader`、`UNETLoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`KSampler`、`Int`、`GetImageSize`、`CLIPLoader`、`VAELoader`、`LoadImage`、`EmptySD3LatentImage`、`ControlNetApplyAdvanced`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
