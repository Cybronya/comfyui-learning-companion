---
key: 平台全量/Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738.json
name: Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738.json
hash: bef19a26ab64d711
coverage: 0.96
learned_at: 2026-11-14 00:28:31
nodes: [UNETLoader, DifferentialDiffusion, DualCLIPLoader, ConditioningZeroOut, FluxGuidance, InpaintModelConditioning, VAELoader, VAEDecode, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAEDecode, VAEDecode, VAEDecode, KSampler, SaveImage, SaveImage, SaveImage, SaveImage, KSampler, KSampler, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 509104128438711, "steps": 27}
---

# 平台全量/Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `InpaintModelConditioning`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `seed` = `509104128438711`
- `steps` = `27`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`UNETLoader`、`DifferentialDiffusion`、`DualCLIPLoader`、`ConditioningZeroOut`、`FluxGuidance`、`InpaintModelConditioning`、`VAELoader`、`VAEDecode`、`LoadImage`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
