---
key: 图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json
name: Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json
hash: a537d1da91a1931d
coverage: 0.865385
learned_at: 2026-10-23 11:06:57
nodes: [ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, DualCLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, FluxGuidance, ConditioningZeroOut, KSampler, PreviewImage, LoadImage, FastCanvasTool, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, DeepTranslatorTextNode, UNETLoader, CLIPTextEncode, VAEEncode, LoraLoaderModelOnly, VAELoader, RandomNoise, SplitSigmas, SamplerCustomAdvanced, DisableNoise, SamplerCustomAdvanced, ModelSamplingSD3, KSamplerSelect, CLIPTextEncode, Image Comparer (rgthree), RH_Captioner, WanVideoNAG, CFGGuider, CLIPLoader, VAEDecode, SaveImage, BasicScheduler, ImageConcatMulti, LoadImage, Image Comparer (rgthree), VAEDecode, ReferenceLatent, PreviewImage, FastCanvas, FluxKontextImageScale, PreviewImage, Image Comparer (rgthree), easy cleanGpuUsed, ImageConcanate, easy cleanGpuUsed, SeedVR2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 477646688424748, "steps": 20}
---

# 图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext万物融图+Wan2.2洗图（手动编辑）_1955827510690942977.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `ShowText|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PreviewImage`
- `LoadImage`
- `FastCanvasTool`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `DeepTranslatorTextNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `RandomNoise`
- `SplitSigmas`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `RH_Captioner`
- `WanVideoNAG`
- `CFGGuider`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `BasicScheduler`
- `ImageConcatMulti`
- `LoadImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `PreviewImage`
- `FastCanvas`
- `FluxKontextImageScale`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `SeedVR2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `477646688424748`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEEncode`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`LoadImage`、`FastCanvasTool`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`DeepTranslatorTextNode`、`RandomNoise`、`SplitSigmas`、`SamplerCustomAdvanced`、`DisableNoise`、`ModelSamplingSD3`、`KSamplerSelect`、`RH_Captioner`、`WanVideoNAG`、`CFGGuider`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`BasicScheduler`、`ImageConcatMulti`、`ReferenceLatent`、`FastCanvas`、`FluxKontextImageScale`、`easy cleanGpuUsed`、`ImageConcanate`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
