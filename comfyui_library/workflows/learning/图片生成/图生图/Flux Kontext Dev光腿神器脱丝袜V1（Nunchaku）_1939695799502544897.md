---
key: 图片生成/图生图/Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897.json
name: Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897.json
hash: 2812f0960657313e
coverage: 0.875
learned_at: 2026-10-23 10:56:58
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, KSampler, VAEDecode, SaveImage, ImageConcanate, SaveImage, CR Prompt Text, NunchakuFluxLoraLoader, LoadImage, GoogleTranslateTextNode, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 832413146950096, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev光腿神器脱丝袜V1（Nunchaku）_1939695799502544897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `CR Prompt Text`
- `NunchakuFluxLoraLoader` ★核心
- `LoadImage`
- `GoogleTranslateTextNode`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `832413146950096`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`CR Prompt Text`、`NunchakuFluxLoraLoader`、`LoadImage`、`GoogleTranslateTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
