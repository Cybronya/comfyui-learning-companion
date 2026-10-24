---
key: 图片生成/图生图/（自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970.json
name: （自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970.json
hash: 3db06bd5767a812d
coverage: 0.958333
learned_at: 2026-10-23 13:38:07
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, NunchakuFluxLoraLoader, GoogleTranslateTextNode, LoadImage, CR Prompt Text, FluxKontextImageScale, SaveImage, VAELoader, LoadLatent, VAEDecode, SaveImage, SaveLatent, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 201175548854655, "steps": 20}
---

# 图片生成/图生图/（自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Flux Kontext Dev胸肌调整V1（Nunchaku）_1939731118046547970.json`

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
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `NunchakuFluxLoraLoader` ★核心
- `GoogleTranslateTextNode`
- `LoadImage`
- `CR Prompt Text`
- `FluxKontextImageScale`
- `SaveImage`
- `VAELoader`
- `LoadLatent`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveLatent`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `201175548854655`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`NunchakuFluxLoraLoader`、`GoogleTranslateTextNode`、`LoadImage`、`CR Prompt Text`、`FluxKontextImageScale`、`SaveImage`、`LoadLatent`、`VAEDecode`、`SaveLatent`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
