---
key: 图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json
name: F.1通过线稿，生成室内效果图_1908530217424400386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json
hash: dc1f475f9fb998b1
coverage: 0.888889
learned_at: 2026-10-23 10:52:39
nodes: [KSampler, ImageResize, SaveImage, CLIPTextEncodeFlux, DualCLIPLoader, ConditioningZeroOut, VAELoader, BaiduTranslateNode, Note, UNETLoader, DifferentialDiffusion, LoadImage, InstructPixToPixConditioning, VAEDecode, LoraLoaderModelOnly, PreviewImage, FluxGuidance, Canny]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 555506548222477, "steps": 20}
---

# 图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1通过线稿，生成室内效果图_1908530217424400386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `KSampler` ★核心
- `ImageResize`
- `SaveImage`
- `CLIPTextEncodeFlux` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `BaiduTranslateNode`
- `Note`
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `LoadImage`
- `InstructPixToPixConditioning`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `FluxGuidance`
- `Canny`

## 关键参数

- `seed` = `555506548222477`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`KSampler`、`ImageResize`、`SaveImage`、`CLIPTextEncodeFlux`、`DualCLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`BaiduTranslateNode`、`UNETLoader`、`DifferentialDiffusion`、`LoadImage`、`InstructPixToPixConditioning`、`VAEDecode`、`LoraLoaderModelOnly`、`FluxGuidance`、`Canny`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、Canny
