---
key: 图片生成/图生图/KontextNunchakuDevLora一键转手办_1949798748291555330.json
name: KontextNunchakuDevLora一键转手办_1949798748291555330
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora一键转手办_1949798748291555330.json
hash: 5bcc0a9dff732cbb
coverage: 0.95
learned_at: 2026-10-23 11:06:32
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, NunchakuFluxDiTLoader, ModelSamplingFlux, KSampler, EmptyLatentImage, VAELoader, ImageStitch, PreviewImage, LoadImage, FluxKontextImageScale, VAEEncode, LoadImage, LoraLoaderModelOnly, RH_Translator]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 945486913256276, "steps": 20, "width": 1024}
---

# 图片生成/图生图/KontextNunchakuDevLora一键转手办_1949798748291555330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora一键转手办_1949798748291555330.json`

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
- `ModelSamplingFlux`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ImageStitch`
- `PreviewImage`
- `LoadImage`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `945486913256276`
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

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`KSampler`、`EmptyLatentImage`、`VAELoader`、`ImageStitch`、`LoadImage`、`FluxKontextImageScale`、`VAEEncode`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
