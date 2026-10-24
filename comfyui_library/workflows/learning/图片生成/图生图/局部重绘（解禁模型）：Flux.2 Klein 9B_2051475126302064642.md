---
key: 图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json
name: 局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json
hash: ea09946b11f1ff41
coverage: 0.944444
learned_at: 2026-10-23 12:50:14
nodes: [UNETLoader, CLIPLoader, VAELoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, Mask Fill Holes, LayerMask: MaskGrow, DrawMaskOnImage, SamplerCustomAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason]
patterns: []
missing: []
---

# 图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘（解禁模型）：Flux.2 Klein 9B_2051475126302064642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `Mask Fill Holes`
- `LayerMask: MaskGrow`
- `DrawMaskOnImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`Mask Fill Holes`、`LayerMask: MaskGrow`、`DrawMaskOnImage`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect
