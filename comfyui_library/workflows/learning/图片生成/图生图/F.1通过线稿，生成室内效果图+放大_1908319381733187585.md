---
key: 图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json
name: F.1通过线稿，生成室内效果图+放大_1908319381733187585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json
hash: d54a78e0849b3747
coverage: 0.941176
learned_at: 2026-10-23 10:52:38
nodes: [FluxGuidance, DifferentialDiffusion, InstructPixToPixConditioning, VAEDecode, ConditioningZeroOut, CLIPTextEncodeFlux, VAELoader, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, LoadImage, Canny, ArgosTranslateTextNode, ImageResize, KSampler, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 360838865191937, "steps": 25}
---

# 图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1通过线稿，生成室内效果图+放大_1908319381733187585.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `FluxGuidance`
- `DifferentialDiffusion`
- `InstructPixToPixConditioning`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Canny`
- `ArgosTranslateTextNode`
- `ImageResize`
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `360838865191937`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`FluxGuidance`、`DifferentialDiffusion`、`InstructPixToPixConditioning`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncodeFlux`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`Canny`、`ArgosTranslateTextNode`、`ImageResize`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、Canny
