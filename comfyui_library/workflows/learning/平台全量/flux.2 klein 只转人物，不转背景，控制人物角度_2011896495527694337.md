---
key: 平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json
name: flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json
hash: 0544962e0c44f188
coverage: 1
learned_at: 2026-11-14 01:10:59
nodes: [CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, ImageScaleToTotalPixels, CLIPTextEncode, ConditioningZeroOut, VAEEncode, ReferenceLatent, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, VAELoader, VAEDecode, Get Image Size, SaveImage, CLIPLoader, UNETLoader, LoadImage, QwenMultiangleCameraNode]
patterns: []
missing: []
---

# 平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json

> 来源文件 `comfyui_library/workflows/平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `Get Image Size`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `QwenMultiangleCameraNode`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`VAELoader`、`VAEDecode`、`Get Image Size`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`QwenMultiangleCameraNode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider
