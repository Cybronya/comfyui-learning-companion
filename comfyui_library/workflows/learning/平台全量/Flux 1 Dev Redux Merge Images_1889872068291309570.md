---
key: 平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json
name: Flux 1 Dev Redux Merge Images_1889872068291309570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json
hash: 582759abb5b6aa58
coverage: 0.725
learned_at: 2026-11-14 00:27:30
nodes: [CLIPTextEncode, VAEDecode, SaveImage, VAELoader, DualCLIPLoader, UNETLoader, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, FluxGuidance, EmptySD3LatentImage, Note, ModelSamplingFlux, PrimitiveNode, PrimitiveNode, Note, CLIPVisionLoader, CLIPVisionEncode, LoadImage, StyleModelApply, StyleModelLoader, Note, ConditioningAverage, CLIPVisionEncode, LoadImage, StyleModelApply, ConditioningAverage, CLIPVisionEncode, StyleModelApply, ConditioningAverage, Note, Note, Note, Note, Note, LoadImage, Fast Groups Bypasser (rgthree), Text Multiline]
patterns: []
missing: []
---

# 平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux 1 Dev Redux Merge Images_1889872068291309570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `EmptySD3LatentImage`
- `Note`
- `ModelSamplingFlux`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LoadImage`
- `StyleModelApply`
- `StyleModelLoader`
- `Note`
- `ConditioningAverage`
- `CLIPVisionEncode`
- `LoadImage`
- `StyleModelApply`
- `ConditioningAverage`
- `CLIPVisionEncode`
- `StyleModelApply`
- `ConditioningAverage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`EmptySD3LatentImage`、`ModelSamplingFlux`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LoadImage`、`StyleModelApply`、`StyleModelLoader`、`ConditioningAverage`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
