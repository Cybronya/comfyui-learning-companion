---
key: 图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json
name: FLUX.1Kontext.dev-单多图测试_1939156551691067393
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json
hash: c1c484b5751df3b1
coverage: 0.878049
learned_at: 2026-10-23 10:54:02
nodes: [ConditioningZeroOut, PreviewImage, LoadImage, ReferenceLatent, FluxGuidance, VAEEncode, ImageStitch, UNETLoader, DualCLIPLoader, CLIPTextEncode, VAELoader, KSampler, RH_Translator, LoadImage, FluxKontextImageScale, ImageResizeKJv2, SDXLEmptyLatentSizePicker+, ConditioningZeroOut, PreviewImage, VAEDecode, ReferenceLatent, FluxGuidance, VAEEncode, UNETLoader, DualCLIPLoader, CLIPTextEncode, VAELoader, FluxKontextImageScale, ImageResizeKJv2, SDXLEmptyLatentSizePicker+, LoadImage, LoadImage, SDXLEmptyLatentSizePicker+, ImageStitch, KSampler, RH_Translator, MarkdownNote, PreviewImage, VAEDecode, SaveImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 0, "cfg": 1, "denoise": 1, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 113231584388857, "steps": 20, "width": "832x1216 (0.68)"}
---

# 图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1Kontext.dev-单多图测试_1939156551691067393.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImage`
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `ImageStitch`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `RH_Translator`
- `LoadImage`
- `FluxKontextImageScale`
- `ImageResizeKJv2`
- `SDXLEmptyLatentSizePicker+` ★核心
- `ConditioningZeroOut`
- `PreviewImage`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `FluxKontextImageScale`
- `ImageResizeKJv2`
- `SDXLEmptyLatentSizePicker+` ★核心
- `LoadImage`
- `LoadImage`
- `SDXLEmptyLatentSizePicker+` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `RH_Translator`
- `MarkdownNote`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `113231584388857`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `832x1216 (0.68)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`ConditioningZeroOut`、`LoadImage`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`ImageStitch`、`UNETLoader`、`DualCLIPLoader`、`CLIPTextEncode`、`VAELoader`、`KSampler`、`RH_Translator`、`FluxKontextImageScale`、`ImageResizeKJv2`、`SDXLEmptyLatentSizePicker+`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
