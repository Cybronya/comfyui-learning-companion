---
key: 图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json
name: QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json
hash: 65f4b8c7ace0c3c7
coverage: 0.609756
learned_at: 2026-10-21 00:43:51
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ResolutionSelector, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, VAEDecode, KSampler, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, PrimitiveFloat, easy clearCacheAll, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, TextEncodeQwenImage21, EmptyLatentImage, QwenImage21Cache, KSampler, GetNode, PreviewImage, PreviewImage, Any Switch (rgthree), VAEDecode, RH_DLSS5Enhance, SaveImage, UNETLoader, CLIPLoader, VAELoader, Load Image From Url (mtb), LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 42, "steps": 25, "width": 1024}
---

# 图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `easy clearCacheAll`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `RH_DLSS5Enhance`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Load Image From Url (mtb)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **61%**（25/41）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`easy clearCacheAll`、`ComfyMathExpression`、`RH_DLSS5Enhance`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Load Image From Url (mtb)`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
