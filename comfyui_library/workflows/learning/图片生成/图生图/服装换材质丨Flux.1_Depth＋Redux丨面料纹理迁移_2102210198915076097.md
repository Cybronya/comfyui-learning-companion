---
key: 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
name: 服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
hash: cb3ee18accd9b1aa
coverage: 0.782609
learned_at: 2026-10-09 22:27:09
nodes: [FluxGuidance, StyleModelAdvancedApply, InstructPixToPixConditioning, KSampler, VAEDecode, SaveImage, Anything Everywhere3, Anything Everywhere, Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, CLIPVisionEncode, LayerUtility: TextBox, LayerUtility: ImageScaleByAspectRatio V2, DepthAnythingPreprocessor, RHHiddenNodes, LoadImage, LoadImage, StyleModelLoader, CLIPVisionLoader, UNETLoader, DualCLIPLoader, VAELoader]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 353748859257925, "steps": 20}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102210198915076097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `FluxGuidance`
- `StyleModelAdvancedApply`
- `InstructPixToPixConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Anything Everywhere3`
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
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
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `seed` = `353748859257925`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`FluxGuidance`、`StyleModelAdvancedApply`、`InstructPixToPixConditioning`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`CLIPVisionEncode`、`DepthAnythingPreprocessor`、`RHHiddenNodes`、`LoadImage`、`StyleModelLoader`、`CLIPVisionLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: TextBox`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、DepthAnythingPreprocessor

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识
