---
key: 视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json
name: Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json
hash: f2655828d74379ed
coverage: 0.705882
learned_at: 2026-10-15 22:47:01
nodes: [Note, Pick From Batch (mtb), Note, CLIPLoader, VAELoader, ImageScaleBy, CLIPTextEncode, VHS_VideoCombine, CLIPTextEncode, Note, Note, WanImageToVideo, ModelSamplingSD3, VHS_VideoCombine, ModelSamplingSD3, Note, Note, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, PreviewImage, KSamplerAdvanced, Seed (rgthree), ImageScaleBy, SaveImage, PrimitiveStringMultiline, mxSlider2D, Note, Note, RIFE VFI, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `Note`
- `Pick From Batch (mtb)`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `ImageScaleBy`
- `SaveImage`
- `PrimitiveStringMultiline`
- `mxSlider2D`
- `Note`
- `Note`
- `RIFE VFI`
- `Label (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`Pick From Batch (mtb)`、`CLIPLoader`、`VAELoader`、`ImageScaleBy`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`Seed (rgthree)`、`SaveImage`、`mxSlider2D`、`RIFE VFI`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、SaveImage
