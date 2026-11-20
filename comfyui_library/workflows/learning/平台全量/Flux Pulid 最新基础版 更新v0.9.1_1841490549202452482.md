---
key: 平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json
name: Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json
hash: 140de5ea5c8450f3
coverage: 0.923077
learned_at: 2026-11-14 00:28:01
nodes: [SamplerCustomAdvanced, BasicGuider, KSamplerSelect, Reroute, PulidFluxEvaClipLoader, RandomNoise, VAELoader, VAEDecode, SaveImage, PreviewImage, FluxGuidance, CLIPTextEncode, RH_Prompter, DisplayText, EmptySD3LatentImage, DualCLIPLoader, ApplyPulidFlux, LoraLoaderModelOnly, easy cleanGpuUsed, PulidFluxInsightFaceLoader, BasicScheduler, UNETLoader, UnetLoaderGGUF, TextBox, PulidFluxModelLoader, LoadImage]
patterns: []
missing: []
---

# 平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Pulid 最新基础版 更新v0.9.1_1841490549202452482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `Reroute`
- `PulidFluxEvaClipLoader`
- `RandomNoise`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `RH_Prompter`
- `DisplayText`
- `EmptySD3LatentImage`
- `DualCLIPLoader`
- `ApplyPulidFlux`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `PulidFluxInsightFaceLoader`
- `BasicScheduler`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `TextBox`
- `PulidFluxModelLoader`
- `LoadImage`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`PulidFluxEvaClipLoader`、`RandomNoise`、`VAELoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`CLIPTextEncode`、`RH_Prompter`、`DisplayText`、`EmptySD3LatentImage`、`DualCLIPLoader`、`ApplyPulidFlux`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`PulidFluxInsightFaceLoader`、`BasicScheduler`、`UNETLoader`、`UnetLoaderGGUF`、`TextBox`、`PulidFluxModelLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
