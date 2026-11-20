---
key: 平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json
name: 风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json
hash: 9268611b66f9d29d
coverage: 0.603175
learned_at: 2026-11-14 02:50:47
nodes: [SamplerCustomAdvanced, BasicGuider, BasicScheduler, DisableNoise, Image Flip, GetNode, GetNode, InFluxModelSamplingPred, GetNode, GetNode, DisableNoise, BasicGuider, BasicScheduler, FlipSigmas, SamplerCustomAdvanced, SetNode, GetNode, GetNode, GetNode, FluxDeGuidance, VAEEncode, SetNode, SetNode, SetNode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, SDXLEmptyLatentSizePicker+, Note, FluxForwardODESampler, VAEDecode, PreviewImage, GetNode, SetNode, Fast Groups Bypasser (rgthree), FluxReverseODESampler, DualCLIPLoader, Anything Everywhere3, LoraLoader, VAELoader, PreviewImage, ImageScale, PreviewImage, ImageConcatMulti, SaveImage, CR Text, LoadImage, SetNode, FluxDeGuidance, CLIPTextEncode, GetNode, CR Text, RH_Captioner, ShowText|pysssss, AutoCropFaces, PreviewImage, OutFluxModelSamplingPred, UNETLoader, ApplyPulidFlux, SetNode, GetNode, CLIPTextEncode, LoadImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 0, "height": 1, "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "strength_clip": 1, "strength_model": 1, "width": "1024x1024 (1.0)"}
---

# 平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json

> 来源文件 `comfyui_library/workflows/平台全量/风格与面部转换 Style and Face Transfer with Unsampling_1851210721353756673.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `BasicScheduler`
- `DisableNoise`
- `Image Flip`
- `GetNode`
- `GetNode`
- `InFluxModelSamplingPred`
- `GetNode`
- `GetNode`
- `DisableNoise`
- `BasicGuider`
- `BasicScheduler`
- `FlipSigmas`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxDeGuidance`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `SDXLEmptyLatentSizePicker+` ★核心
- `Note`
- `FluxForwardODESampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `FluxReverseODESampler` ★核心
- `DualCLIPLoader`
- `Anything Everywhere3`
- `LoraLoader` ★核心
- `VAELoader`
- `PreviewImage`
- `ImageScale`
- `PreviewImage`
- `ImageConcatMulti`
- `SaveImage`
- `CR Text`
- `LoadImage`
- `SetNode`
- `FluxDeGuidance`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CR Text`
- `RH_Captioner`
- `ShowText|pysssss`
- `AutoCropFaces`
- `PreviewImage`
- `OutFluxModelSamplingPred`
- `UNETLoader` ★核心
- `ApplyPulidFlux`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `width` = `1024x1024 (1.0)`
- `height` = `1`
- `batch_size` = `0`
- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **60%**（38/63）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`BasicScheduler`、`DisableNoise`、`Image Flip`、`InFluxModelSamplingPred`、`FlipSigmas`、`FluxDeGuidance`、`VAEEncode`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxModelLoader`、`SDXLEmptyLatentSizePicker+`、`FluxForwardODESampler`、`VAEDecode`、`FluxReverseODESampler`、`DualCLIPLoader`、`LoraLoader`、`VAELoader`、`ImageScale`、`ImageConcatMulti`、`SaveImage`、`CR Text`、`LoadImage`、`CLIPTextEncode`、`RH_Captioner`、`AutoCropFaces`、`OutFluxModelSamplingPred`、`UNETLoader`、`ApplyPulidFlux`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxDeGuidance、FluxForwardODESampler、FluxReverseODESampler
