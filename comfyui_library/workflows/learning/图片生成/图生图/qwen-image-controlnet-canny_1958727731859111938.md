---
key: 图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json
name: qwen-image-controlnet-canny_1958727731859111938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json
hash: 17ab5c79015d3aca
coverage: 0.577778
learned_at: 2026-10-23 11:42:44
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, SetNode, PreviewImage, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, EmptySD3LatentImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, KSampler, RH_Captioner, PrimitiveStringMultiline, CR Text Concatenate, SaveImage, QwenImageDiffsynthControlnet, LoadImage, AIO_Preprocessor, ModelPatchLoader, GetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 641991028963879, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-controlnet-canny_1958727731859111938.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `RH_Captioner`
- `PrimitiveStringMultiline`
- `CR Text Concatenate`
- `SaveImage`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `GetNode`

## 关键参数

- `seed` = `641991028963879`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **58%**（26/45）

**有卡**：`Label (rgthree)`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`CLIPTextEncode`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`RH_Captioner`、`CR Text Concatenate`、`SaveImage`、`QwenImageDiffsynthControlnet`、`LoadImage`、`AIO_Preprocessor`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
