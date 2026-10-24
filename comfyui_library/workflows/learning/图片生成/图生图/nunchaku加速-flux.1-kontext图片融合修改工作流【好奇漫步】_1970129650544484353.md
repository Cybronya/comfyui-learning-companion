---
key: 图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json
name: nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json
hash: bc63e58f0abf7590
coverage: 0.678571
learned_at: 2026-10-23 11:41:24
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, SaveImage, VAEDecode, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, MarkdownNote, MarkdownNote, MarkdownNote, ReferenceLatent, KSampler, MarkdownNote, NunchakuFluxDiTLoader, DualCLIPLoader, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, ImageStitch, LoadImageOutput, LoadImage, LoadImageOutput, EmptySD3LatentImage, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 223747821586759, "steps": 20}
---

# 图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ReferenceLatent`
- `KSampler` ★核心
- `MarkdownNote`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `ImageStitch`
- `LoadImageOutput`
- `LoadImage`
- `LoadImageOutput`
- `EmptySD3LatentImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `223747821586759`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（19/28）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`KSampler`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`LoadImage`、`ImageStitch`、`LoadImageOutput`、`EmptySD3LatentImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
