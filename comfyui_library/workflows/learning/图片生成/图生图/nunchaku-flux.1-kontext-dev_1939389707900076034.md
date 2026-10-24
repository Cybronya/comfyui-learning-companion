---
key: 图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json
name: nunchaku-flux.1-kontext-dev_1939389707900076034
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json
hash: 6f861f18add0b7eb
coverage: 0.857143
learned_at: 2026-10-23 11:41:19
nodes: [VAELoader, DualCLIPLoader, ConditioningZeroOut, PreviewImage, SaveImage, VAEDecode, VAEEncode, FluxKontextImageScale, FluxGuidance, ReferenceLatent, MarkdownNote, NunchakuFluxDiTLoader, KSampler, EmptySD3LatentImage, LoadImageOutput, ImageStitch, LoadImageOutput, LoadImage, CLIPTextEncode, MarkdownNote, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 650502565023642, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `FluxGuidance`
- `ReferenceLatent`
- `MarkdownNote`
- `NunchakuFluxDiTLoader`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `LoadImageOutput`
- `ImageStitch`
- `LoadImageOutput`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `650502565023642`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`NunchakuFluxDiTLoader`、`KSampler`、`EmptySD3LatentImage`、`LoadImageOutput`、`ImageStitch`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
