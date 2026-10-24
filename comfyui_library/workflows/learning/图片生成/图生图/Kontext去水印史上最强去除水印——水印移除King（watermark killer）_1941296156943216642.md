---
key: 图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json
name: Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json
hash: 3ac72b9c1148a096
coverage: 0.933333
learned_at: 2026-10-23 11:07:08
nodes: [DualCLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, VAEEncode, ReferenceLatent, KSampler, DeepTranslatorTextNode, SaveImage, VAEDecode, LoadImage, Image Comparer (rgthree), NunchakuFluxDiTLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 223724833190377, "steps": 20}
---

# 图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `DeepTranslatorTextNode`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `NunchakuFluxDiTLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `223724833190377`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxGuidance`、`FluxKontextImageScale`、`VAEEncode`、`ReferenceLatent`、`KSampler`、`DeepTranslatorTextNode`、`SaveImage`、`VAEDecode`、`LoadImage`、`NunchakuFluxDiTLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
