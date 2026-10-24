---
key: 图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json
name: qwen-image-controlnet-depth_1958718480977707010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json
hash: 33d432edd85be8ed
coverage: 0.577778
learned_at: 2026-10-23 11:42:45
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, SetNode, INTConstant, INTConstant, SetNode, SetNode, GetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, KSampler, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, SetNode, AIO_Preprocessor, ImageResizeKJv2, PreviewImage, SetNode, SetNode, ModelPatchLoader, GetNode, GetNode, SetNode, RH_Captioner, PrimitiveStringMultiline, EmptySD3LatentImage, GetNode, QwenImageDiffsynthControlnet, LoadImage, GetNode, VAEDecode, CLIPTextEncode, CR Text Concatenate, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 974171192851781, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-controlnet-depth_1958718480977707010.json`

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
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `AIO_Preprocessor`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `ModelPatchLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `RH_Captioner`
- `PrimitiveStringMultiline`
- `EmptySD3LatentImage`
- `GetNode`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `GetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `SaveImage`

## 关键参数

- `seed` = `974171192851781`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **58%**（26/45）

**有卡**：`Label (rgthree)`、`INTConstant`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`ImageResizeKJv2`、`ModelPatchLoader`、`RH_Captioner`、`EmptySD3LatentImage`、`QwenImageDiffsynthControlnet`、`LoadImage`、`VAEDecode`、`CR Text Concatenate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
