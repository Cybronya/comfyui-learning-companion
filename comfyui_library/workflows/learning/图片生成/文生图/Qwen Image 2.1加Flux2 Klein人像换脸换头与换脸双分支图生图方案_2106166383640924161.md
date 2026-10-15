---
key: 图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json
name: Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json
hash: ce2f6b3ccdb12bc5
coverage: 0.863636
learned_at: 2026-10-10 20:58:52
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, LoadImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, SaveImage, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1加Flux2 Klein人像换脸换头与换脸双分支图生图方案_2106166383640924161.json`

## 结构

**节点**（66 个）：
- `ComfySwitchNode`
- `VAEDecode`
- `KSampler`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`
- `CLIPTextEncode`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode`
- `KSampler`
- `VAEDecode`
- `EmptyFlux2LatentImage`
- `UNETLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAEEncode`
- `LoraLoaderModelOnly`
- `LoadImage`
- `CLIPTextEncode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **86%**（57/66）

**有卡**：`ComfySwitchNode`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`JjkText`、`LoadImage`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SaveImage`、`Image Comparer (rgthree)`、`Fast Groups Bypasser (rgthree)`、`孤海注释`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
