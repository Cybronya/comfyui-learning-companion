---
key: 图片生成/文生图/图文生图全都要｜全能G2-Images 2.0合集版_2096601839860015106.json
name: 图文生图全都要｜全能G2-Images 2.0合集版_2096601839860015106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图文生图全都要｜全能G2-Images 2.0合集版_2096601839860015106.json
hash: 398049100b2b1023
coverage: 0.859375
learned_at: 2026-10-20 01:20:07
nodes: [Fast Groups Bypasser (rgthree), RH_RhartImageG2OfficialImageToImage, SaveImage, Image Comparer (rgthree), RHHiddenNodes, SaveImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SeedVR2ExtraArgs, SeedVR2, ImageScaleToTotalPixels, Image Comparer (rgthree), SaveImage, SeedVR2BlockSwap, DF_Integer, PrimitiveNode, PrimitiveNode, RH_RhartImageG2TextToImage, SaveImage, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/图文生图全都要｜全能G2-Images 2.0合集版_2096601839860015106.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图文生图全都要｜全能G2-Images 2.0合集版_2096601839860015106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `Fast Groups Bypasser (rgthree)`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RHHiddenNodes`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2BlockSwap`
- `DF_Integer`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
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

覆盖率 **86%**（55/64）

**有卡**：`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RHHiddenNodes`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SeedVR2ExtraArgs`、`SeedVR2`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`DF_Integer`、`RH_RhartImageG2TextToImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
