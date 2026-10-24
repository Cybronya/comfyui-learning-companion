---
key: 图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json
name: Klein一键快速扩图王4.0_2016076763520045057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json
hash: 530fb49714702241
coverage: 1
learned_at: 2026-10-23 11:04:59
nodes: [KSamplerSelect, CLIPLoader, CFGGuider, UNETLoader, SamplerCustomAdvanced, RandomNoise, ConditioningZeroOut, ReferenceLatent, Flux2Scheduler, VAELoader, ReferenceLatent, VAEEncode, VAEDecode, LayerStyle: ColorOverlay, ImageScaleToTotalPixels, CLIPTextEncode, ImagePadForOutpaint, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Klein一键快速扩图王4.0_2016076763520045057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `CFGGuider`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Flux2Scheduler`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `LayerStyle: ColorOverlay`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`KSamplerSelect`、`CLIPLoader`、`CFGGuider`、`UNETLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`ConditioningZeroOut`、`ReferenceLatent`、`Flux2Scheduler`、`VAELoader`、`VAEEncode`、`VAEDecode`、`LayerStyle: ColorOverlay`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ImagePadForOutpaint`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
