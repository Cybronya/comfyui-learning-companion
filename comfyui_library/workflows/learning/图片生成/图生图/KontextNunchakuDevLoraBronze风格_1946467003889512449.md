---
key: 图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json
name: KontextNunchakuDevLoraBronze风格_1946467003889512449
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json
hash: 49d68acf03b26982
coverage: 1
learned_at: 2026-10-23 11:06:29
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, VAELoader, NunchakuFluxDiTLoader, VAEEncode, ModelSamplingFlux, KSampler, EmptyLatentImage, LoraLoaderModelOnly, RH_Translator, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 109484508694928, "steps": 20, "width": 1024}
---

# 图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLoraBronze风格_1946467003889512449.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
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
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `109484508694928`
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

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAELoader`、`NunchakuFluxDiTLoader`、`VAEEncode`、`ModelSamplingFlux`、`KSampler`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`RH_Translator`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
