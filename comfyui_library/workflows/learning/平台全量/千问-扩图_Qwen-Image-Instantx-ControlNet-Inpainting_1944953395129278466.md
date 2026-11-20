---
key: 平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json
name: 千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json
hash: 8273abe225b39570
coverage: 0.944444
learned_at: 2026-11-14 01:47:24
nodes: [CLIPLoader, UNETLoader, VAEDecode, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAELoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, VAEEncode, SaveImage, PreviewImage, KSampler, ImagePadForOutpaint, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ControlNetLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 965334706953052, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json

> 来源文件 `comfyui_library/workflows/平台全量/千问-扩图_Qwen-Image-Instantx-ControlNet-Inpainting_1944953395129278466.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `VAEEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `KSampler` ★核心
- `ImagePadForOutpaint`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `965334706953052`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAELoader`、`CLIPTextEncode`、`ControlNetInpaintingAliMamaApply`、`VAEEncode`、`SaveImage`、`KSampler`、`ImagePadForOutpaint`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
