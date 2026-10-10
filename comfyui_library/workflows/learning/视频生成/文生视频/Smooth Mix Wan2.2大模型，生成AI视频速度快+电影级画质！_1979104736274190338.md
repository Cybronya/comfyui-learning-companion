---
key: 视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json
name: Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix Wan2.2大模型，生成AI视频速度快+电影级画质！_1979104736274190338.json
hash: f2655828d74379ed
coverage: 0.529412
learned_at: 2026-10-10 23:05:43
nodes: [Note, Pick From Batch (mtb), Note, CLIPLoader, VAELoader, ImageScaleBy, CLIPTextEncode, VHS_VideoCombine, CLIPTextEncode, Note, Note, WanImageToVideo, ModelSamplingSD3, VHS_VideoCombine, ModelSamplingSD3, Note, Note, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, PreviewImage, KSamplerAdvanced, Seed (rgthree), ImageScaleBy, SaveImage, PrimitiveStringMultiline, mxSlider2D, Note, Note, RIFE VFI, Label (rgthree)]
patterns: []
missing: [Label (rgthree), Pick From Batch (mtb), RIFE VFI, easy cleanGpuUsed, easy cleanGpuUsed, Seed (rgthree)]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **53%**（18/34）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageScaleBy`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`UNETLoader`、`SaveImage`、`mxSlider2D`

**缺卡**（6）：`Label (rgthree)`、`Pick From Batch (mtb)`、`RIFE VFI`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SaveImage、ImageScaleBy

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
