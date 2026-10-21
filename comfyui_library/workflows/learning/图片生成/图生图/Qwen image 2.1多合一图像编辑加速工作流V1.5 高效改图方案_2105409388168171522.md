---
key: 图片生成/图生图/Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522.json
name: Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522.json
hash: f309abdaff3516c4
coverage: 0.759036
learned_at: 2026-10-21 00:42:59
nodes: [EmptyLatentImage, Seed (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageConcanate, Any Switch (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, LoadImage, ImageConcatMulti, LoadImage, ImageConcanate, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, UNETLoader, SaveImageAdvanced, Any Switch (rgthree), Any Switch (rgthree), ComfySwitchNode, Fast Bypasser (rgthree), CLIPLoader, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), PreviewAny, TextEncodeQwenImage21, TextGenerate, KSampler, PrimitiveInt, ComfySwitchNode, PrimitiveInt, LoraLoaderModelOnly, ComfySwitchNode, Reroute, VAEDecode, SaveImage, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, ComfySwitchNode, PathchSageAttentionKJ, QwenImage21Cache, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多合一图像编辑加速工作流V1.5 高效改图方案_2105409388168171522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `Any Switch (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
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
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `ComfySwitchNode`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `KSampler` ★核心
- `PrimitiveInt`
- `ComfySwitchNode`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `Reroute`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `ComfySwitchNode`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
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

覆盖率 **76%**（63/83）

**有卡**：`EmptyLatentImage`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`ImageConcanate`、`VAELoader`、`CLIPLoader`、`ImageConcatMulti`、`LoadImage`、`UNETLoader`、`SaveImageAdvanced`、`Fast Bypasser (rgthree)`、`TextEncodeQwenImage21`、`TextGenerate`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`PrimitiveBoolean`、`ResolutionSelector`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
