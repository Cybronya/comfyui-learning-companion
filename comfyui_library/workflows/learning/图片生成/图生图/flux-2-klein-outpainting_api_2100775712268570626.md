---
key: 图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json
name: flux-2-klein-outpainting_api_2100775712268570626
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json
hash: d504f65e568b08fc
coverage: 1
learned_at: 2026-10-21 00:45:15
nodes: [VAELoader, ConditioningZeroOut, UNETLoader, CLIPLoader, VAEDecode, CLIPTextEncode, LoadImage, ReferenceLatent, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, KSampler, ImagePadForOutpaint, DrawMaskOnImage, ColorMatch, SaveImage, ImageScale]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1055829000321459, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `ImagePadForOutpaint`
- `DrawMaskOnImage`
- `ColorMatch`
- `SaveImage`
- `ImageScale`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1055829000321459`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`CLIPTextEncode`、`LoadImage`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`KSampler`、`ImagePadForOutpaint`、`DrawMaskOnImage`、`ColorMatch`、`SaveImage`、`ImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
