---
key: 图片生成/图生图/Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810.json
name: Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810.json
hash: 9c6458214f37d6ed
coverage: 0.913043
learned_at: 2026-10-23 10:57:09
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, VAEDecode, SaveImage, NunchakuFluxLoraLoader, CR Prompt Text, LoadImage, KSampler, SaveImage, ImageConcanate]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 199434417451808, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev手绘风4视图（Nunchaku）_1940445748691447810.json`

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
- `NunchakuFluxLoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `ImageConcanate`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `199434417451808`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`NunchakuFluxLoraLoader`、`CR Prompt Text`、`LoadImage`、`KSampler`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
