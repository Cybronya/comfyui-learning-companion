---
key: 平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json
name: FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json
hash: 4c68be7314ec727c
coverage: 0.925926
learned_at: 2026-11-14 00:24:36
nodes: [PulidFluxEvaClipLoader, KSamplerSelect, BasicGuider, RandomNoise, SamplerCustomAdvanced, EmptyLatentImage, StyleModelApply, CLIPVisionEncode, CLIPTextEncode, VAEDecode, SaveImage, Image Comparer (rgthree), BasicScheduler, LoadImage, ApplyPulidFlux, LoadImage, VAELoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, StyleModelLoader, DualCLIPLoader, UnetLoaderGGUF, ImageScaleToTotalPixels, Note, CLIPVisionLoader, GetImageSizeAndCount, FluxGuidance]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 768}
---

# 平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX Redux + PULid Image to Image Face Swap Consis_1863417703032664066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `PulidFluxEvaClipLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `BasicScheduler`
- `LoadImage`
- `ApplyPulidFlux`
- `LoadImage`
- `VAELoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `StyleModelLoader`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `FluxGuidance`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`PulidFluxEvaClipLoader`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`StyleModelApply`、`CLIPVisionEncode`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`BasicScheduler`、`LoadImage`、`ApplyPulidFlux`、`VAELoader`、`PulidFluxInsightFaceLoader`、`PulidFluxModelLoader`、`StyleModelLoader`、`DualCLIPLoader`、`UnetLoaderGGUF`、`ImageScaleToTotalPixels`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`FluxGuidance`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
