---
key: 图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json
name: SeedVR2.5-去水印修复放大（有用）_2013859487152607234
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json
hash: dd1aebbcdc8863d3
coverage: 0.818182
learned_at: 2026-10-23 11:24:59
nodes: [VAELoader, DualCLIPLoader, NunchakuFluxDiTLoader, ReferenceLatent, VAEEncode, ConditioningZeroOut, FluxGuidance, MarkdownNote, KSampler, PreviewImage, CLIPTextEncode, LoadImage, ImageStitch, FluxKontextImageScale, PreviewImage, easy cleanGpuUsed, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 606672046415711, "steps": 20}
---

# 图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `MarkdownNote`
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageStitch`
- `FluxKontextImageScale`
- `PreviewImage`
- `easy cleanGpuUsed`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `606672046415711`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`VAELoader`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`FluxGuidance`、`KSampler`、`CLIPTextEncode`、`LoadImage`、`ImageStitch`、`FluxKontextImageScale`、`easy cleanGpuUsed`、`SaveImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、SeedVR2LoadDiTModel
