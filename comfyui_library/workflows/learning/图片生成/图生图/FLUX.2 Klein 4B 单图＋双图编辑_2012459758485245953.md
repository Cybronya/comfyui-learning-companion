---
key: 图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json
name: FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json
hash: e1dd29c963c7fbe1
coverage: 0.933333
learned_at: 2026-10-23 10:54:04
nodes: [CLIPLoader, Image Comparer (rgthree), LoadImage, UNETLoader, FluxGuidance, VAELoader, ConditioningZeroOut, ReferenceLatent, InvertMask, VAEEncode, AutoImageResize, KSampler, VAEDecode, MaskToImage, Cut By Mask, Get resolution [Crystools], SaveImage, ImageScale, CLIPTextEncode, VAEDecode, AutoImageResize, InvertMask, MaskToImage, ReferenceLatent, Get resolution [Crystools], ImageScale, Cut By Mask, KSampler, UNETLoader, CLIPLoader, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, FluxGuidance, SaveImage, LoadImage, LoadImage, ConditioningZeroOut, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 975481589195195, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 4B 单图＋双图编辑_2012459758485245953.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `FluxGuidance`
- `VAELoader`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `InvertMask`
- `VAEEncode` ★核心
- `AutoImageResize`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MaskToImage`
- `Cut By Mask`
- `Get resolution [Crystools]`
- `SaveImage`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `AutoImageResize`
- `InvertMask`
- `MaskToImage`
- `ReferenceLatent`
- `Get resolution [Crystools]`
- `ImageScale`
- `Cut By Mask`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `975481589195195`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`CLIPLoader`、`LoadImage`、`UNETLoader`、`FluxGuidance`、`VAELoader`、`ConditioningZeroOut`、`ReferenceLatent`、`InvertMask`、`VAEEncode`、`AutoImageResize`、`KSampler`、`VAEDecode`、`MaskToImage`、`Cut By Mask`、`Get resolution [Crystools]`、`SaveImage`、`ImageScale`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
