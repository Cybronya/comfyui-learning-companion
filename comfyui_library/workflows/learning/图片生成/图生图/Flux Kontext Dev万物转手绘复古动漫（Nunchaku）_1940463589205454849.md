---
key: 图片生成/图生图/Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849.json
name: Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849.json
hash: cb65beacf35dc91f
coverage: 0.913043
learned_at: 2026-10-23 10:56:51
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, VAEDecode, SaveImage, KSampler, SaveImage, ImageConcanate, NunchakuFluxLoraLoader, CR Prompt Text, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 171051317545561, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物转手绘复古动漫（Nunchaku）_1940463589205454849.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
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
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `ImageConcanate`
- `NunchakuFluxLoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `171051317545561`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`KSampler`、`ImageConcanate`、`NunchakuFluxLoraLoader`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
