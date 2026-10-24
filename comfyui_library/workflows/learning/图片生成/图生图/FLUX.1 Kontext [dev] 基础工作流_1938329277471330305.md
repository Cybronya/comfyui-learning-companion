---
key: 图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json
name: FLUX.1 Kontext [dev] 基础工作流_1938329277471330305
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json
hash: 658f28bb3f283a1d
coverage: 0.782609
learned_at: 2026-10-23 10:53:59
nodes: [VAELoader, DualCLIPLoader, ConditioningZeroOut, SaveImage, VAEDecode, MarkdownNote, FluxGuidance, ReferenceLatent, VAEEncode, PreviewImage, FluxKontextImageScale, CLIPTextEncode, easy cleanGpuUsed, ImageScale, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, easy cleanGpuUsed, LoadImage, ImageStitch, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 792700593471723, "steps": 20}
---

# 图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `SaveImage`
- `VAEDecode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `PreviewImage`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ImageScale`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `ImageStitch`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `792700593471723`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`FluxKontextImageScale`、`CLIPTextEncode`、`easy cleanGpuUsed`、`ImageScale`、`UNETLoader`、`LoadImage`、`ImageStitch`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
