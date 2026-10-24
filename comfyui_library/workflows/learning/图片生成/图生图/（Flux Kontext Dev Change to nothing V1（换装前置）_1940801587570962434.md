---
key: 图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json
name: （Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json
hash: 549a65116137807c
coverage: 0.928571
learned_at: 2026-10-23 13:37:14
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, MagCache, EmptySD3LatentImage, GoogleTranslateTextNode, UnetLoaderGGUF, SaveLatent, SaveImage, CR Prompt Text, LoraLoaderModelOnly, KSampler, LoadImage, LoadLatent, VAELoader, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 205156513641490, "steps": 20}
---

# 图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（Flux Kontext Dev Change to nothing V1（换装前置）_1940801587570962434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `MagCache`
- `EmptySD3LatentImage`
- `GoogleTranslateTextNode`
- `UnetLoaderGGUF` ★核心
- `SaveLatent`
- `SaveImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadLatent`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `205156513641490`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`MagCache`、`EmptySD3LatentImage`、`GoogleTranslateTextNode`、`UnetLoaderGGUF`、`SaveLatent`、`SaveImage`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`LoadLatent`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
