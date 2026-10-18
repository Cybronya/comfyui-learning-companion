---
key: 视频生成/图生视频/Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218.json
name: Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218.json
hash: c7dae377a0033b54
coverage: 0.897638
learned_at: 2026-10-17 22:18:56
nodes: [SaveImageAdvanced, ResolutionSelector, SaveImageAdvanced, LoadImage, LoadImage, SaveImageAdvanced, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy cleanGpuUsed, easy showAnything, TextEncodeQwenImage21, UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, easy cleanGpuUsed, LoadImage, ImageResizeKJv2, CLIPLoader, ResolutionSelector, easy showAnything, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, easy cleanGpuUsed, CLIPLoader, easy showAnything, LoadImage, ImageResizeKJv2, UNETLoader, VAELoader, EmptyLatentImage, KSampler, QwenImage21Cache, VAEDecode, SaveImageAdvanced, PreviewImage, CLIPLoader, easy showAnything, TextEncodeQwenImage21, easy cleanGpuUsed, ImageStitch, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, MuyeTextEditOutput, TextGenerate, CR Prompt Text, MuyeTextEditOutput, PrimitiveStringMultiline, MuyeTextEditOutput, TextGenerate, TextGenerate, CR Prompt Text, MuyeTextEditOutput, TextGenerate, BatchImagesNode, Fast Groups Bypasser (rgthree), ResolutionSelector, CLIPLoader, SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（127 个）：
- `SaveImageAdvanced`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `easy cleanGpuUsed`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPLoader`
- `ResolutionSelector`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `easy showAnything`
- `LoadImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `PreviewImage`
- `CLIPLoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `ImageStitch`
- `TTResolutionSelector`
- `CR Prompt Text`
- `CLIPLoader`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `MuyeTextEditOutput`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `PrimitiveStringMultiline`
- `MuyeTextEditOutput`
- `TextGenerate`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `TextGenerate`
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **90%**（114/127）

**有卡**：`SaveImageAdvanced`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`ImageStitch`、`TTResolutionSelector`、`CR Prompt Text`、`MuyeTextEditOutput`、`TextGenerate`、`BatchImagesNode`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
