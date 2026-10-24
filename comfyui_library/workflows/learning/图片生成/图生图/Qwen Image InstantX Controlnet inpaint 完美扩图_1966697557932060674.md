---
key: 图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json
name: Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json
hash: f59725225b1e4795
coverage: 0.84
learned_at: 2026-10-23 11:13:22
nodes: [ModelSamplingAuraFlow, CLIPTextEncode, KSampler, VAEEncode, ControlNetLoader, CLIPTextEncode, PreviewImage, SaveImage, LayerUtility: LoadJoyCaptionBeta1Model, CLIPLoader, VAELoader, LoraLoaderModelOnly, ImageAndMaskPreview, VAEDecode, ImageConcanate, ControlNetInpaintingAliMamaApply, Image Comparer (rgthree), SaveImage, LayerUtility: JoyCaptionBeta1, ShowText|pysssss, UNETLoader, LoadImage, ImageScaleToTotalPixels, ImagePadForOutpaint, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 833426667642685, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet inpaint 完美扩图_1966697557932060674.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageAndMaskPreview`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ControlNetInpaintingAliMamaApply`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImagePadForOutpaint`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `833426667642685`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`KSampler`、`VAEEncode`、`ControlNetLoader`、`SaveImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`ImageAndMaskPreview`、`VAEDecode`、`ImageConcanate`、`ControlNetInpaintingAliMamaApply`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
