---
key: 图片生成/图生图/局部重绘！NUCHAKU-Flux Kontext Dev 局部重绘_1944413717377503233.json
name: 局部重绘！NUCHAKU-Flux Kontext Dev 局部重绘_1944413717377503233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘！NUCHAKU-Flux Kontext Dev 局部重绘_1944413717377503233.json
hash: 7e716a95985ca87e
coverage: 0.645161
learned_at: 2026-10-23 12:50:13
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, DeepTranslatorTextNode, CLIPTextEncode, KSampler, Image Comparer (rgthree), NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, NunchakuFluxLoraLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, Kontext Inpainting Conditioning, FluxGuidance, ConditioningZeroOut, JjkText, JjkText, LoadImage, SaveImage, PreviewImage, ImageStitch, Int, easy imageConcat, easy seed, VAEDecode, FluxKontextImageScale]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 784983776706841, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/局部重绘！NUCHAKU-Flux Kontext Dev 局部重绘_1944413717377503233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘！NUCHAKU-Flux Kontext Dev 局部重绘_1944413717377503233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `DeepTranslatorTextNode`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `NunchakuFluxLoraLoader` ★核心
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `Kontext Inpainting Conditioning`
- `FluxGuidance`
- `ConditioningZeroOut`
- `JjkText`
- `JjkText`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `ImageStitch`
- `Int`
- `easy imageConcat`
- `easy seed`
- `VAEDecode` ★核心
- `FluxKontextImageScale`

## 关键参数

- `seed` = `784983776706841`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **65%**（20/31）

**有卡**：`DeepTranslatorTextNode`、`CLIPTextEncode`、`KSampler`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`NunchakuFluxLoraLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatLatentBatch`、`Kontext Inpainting Conditioning`、`FluxGuidance`、`ConditioningZeroOut`、`LoadImage`、`SaveImage`、`ImageStitch`、`Int`、`easy imageConcat`、`easy seed`、`VAEDecode`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、easy seed

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
