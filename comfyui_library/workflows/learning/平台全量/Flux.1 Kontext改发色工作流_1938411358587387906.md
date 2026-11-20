---
key: 平台全量/Flux.1 Kontext改发色工作流_1938411358587387906.json
name: Flux.1 Kontext改发色工作流_1938411358587387906
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1 Kontext改发色工作流_1938411358587387906.json
hash: 4027c92516ba689a
coverage: 0.941176
learned_at: 2026-11-14 00:28:47
nodes: [VAELoader, DualCLIPLoader, ConditioningZeroOut, PreviewImage, SaveImage, LoadImageOutput, KSampler, VAEDecode, FluxKontextImageScale, ImageStitch, FluxGuidance, ReferenceLatent, VAEEncode, CLIPTextEncode, UNETLoader, LoadImage, Label (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 214273145428667, "steps": 20}
---

# 平台全量/Flux.1 Kontext改发色工作流_1938411358587387906.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1 Kontext改发色工作流_1938411358587387906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `SaveImage`
- `LoadImageOutput`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `ImageStitch`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `214273145428667`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`SaveImage`、`LoadImageOutput`、`KSampler`、`VAEDecode`、`FluxKontextImageScale`、`ImageStitch`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`CLIPTextEncode`、`UNETLoader`、`LoadImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
