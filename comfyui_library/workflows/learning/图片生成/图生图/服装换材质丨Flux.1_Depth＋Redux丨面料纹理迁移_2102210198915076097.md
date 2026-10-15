---
key: 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
name: 服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json
hash: cb3ee18accd9b1aa
coverage: 0.869565
learned_at: 2026-10-15 22:25:57
nodes: [FluxGuidance, StyleModelAdvancedApply, InstructPixToPixConditioning, KSampler, VAEDecode, SaveImage, Anything Everywhere3, Anything Everywhere, Anything Everywhere, CLIPTextEncode, ConditioningZeroOut, CLIPVisionEncode, LayerUtility: TextBox, LayerUtility: ImageScaleByAspectRatio V2, DepthAnythingPreprocessor, RHHiddenNodes, LoadImage, LoadImage, StyleModelLoader, CLIPVisionLoader, UNETLoader, DualCLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 353748859257925, "steps": 20}
---

# 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json`

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

覆盖率 **87%**（20/23）

**有卡**：`FluxGuidance`、`StyleModelAdvancedApply`、`InstructPixToPixConditioning`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`CLIPVisionEncode`、`LayerUtility: TextBox`、`LayerUtility: ImageScaleByAspectRatio V2`、`DepthAnythingPreprocessor`、`RHHiddenNodes`、`LoadImage`、`StyleModelLoader`、`CLIPVisionLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、DepthAnythingPreprocessor
