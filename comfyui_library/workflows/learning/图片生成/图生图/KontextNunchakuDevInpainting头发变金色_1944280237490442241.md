---
key: 图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json
name: KontextNunchakuDevInpainting头发变金色_1944280237490442241
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json
hash: 865fd5dee4dcaf57
coverage: 1
learned_at: 2026-10-23 11:06:29
nodes: [DualCLIPLoader, VAEDecode, SaveImage, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, NunchakuFluxDiTLoader, ModelSamplingFlux, EmptyLatentImage, KSampler, FluxGuidance, LoadImage, RH_Translator, LoraLoaderModelOnly, Kontext Inpainting Conditioning, FluxKontextImageScale, VAELoader, VAEEncode]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 403520508394345, "steps": 20, "width": 1024}
---

# 图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `NunchakuFluxDiTLoader`
- `ModelSamplingFlux`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `LoadImage`
- `RH_Translator`
- `LoraLoaderModelOnly` ★核心
- `Kontext Inpainting Conditioning`
- `FluxKontextImageScale`
- `VAELoader`
- `VAEEncode` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `403520508394345`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`EmptyLatentImage`、`KSampler`、`FluxGuidance`、`LoadImage`、`RH_Translator`、`LoraLoaderModelOnly`、`Kontext Inpainting Conditioning`、`FluxKontextImageScale`、`VAELoader`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
