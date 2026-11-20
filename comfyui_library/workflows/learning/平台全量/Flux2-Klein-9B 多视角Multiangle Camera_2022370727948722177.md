---
key: 平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json
name: Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json
hash: 5697df8277c7dda6
coverage: 0.888889
learned_at: 2026-11-14 00:29:27
nodes: [Reroute, CLIPLoader, VAELoader, Reroute, SamplerCustomAdvanced, ReferenceLatent, VAEEncode, ReferenceLatent, UNETLoader, RandomNoise, EmptyFlux2LatentImage, Flux2Scheduler, CFGGuider, KSamplerSelect, ConditioningZeroOut, Reroute, MuyeSizeSelector, LoadImage, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Reroute, CLIPTextEncode, QwenMultiangleCameraNode]
patterns: []
missing: []
---

# 平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux2-Klein-9B 多视角Multiangle Camera_2022370727948722177.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `UNETLoader` ★核心
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `Reroute`
- `MuyeSizeSelector`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `CLIPTextEncode` ★核心
- `QwenMultiangleCameraNode`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`ReferenceLatent`、`VAEEncode`、`UNETLoader`、`RandomNoise`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`CFGGuider`、`KSamplerSelect`、`ConditioningZeroOut`、`MuyeSizeSelector`、`LoadImage`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`QwenMultiangleCameraNode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider
