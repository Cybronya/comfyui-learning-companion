---
key: 图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json
name: Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json
hash: 678689115d8b3d9c
coverage: 0.851852
learned_at: 2026-10-23 11:16:45
nodes: [RH_LLMAPI_NODE, easy showAnything, LoraLoaderModelOnly, UNETLoader, easy promptLine, SeedVR2BlockSwap, SeedVR2, SeedVR2ExtraArgs, easy showAnything, VAEEncode, ConditioningZeroOut, KSampler, SaveImage, TextEncodeQwenImageEditPlus, CR Prompt Text, ttN seed, ProcessString, PrimitiveStringMultiline, LoadImage, Int, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, LoraLoaderModelOnly, Anything Everywhere3, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 591139342038118, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit 分镜编辑（Next Scene LoRA）_2005443551607619585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy promptLine`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `easy showAnything`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `CR Prompt Text`
- `ttN seed`
- `ProcessString`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `591139342038118`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`RH_LLMAPI_NODE`、`LoraLoaderModelOnly`、`UNETLoader`、`easy promptLine`、`SeedVR2BlockSwap`、`SeedVR2`、`SeedVR2ExtraArgs`、`VAEEncode`、`ConditioningZeroOut`、`KSampler`、`SaveImage`、`TextEncodeQwenImageEditPlus`、`CR Prompt Text`、`ttN seed`、`ProcessString`、`LoadImage`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
