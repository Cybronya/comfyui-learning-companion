---
key: 图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json
name: 单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json
hash: 371b2a43f86e6bcc
coverage: 0.933333
learned_at: 2026-10-23 12:32:38
nodes: [CLIPLoader, VAELoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, CFGGuider, SaveImage, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, Image Comparer (rgthree), UNETLoader, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
---

# 图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `CFGGuider`
- `SaveImage`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`CFGGuider`、`SaveImage`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
