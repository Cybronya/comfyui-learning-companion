---
key: 平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json
name: PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json
hash: 8b94e6aec6ccea5d
coverage: 0.952381
learned_at: 2026-11-14 00:48:40
nodes: [ApplyPulidFlux, KSamplerSelect, BasicGuider, PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, SamplerCustomAdvanced, RandomNoise, CLIPTextEncode, FluxGuidance, BasicScheduler, EmptySD3LatentImage, LayerUtility: PurgeVRAM, VAELoader, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAEDecode, SaveImage, LoadImage, PreviewImage]
patterns: []
missing: []
---

# 平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json

> 来源文件 `comfyui_library/workflows/平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ApplyPulidFlux`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `BasicScheduler`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ApplyPulidFlux`、`KSamplerSelect`、`BasicGuider`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPTextEncode`、`FluxGuidance`、`BasicScheduler`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
