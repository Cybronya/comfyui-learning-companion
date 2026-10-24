---
key: 图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json
name: 双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json
hash: 0ecdb7beeea4cb63
coverage: 0.941176
learned_at: 2026-10-23 12:35:14
nodes: [ConditioningZeroOut, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, LoadImage, LoadImage, Flux2Scheduler, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
---

# 图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `Flux2Scheduler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`LoadImage`、`Flux2Scheduler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
