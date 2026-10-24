---
key: 图片生成/图生图/KontextNunchakuDevLoraFelt风格_1946468864593158145.json
name: KontextNunchakuDevLoraFelt风格_1946468864593158145
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLoraFelt风格_1946468864593158145.json
hash: bce9030abba75785
coverage: 1
learned_at: 2026-10-23 11:06:30
nodes: [DualCLIPLoader, VAEDecode, SaveImage, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, VAELoader, NunchakuFluxDiTLoader, VAEEncode, ModelSamplingFlux, KSampler, EmptyLatentImage, LoadImage, FluxGuidance, LoraLoaderModelOnly, RH_Translator]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 541022892424771, "steps": 20, "width": 1024}
---

# 图片生成/图生图/KontextNunchakuDevLoraFelt风格_1946468864593158145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLoraFelt风格_1946468864593158145.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `VAELoader`
- `NunchakuFluxDiTLoader`
- `VAEEncode` ★核心
- `ModelSamplingFlux`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `541022892424771`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAELoader`、`NunchakuFluxDiTLoader`、`VAEEncode`、`ModelSamplingFlux`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`FluxGuidance`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
