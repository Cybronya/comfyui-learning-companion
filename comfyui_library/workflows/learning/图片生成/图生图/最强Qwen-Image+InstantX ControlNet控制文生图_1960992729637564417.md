---
key: 图片生成/图生图/最强Qwen-Image+InstantX ControlNet控制文生图_1960992729637564417.json
name: 最强Qwen-Image+InstantX ControlNet控制文生图_1960992729637564417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强Qwen-Image+InstantX ControlNet控制文生图_1960992729637564417.json
hash: 36a8669f2c205744
coverage: 0.862069
learned_at: 2026-10-23 13:05:34
nodes: [VAELoader, ImageConcanate, VAEDecode, SeedVR2GGUF, ImageConcanate, ControlNetLoader, SetUnionControlNetType, ControlNetApplyAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, UnetLoaderGGUF, KSampler, ModelSamplingAuraFlow, CFGNorm, PresetTextSelector, PrimitiveStringMultiline, EmptySD3LatentImage, AIO_Preprocessor, CLIPLoader, LoraLoaderModelOnly, ImageScaleToTotalPixels, easy promptConcat, CLIPTextEncode, CLIPTextEncode, SaveImage, PreviewImage, PreviewImage, RHHiddenNodes, ShowText|pysssss]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 383275926264952, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/最强Qwen-Image+InstantX ControlNet控制文生图_1960992729637564417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强Qwen-Image+InstantX ControlNet控制文生图_1960992729637564417.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAELoader`
- `ImageConcanate`
- `VAEDecode` ★核心
- `SeedVR2GGUF`
- `ImageConcanate`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `ControlNetApplyAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PresetTextSelector`
- `PrimitiveStringMultiline`
- `EmptySD3LatentImage`
- `AIO_Preprocessor`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `easy promptConcat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `RHHiddenNodes`
- `ShowText|pysssss`

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `383275926264952`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`VAELoader`、`ImageConcanate`、`VAEDecode`、`SeedVR2GGUF`、`ControlNetLoader`、`SetUnionControlNetType`、`ControlNetApplyAdvanced`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`UnetLoaderGGUF`、`KSampler`、`ModelSamplingAuraFlow`、`CFGNorm`、`PresetTextSelector`、`EmptySD3LatentImage`、`AIO_Preprocessor`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`easy promptConcat`、`CLIPTextEncode`、`SaveImage`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
