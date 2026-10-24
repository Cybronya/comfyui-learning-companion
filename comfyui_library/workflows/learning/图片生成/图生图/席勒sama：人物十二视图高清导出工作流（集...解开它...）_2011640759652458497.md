---
key: 图片生成/图生图/席勒sama：人物十二视图高清导出工作流（集...解开它...）_2011640759652458497.json
name: 席勒sama：人物十二视图高清导出工作流（集...解开它...）_2011640759652458497
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/席勒sama：人物十二视图高清导出工作流（集...解开它...）_2011640759652458497.json
hash: 8e273bc8af763ee6
coverage: 0.965517
learned_at: 2026-10-23 12:50:41
nodes: [CFGNorm, VAEEncode, ImageScaleToTotalPixels, ModelSamplingAuraFlow, TextEncodeQwenImageEdit, KSampler, SaveImage, VAEDecode, easy forLoopStart, SimpleMath+, Text Load Line From File, easy batchAnything, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoadImage, RHHiddenNodes, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2ExtraArgs, SeedVR2, easy cleanGpuUsed, SeedVR2BlockSwap, easy forLoopEnd, SaveImage, PreviewImage, ImageScaleToTotalPixels]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 341086850883834, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/席勒sama：人物十二视图高清导出工作流（集...解开它...）_2011640759652458497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/席勒sama：人物十二视图高清导出工作流（集...解开它...）_2011640759652458497.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CFGNorm`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy forLoopStart`
- `SimpleMath+`
- `Text Load Line From File`
- `easy batchAnything`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RHHiddenNodes`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `easy cleanGpuUsed`
- `SeedVR2BlockSwap`
- `easy forLoopEnd`
- `SaveImage`
- `PreviewImage`
- `ImageScaleToTotalPixels`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `341086850883834`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`CFGNorm`、`VAEEncode`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEdit`、`KSampler`、`SaveImage`、`VAEDecode`、`easy forLoopStart`、`SimpleMath+`、`Text Load Line From File`、`easy batchAnything`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`RHHiddenNodes`、`UNETLoader`、`SeedVR2ExtraArgs`、`SeedVR2`、`easy cleanGpuUsed`、`SeedVR2BlockSwap`、`easy forLoopEnd`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
