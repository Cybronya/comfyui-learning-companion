---
key: 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json
name: Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json
hash: 00a208132add6ba9
coverage: 0.763636
learned_at: 2026-10-10 20:58:57
nodes: [TextGenerate, RegexExtract, Seed (rgthree), UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, SaveImage, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, PreviewImage, VAEDecode, SaveImage, PrimitiveStringMultiline, EmptyLatentImage, PreviewAny, ResolutionSelector, StringConcatenate, TextEncodeQwenImage21, Any Switch (rgthree), PrimitiveStringMultiline, PreviewImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json`

## 结构

**节点**（55 个）：
- `TextGenerate`
- `RegexExtract`
- `Seed (rgthree)`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage`
- `PreviewAny`
- `ResolutionSelector`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `Any Switch (rgthree)`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
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

**识别到的模式**：text_to_image

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

覆盖率 **76%**（42/55）

**有卡**：`TextGenerate`、`RegexExtract`、`Seed (rgthree)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`PreviewImage`、`VAEDecode`、`PrimitiveStringMultiline`、`EmptyLatentImage`、`PreviewAny`、`ResolutionSelector`、`StringConcatenate`、`TextEncodeQwenImage21`、`Any Switch (rgthree)`、`Image Comparer (rgthree)`、`Fast Groups Bypasser (rgthree)`、`KSampler`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（1）：`Seed (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
