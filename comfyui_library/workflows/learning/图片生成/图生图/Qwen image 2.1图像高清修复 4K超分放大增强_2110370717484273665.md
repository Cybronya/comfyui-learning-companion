---
key: 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json
name: Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json
hash: 434a03f58057e7bf
coverage: 0.826087
learned_at: 2026-10-23 11:14:01
nodes: [CLIPLoader, VAELoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, LoadImage, Latent Switch (JPS), UNETLoader, TextEncodeQwenImage21, EmptyLatentImage, SaveImage, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Comparer (rgthree), CR Text, Fast Groups Bypasser (rgthree), easy imageSize, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, PreviewImage, ImageResize+, ImageScaleBy, SeedVR2LoadDiTModel, ImageResize+, PreviewImage, easy imageSize, easy imageSize, ImageScaleBy, TTP_Image_Assy, Image Comparer (rgthree), GetNode, TTP_Tile_image_size, SaveImage, VAEDecode, SetNode, ImageResizeKJv2, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像高清修复 4K超分放大增强_2110370717484273665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `Latent Switch (JPS)`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `ImageResize+`
- `PreviewImage`
- `easy imageSize`
- `easy imageSize`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `GetNode`
- `TTP_Tile_image_size`
- `SaveImage`
- `VAEDecode` ★核心
- `SetNode`
- `ImageResizeKJv2`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **83%**（57/69）

**有卡**：`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`Latent Switch (JPS)`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`LoraLoaderModelOnly`、`CR Text`、`easy imageSize`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`SeedVR2VideoUpscaler`、`ImageResize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`VAEDecode`、`ImageResizeKJv2`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
