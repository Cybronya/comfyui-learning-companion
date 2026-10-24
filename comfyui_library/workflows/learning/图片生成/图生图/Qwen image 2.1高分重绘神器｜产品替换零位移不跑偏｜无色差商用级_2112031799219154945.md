---
key: 图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json
name: Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json
hash: d95b377419e9785a
coverage: 0.835616
learned_at: 2026-10-23 11:14:12
nodes: [ImageScaleToTotalPixels, MaskFillHoles, SimpleMath+, InpaintCropImproved, DrawMaskOnImage, GetNode, VAEEncode, Seed (rgthree), SetLatentNoiseMask, TextEncodeQwenImage21, KSampler, VAEDecode, InpaintStitchImproved, SaveImage, INTConstant, Image Comparer (rgthree), CLIPLoader, Anything Everywhere, Anything Everywhere, UNETLoader, VAELoader, Anything Everywhere, ComfySwitchNode, LoadImage, LoadImage, QwenImage21Cache, PrimitiveStringMultiline, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `ImageScaleToTotalPixels`
- `MaskFillHoles`
- `SimpleMath+`
- `InpaintCropImproved`
- `DrawMaskOnImage`
- `GetNode`
- `VAEEncode` ★核心
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `SaveImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `UNETLoader` ★核心
- `VAELoader`
- `Anything Everywhere`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
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

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（61/73）

**有卡**：`ImageScaleToTotalPixels`、`MaskFillHoles`、`SimpleMath+`、`InpaintCropImproved`、`DrawMaskOnImage`、`VAEEncode`、`Seed (rgthree)`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`InpaintStitchImproved`、`SaveImage`、`INTConstant`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`QwenImage21Cache`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
