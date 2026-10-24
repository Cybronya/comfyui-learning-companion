---
key: 图片生成/图生图/KontextNunchakuDevInpaintingRedux换装_1945000724100210689.json
name: KontextNunchakuDevInpaintingRedux换装_1945000724100210689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevInpaintingRedux换装_1945000724100210689.json
hash: 7d72fd2d202b5ff8
coverage: 1
learned_at: 2026-10-23 11:06:28
nodes: [DualCLIPLoader, VAEDecode, SaveImage, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, NunchakuFluxDiTLoader, ModelSamplingFlux, KSampler, LoraLoaderModelOnly, FluxKontextImageScale, VAEEncode, VAELoader, LoadImage, RH_Translator, ImageStitch, StyleModelLoader, Kontext Inpainting Conditioning, FluxGuidance, easy imageRemBg, LoadImage, CLIPVisionLoader, ReduxAdvanced, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 654336784689558, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDevInpaintingRedux换装_1945000724100210689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevInpaintingRedux换装_1945000724100210689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `NunchakuFluxDiTLoader`
- `ModelSamplingFlux`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `VAELoader`
- `LoadImage`
- `RH_Translator`
- `ImageStitch`
- `StyleModelLoader`
- `Kontext Inpainting Conditioning`
- `FluxGuidance`
- `easy imageRemBg`
- `LoadImage`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `654336784689558`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`KSampler`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`VAEEncode`、`VAELoader`、`LoadImage`、`RH_Translator`、`ImageStitch`、`StyleModelLoader`、`Kontext Inpainting Conditioning`、`FluxGuidance`、`easy imageRemBg`、`CLIPVisionLoader`、`ReduxAdvanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
