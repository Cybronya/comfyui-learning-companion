---
key: 图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json
name: （自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json
hash: 0b7c412a5119492d
coverage: 0.928571
learned_at: 2026-10-23 13:38:05
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, MagCache, EmptySD3LatentImage, GoogleTranslateTextNode, VAEDecode, SaveImage, UnetLoaderGGUF, SaveLatent, SaveImage, LoadImage, CR Prompt Text, LoraLoaderModelOnly, VAELoader, KSampler, LoadLatent]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 205156513641490, "steps": 20}
---

# 图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev Unlock V1（换装前置）_1940800414864535554.json`

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
- `VAEDecode` ★核心
- `SaveImage`
- `UnetLoaderGGUF` ★核心
- `SaveLatent`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `KSampler` ★核心
- `LoadLatent`

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

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`MagCache`、`EmptySD3LatentImage`、`GoogleTranslateTextNode`、`VAEDecode`、`SaveImage`、`UnetLoaderGGUF`、`SaveLatent`、`LoadImage`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`LoadLatent`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
