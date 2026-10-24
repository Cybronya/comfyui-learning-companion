---
key: 图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033.json
name: Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033.json
hash: 971f057c70182ce0
coverage: 0.931507
learned_at: 2026-10-23 10:56:25
nodes: [VAELoader, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, EmptySD3LatentImage, VAEDecode, SaveImage, ImageConcanate, LoadImage, DualCLIPLoader, SaveImage, ShowText, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, ConditioningZeroOut, FluxGuidance, ReferenceLatent, NunchakuFluxDiTLoader, easy promptConcat, CR Prompt Text, RHHiddenNodes, Note, CR Prompt Text, CR Prompt Text, CR Prompt Text, JWInteger, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, ImpactSwitch, Note, LoadImage, LoadImage, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 607389948144868, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 22种风格转绘加速稳定版V1（Nunchaku）_1939713012859052033.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `VAELoader`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `DualCLIPLoader`
- `SaveImage`
- `ShowText`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `NunchakuFluxDiTLoader`
- `easy promptConcat`
- `CR Prompt Text`
- `RHHiddenNodes`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `ImpactSwitch`
- `Note`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `607389948144868`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（68/73）

**有卡**：`VAELoader`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`LoadImage`、`DualCLIPLoader`、`ShowText`、`KSampler`、`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`NunchakuFluxDiTLoader`、`easy promptConcat`、`CR Prompt Text`、`RHHiddenNodes`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
