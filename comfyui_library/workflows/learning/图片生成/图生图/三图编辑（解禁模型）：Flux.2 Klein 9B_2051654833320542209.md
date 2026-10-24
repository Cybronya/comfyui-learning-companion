---
key: 图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json
name: 三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json
hash: 511bd56fd5870ba1
coverage: 0.9
learned_at: 2026-10-23 12:01:49
nodes: [Reroute, UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, SaveImage, VAEDecode, Image Comparer (rgthree), LoadImage, Flux2Scheduler, RandomNoise, LoadImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
---

# 图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `Flux2Scheduler`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`SaveImage`、`VAEDecode`、`LoadImage`、`Flux2Scheduler`、`RandomNoise`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
