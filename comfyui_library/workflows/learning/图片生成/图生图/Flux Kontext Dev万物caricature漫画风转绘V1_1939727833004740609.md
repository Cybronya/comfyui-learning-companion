---
key: 图片生成/图生图/Flux Kontext Dev万物caricature漫画风转绘V1_1939727833004740609.json
name: Flux Kontext Dev万物caricature漫画风转绘V1_1939727833004740609
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物caricature漫画风转绘V1_1939727833004740609.json
hash: 6004bdf7b04ef4ba
coverage: 0.925926
learned_at: 2026-10-23 10:56:40
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, DualCLIPLoader, KSampler, VAEDecode, SaveImage, SaveImage, CLIPTextEncode, GoogleTranslateTextNode, ShowText, UnetLoaderGGUF, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, LoadImage, ImageConcanate, CR Prompt Text, LoraLoaderModelOnly, MagCache, EmptySD3LatentImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 312401850682443, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物caricature漫画风转绘V1_1939727833004740609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物caricature漫画风转绘V1_1939727833004740609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
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
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `ShowText`
- `UnetLoaderGGUF` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `ImageConcanate`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `MagCache`
- `EmptySD3LatentImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `312401850682443`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`DualCLIPLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`ShowText`、`UnetLoaderGGUF`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`LoadImage`、`ImageConcanate`、`CR Prompt Text`、`LoraLoaderModelOnly`、`MagCache`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
