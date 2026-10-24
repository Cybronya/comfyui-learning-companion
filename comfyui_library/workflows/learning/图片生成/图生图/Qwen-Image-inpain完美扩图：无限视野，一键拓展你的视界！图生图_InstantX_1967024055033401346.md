---
key: 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json
name: Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json
hash: 59d11d50fce5b35a
coverage: 0.935484
learned_at: 2026-10-23 11:17:19
nodes: [VAELoader, VAEEncode, VAEDecode, ImageAndMaskPreview, ImageConcanate, LayerUtility: ImageBlend V2, GrowMaskWithBlur, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, ImageScaleToTotalPixels, SaveImage, Image Comparer (rgthree), SaveImage, PreviewImage, UNETLoader, InpaintPreprocessor, ControlNetInpaintingAliMamaApply, KSampler, SetLatentNoiseMask, easy cleanGpuUsed, ModelSamplingAuraFlow, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, CR Text, CR Text, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LayerUtility: JoyCaptionBeta1, ImagePadForOutpaint]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 79162106956265, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-inpain完美扩图：无限视野，一键拓展你的视界！图生图_InstantX_1967024055033401346.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageAndMaskPreview`
- `ImageConcanate`
- `LayerUtility: ImageBlend V2`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `InpaintPreprocessor`
- `ControlNetInpaintingAliMamaApply`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `CR Text`
- `CR Text`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LayerUtility: JoyCaptionBeta1`
- `ImagePadForOutpaint`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `79162106956265`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`VAELoader`、`VAEEncode`、`VAEDecode`、`ImageAndMaskPreview`、`ImageConcanate`、`LayerUtility: ImageBlend V2`、`GrowMaskWithBlur`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`SaveImage`、`UNETLoader`、`InpaintPreprocessor`、`ControlNetInpaintingAliMamaApply`、`KSampler`、`SetLatentNoiseMask`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`ControlNetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CR Text`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`、`LayerUtility: JoyCaptionBeta1`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
