---
key: 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
name: 服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
hash: cb3ee18accd9b1aa
coverage: 0.782609
learned_at: 2026-10-10 21:22:17
nodes: [FluxGuidance, StyleModelAdvancedApply, InstructPixToPixConditioning, KSampler, VAEDecode, SaveImage, Anything Everywhere3, Anything Everywhere, Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, CLIPVisionEncode, LayerUtility: TextBox, LayerUtility: ImageScaleByAspectRatio V2, DepthAnythingPreprocessor, RHHiddenNodes, LoadImage, LoadImage, StyleModelLoader, CLIPVisionLoader, UNETLoader, DualCLIPLoader, VAELoader]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 353748859257925, "steps": 20}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json`

## 结构

**节点**（23 个）：
- `FluxGuidance`
- `StyleModelAdvancedApply`
- `InstructPixToPixConditioning`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `Anything Everywhere3`
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CLIPVisionEncode`
- `LayerUtility: TextBox`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DepthAnythingPreprocessor`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `seed` = `353748859257925`
- `steps` = `20`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`FluxGuidance`、`StyleModelAdvancedApply`、`InstructPixToPixConditioning`、`KSampler`、`VAEDecode`、`SaveImage`、`Anything Everywhere3`、`Anything Everywhere`、`CLIPTextEncode`、`ConditioningZeroOut`、`CLIPVisionEncode`、`LayerUtility: TextBox`、`LayerUtility: ImageScaleByAspectRatio V2`、`DepthAnythingPreprocessor`、`RHHiddenNodes`、`LoadImage`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: TextBox`

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识
