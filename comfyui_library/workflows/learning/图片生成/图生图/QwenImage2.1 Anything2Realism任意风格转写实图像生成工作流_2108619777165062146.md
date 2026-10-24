---
key: 图片生成/图生图/QwenImage2.1 Anything2Realism任意风格转写实图像生成工作流_2108619777165062146.json
name: QwenImage2.1 Anything2Realism任意风格转写实图像生成工作流_2108619777165062146
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1 Anything2Realism任意风格转写实图像生成工作流_2108619777165062146.json
hash: 50d52514c556260f
coverage: 0.714286
learned_at: 2026-10-23 11:20:41
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ResolutionSelector, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, VAEDecode, KSampler, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, PrimitiveFloat, easy clearCacheAll, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, TextEncodeQwenImage21, EmptyLatentImage, QwenImage21Cache, KSampler, GetNode, PreviewImage, PreviewImage, Any Switch (rgthree), VAEDecode, RH_DLSS5Enhance, SaveImage, UNETLoader, CLIPLoader, VAELoader, Load Image From Url (mtb), LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenImage2.1 Anything2Realism任意风格转写实图像生成工作流_2108619777165062146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1 Anything2Realism任意风格转写实图像生成工作流_2108619777165062146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **71%**（50/70）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`easy clearCacheAll`、`ComfyMathExpression`、`RH_DLSS5Enhance`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Load Image From Url (mtb)`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
