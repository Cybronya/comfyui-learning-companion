---
key: 图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json
name: FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json
hash: 715e3144e0b53d53
coverage: 0.794118
learned_at: 2026-10-23 10:54:41
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, Int, Int, PrimitiveBoolean, ComfySwitchNode, ReferenceMultiLatent, BasicGuider, ReferenceMultiLatent, ResolutionSelector, VAEDecode, AnySwitch, SamplerCustomAdvanced, KSampler, CLIPTextEncode, JjkText, UNETLoader, LoadImage, ManualSigmas, KSamplerSelect, EmptyFlux2LatentImage, RandomNoise, LoadImage, CreateBoundingBoxes, PreviewAny, MarkdownNote, MarkdownNote, MarkdownNote, CLIPTextEncode, Fast Bypasser (rgthree), SaveImage, PreviewImage, ImageConcatMulti]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 586468331778708, "steps": 25}
---

# 图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX3.0 Klein多图编辑 满血+急速生成_2110934398165143554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ReferenceMultiLatent`
- `BasicGuider`
- `ReferenceMultiLatent`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `AnySwitch`
- `SamplerCustomAdvanced` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `UNETLoader` ★核心
- `LoadImage`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `LoadImage`
- `CreateBoundingBoxes`
- `PreviewAny`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `Fast Bypasser (rgthree)`
- `SaveImage`
- `PreviewImage`
- `ImageConcatMulti`

## 关键参数

- `seed` = `586468331778708`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`Int`、`PrimitiveBoolean`、`ReferenceMultiLatent`、`BasicGuider`、`ResolutionSelector`、`VAEDecode`、`AnySwitch`、`SamplerCustomAdvanced`、`KSampler`、`UNETLoader`、`LoadImage`、`ManualSigmas`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`RandomNoise`、`CreateBoundingBoxes`、`Fast Bypasser (rgthree)`、`SaveImage`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage
