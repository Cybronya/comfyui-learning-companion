---
key: 图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json
name: Flux_Krea_Redux_Advanced工作流_1966815491174096897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json
hash: 034701832b817fdf
coverage: 0.75
learned_at: 2026-10-23 11:01:46
nodes: [SamplerCustomAdvanced, BasicGuider, DualCLIPLoader, Reroute, Reroute, Reroute, VAEDecode, BasicScheduler, RandomNoise, KSamplerSelect, EmptySD3LatentImage, ModelSamplingFlux, Note, CLIPVisionLoader, StyleModelLoader, FluxGuidance, LoadImage, Note, VAELoader, DualCLIPLoader, UnetLoaderGGUF, UNETLoader, VAELoader, ReduxAdvanced, CLIPTextEncode, SaveImage, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
---

# 图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux_Krea_Redux_Advanced工作流_1966815491174096897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `DualCLIPLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `BasicScheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `Note`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `FluxGuidance`
- `LoadImage`
- `Note`
- `VAELoader`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ReduxAdvanced`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PrimitiveNode`
- `PrimitiveNode`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`DualCLIPLoader`、`VAEDecode`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`CLIPVisionLoader`、`StyleModelLoader`、`FluxGuidance`、`LoadImage`、`VAELoader`、`UnetLoaderGGUF`、`UNETLoader`、`ReduxAdvanced`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
