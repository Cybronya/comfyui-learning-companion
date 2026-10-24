---
key: 图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json
name: Flux2.0多图编辑工作流_1993686011580448770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json
hash: f93e7a127530fbf0
coverage: 1
learned_at: 2026-10-23 11:00:51
nodes: [VAEDecode, VAELoader, SaveImage, UNETLoader, CLIPLoader, FluxGuidance, LoadImage, ReferenceLatent, VAEEncode, VAEEncode, ReferenceLatent, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, CLIPTextEncode, ReferenceLatent, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 593508362627232, "steps": 20}
---

# 图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.0多图编辑工作流_1993686011580448770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `FluxGuidance`
- `LoadImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `593508362627232`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`VAEDecode`、`VAELoader`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`FluxGuidance`、`LoadImage`、`ReferenceLatent`、`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
