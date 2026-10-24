---
key: 图片生成/图生图/Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866.json
name: Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866.json
hash: 25acbf0d03b2dbe6
coverage: 0.913043
learned_at: 2026-10-23 10:56:48
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, EmptySD3LatentImage, KSampler, VAEDecode, SaveImage, ImageConcanate, LoadImage, CR Prompt Text, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 516757149080959, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物穿黑色乳胶衣换装V1（Nunchaku）_1939678966276132866.json`

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
- `NunchakuFluxLoraLoader` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `516757149080959`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
