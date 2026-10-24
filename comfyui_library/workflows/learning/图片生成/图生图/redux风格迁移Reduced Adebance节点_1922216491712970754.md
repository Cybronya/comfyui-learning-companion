---
key: 图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json
name: redux风格迁移Reduced Adebance节点_1922216491712970754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json
hash: 37c25c0c046c9070
coverage: 1
learned_at: 2026-10-23 11:44:45
nodes: [StyleModelLoader, CLIPVisionLoader, VAEDecode, SaveImage, ConditioningZeroOut, VAELoader, KSampler, ReduxAdvanced, LoadImage, LoadImage, easy imageConcat, CLIPTextEncode, DualCLIPLoader, FluxGuidance, DifferentialDiffusion, UNETLoader, easy imageConcat, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, EmptyImage, ImageToMask, MaskToImage, InpaintModelConditioning]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 699684739871086, "steps": 30}
---

# 图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/redux风格迁移Reduced Adebance节点_1922216491712970754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `StyleModelLoader`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `VAELoader`
- `KSampler` ★核心
- `ReduxAdvanced`
- `LoadImage`
- `LoadImage`
- `easy imageConcat`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `easy imageConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `EmptyImage`
- `ImageToMask`
- `MaskToImage`
- `InpaintModelConditioning`

## 关键参数

- `seed` = `699684739871086`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`StyleModelLoader`、`CLIPVisionLoader`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`VAELoader`、`KSampler`、`ReduxAdvanced`、`LoadImage`、`easy imageConcat`、`CLIPTextEncode`、`DualCLIPLoader`、`FluxGuidance`、`DifferentialDiffusion`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`EmptyImage`、`ImageToMask`、`MaskToImage`、`InpaintModelConditioning`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
