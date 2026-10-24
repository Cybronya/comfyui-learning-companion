---
key: 图片生成/图生图/（自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258.json
name: （自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258.json
hash: 362418298b401916
coverage: 0.958333
learned_at: 2026-10-23 13:38:05
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, GoogleTranslateTextNode, LoadImage, FluxKontextImageScale, SaveImage, VAELoader, LoadLatent, VAEDecode, SaveImage, SaveLatent, KSampler, LoraLoaderModelOnly, NunchakuFluxDiTLoader, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 790330634840166, "steps": 20}
---

# 图片生成/图生图/（自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev V1（Nunchaku） （换装前置）_1940337496180064258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `GoogleTranslateTextNode`
- `LoadImage`
- `FluxKontextImageScale`
- `SaveImage`
- `VAELoader`
- `LoadLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveLatent`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `NunchakuFluxDiTLoader`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `790330634840166`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`EmptySD3LatentImage`、`GoogleTranslateTextNode`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`LoadLatent`、`VAEDecode`、`SaveLatent`、`KSampler`、`LoraLoaderModelOnly`、`NunchakuFluxDiTLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
