---
key: 图片生成/图生图/多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521.json
name: 多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521.json
hash: b1439d27ccdb3e9e
coverage: 0.807692
learned_at: 2026-10-21 00:51:52
nodes: [EmptyLatentImage, TextGenerate, Fast Bypasser (rgthree), Seed (rgthree), Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, PathchSageAttentionKJ, QwenImage21Cache, ImageScaleToTotalPixels, PreviewAny, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEDecode, Fast Bypasser (rgthree), EasyCache, TextEncodeQwenImage21, Any Switch (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, ResolutionSelector, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, LoadImage, ImageConcatMulti, LoadImage, ImageConcanate, LoadImage, ImageScaleToTotalPixels, LoadImage, ComfySwitchNode, ImageScaleToTotalPixels, SaveImageAdvanced, Any Switch (rgthree), Any Switch (rgthree), Fast Groups Muter (rgthree), ComfySwitchNode, UNETLoader, CLIPLoader, ImageConcanate, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多合一图像编辑提速 Qwen image 2.1局部重绘抠图一站搞定_2104295137974251521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `EmptyLatentImage` ★核心
- `TextGenerate`
- `Fast Bypasser (rgthree)`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ImageScaleToTotalPixels`
- `PreviewAny`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `Fast Bypasser (rgthree)`
- `EasyCache`
- `TextEncodeQwenImage21`
- `Any Switch (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ComfySwitchNode`
- `ImageScaleToTotalPixels`
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageConcanate`
- `SaveImage`
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

覆盖率 **81%**（63/78）

**有卡**：`EmptyLatentImage`、`TextGenerate`、`Fast Bypasser (rgthree)`、`Seed (rgthree)`、`KSampler`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`ImageScaleToTotalPixels`、`VAEDecode`、`EasyCache`、`TextEncodeQwenImage21`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`ImageConcatMulti`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
