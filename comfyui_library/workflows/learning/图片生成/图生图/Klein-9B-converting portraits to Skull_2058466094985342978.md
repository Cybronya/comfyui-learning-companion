---
key: 图片生成/图生图/Klein-9B-converting portraits to Skull_2058466094985342978.json
name: Klein-9B-converting portraits to Skull_2058466094985342978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein-9B-converting portraits to Skull_2058466094985342978.json
hash: 2ef0a835600ce142
coverage: 0.913043
learned_at: 2026-10-23 11:04:30
nodes: [ConditioningZeroOut, CLIPTextEncode, EmptyFlux2LatentImage, Flux2KleinKSamplerExperimental, ReferenceLatent, VAEEncode, ReferenceLatent, CLIPTextEncode, Flux2KleinTextRefBalance, Flux2KleinRefLatentWeight, PathchSageAttentionKJ, Flux2Scheduler, UNETLoader, CLIPLoader, ResizeImagesByLongerEdge, VAELoader, AutoCropFaces, GetImageSize, PreviewImage, Image Comparer (rgthree), VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": 0.5, "scheduler": 1.15, "seed": 4, "steps": "randomize"}
---

# 图片生成/图生图/Klein-9B-converting portraits to Skull_2058466094985342978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein-9B-converting portraits to Skull_2058466094985342978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `Flux2KleinKSamplerExperimental` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `Flux2KleinTextRefBalance`
- `Flux2KleinRefLatentWeight`
- `PathchSageAttentionKJ`
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResizeImagesByLongerEdge`
- `VAELoader`
- `AutoCropFaces`
- `GetImageSize`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `4`
- `steps` = `randomize`
- `cfg` = `1`
- `sampler_name` = `0.5`
- `scheduler` = `1.15`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`Flux2KleinKSamplerExperimental`、`ReferenceLatent`、`VAEEncode`、`Flux2KleinTextRefBalance`、`Flux2KleinRefLatentWeight`、`PathchSageAttentionKJ`、`Flux2Scheduler`、`UNETLoader`、`CLIPLoader`、`ResizeImagesByLongerEdge`、`VAELoader`、`AutoCropFaces`、`GetImageSize`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、Flux2KleinRefLatentWeight
