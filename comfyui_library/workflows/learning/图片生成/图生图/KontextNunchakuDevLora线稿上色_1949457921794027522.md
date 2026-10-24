---
key: 图片生成/图生图/KontextNunchakuDevLora线稿上色_1949457921794027522.json
name: KontextNunchakuDevLora线稿上色_1949457921794027522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora线稿上色_1949457921794027522.json
hash: 5b39a233ff70f4fd
coverage: 0.95
learned_at: 2026-10-23 11:06:41
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, NunchakuFluxDiTLoader, VAEEncode, ModelSamplingFlux, KSampler, EmptyLatentImage, VAELoader, FluxKontextImageScale, ImageStitch, PreviewImage, LoadImage, LoraLoaderModelOnly, RH_Translator, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 289478250373906, "steps": 20, "width": 1024}
---

# 图片生成/图生图/KontextNunchakuDevLora线稿上色_1949457921794027522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora线稿上色_1949457921794027522.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `NunchakuFluxDiTLoader`
- `VAEEncode` ★核心
- `ModelSamplingFlux`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `FluxKontextImageScale`
- `ImageStitch`
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `289478250373906`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`NunchakuFluxDiTLoader`、`VAEEncode`、`ModelSamplingFlux`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`FluxKontextImageScale`、`ImageStitch`、`LoadImage`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
