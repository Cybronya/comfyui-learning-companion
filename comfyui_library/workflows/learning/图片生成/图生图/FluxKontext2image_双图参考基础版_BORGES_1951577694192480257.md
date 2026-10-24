---
key: 图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json
name: FluxKontext2image_双图参考基础版_BORGES_1951577694192480257
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json
hash: 752f63319644fd52
coverage: 0.944444
learned_at: 2026-10-23 11:01:40
nodes: [VAELoader, DualCLIPLoader, ConditioningZeroOut, VAEDecode, FluxGuidance, UNETLoader, CLIPTextEncode, KSampler, EmptyLatentImage, ReferenceLatent, VAEEncode, FluxKontextImageScale, ImageStitch, PreviewImage, LoadImage, Note Plus (mtb), SaveImage, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 13271475756762, "steps": 20, "width": 1024}
---

# 图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FluxKontext2image_双图参考基础版_BORGES_1951577694192480257.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `ImageStitch`
- `PreviewImage`
- `LoadImage`
- `Note Plus (mtb)`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `13271475756762`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`、`ReferenceLatent`、`VAEEncode`、`FluxKontextImageScale`、`ImageStitch`、`LoadImage`、`Note Plus (mtb)`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
