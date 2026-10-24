---
key: 图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json
name: Flux Kontext SingalImage_单图修改_Borges_1951605887653851137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json
hash: 705bd147b284af4a
coverage: 0.944444
learned_at: 2026-10-23 10:57:25
nodes: [VAEEncode, DualCLIPLoader, UNETLoader, ModelSamplingFlux, ReferenceLatent, FluxGuidance, CLIPTextEncode, VAELoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, VAEDecode, SaveImage, FluxResolutionNode, EmptyLatentImage, GoogleTranslateTextNode, Note Plus (mtb), LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 134364300225039, "steps": 20, "width": 1024}
---

# 图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext SingalImage_单图修改_Borges_1951605887653851137.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAEEncode` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingFlux`
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `FluxResolutionNode`
- `EmptyLatentImage` ★核心
- `GoogleTranslateTextNode`
- `Note Plus (mtb)`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `134364300225039`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAEEncode`、`DualCLIPLoader`、`UNETLoader`、`ModelSamplingFlux`、`ReferenceLatent`、`FluxGuidance`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`SaveImage`、`FluxResolutionNode`、`EmptyLatentImage`、`GoogleTranslateTextNode`、`Note Plus (mtb)`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
