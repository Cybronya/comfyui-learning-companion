---
key: 图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json
name: 时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json
hash: 548bec76b0944b83
coverage: 0.793103
learned_at: 2026-10-15 22:28:52
nodes: [VAEDecode, RandomNoise, SamplerCustomAdvanced, BasicGuider, FluxGuidance, FluxForwardOverrider, ApplyTeaCachePatch, SetNode, Int Literal, GetNode, ModelSamplingFlux, Int Literal, GetNode, LoraLoaderModelOnly, KSamplerSelect, BasicScheduler, Note, SaveImage, PlaySound|pysssss, Note, VAELoader, EmptySD3LatentImage, String Literal, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, ConditioningCombine, UNETLoader, Reroute]
patterns: []
missing: []
---

# 图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `VAEDecode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `FluxGuidance`
- `FluxForwardOverrider`
- `ApplyTeaCachePatch`
- `SetNode`
- `Int Literal`
- `GetNode`
- `ModelSamplingFlux`
- `Int Literal`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Note`
- `SaveImage`
- `PlaySound|pysssss`
- `Note`
- `VAELoader`
- `EmptySD3LatentImage`
- `String Literal`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningCombine`
- `UNETLoader` ★核心
- `Reroute`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`FluxGuidance`、`FluxForwardOverrider`、`ApplyTeaCachePatch`、`Int Literal`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`KSamplerSelect`、`BasicScheduler`、`SaveImage`、`PlaySound|pysssss`、`VAELoader`、`EmptySD3LatentImage`、`String Literal`、`DualCLIPLoader`、`CLIPTextEncode`、`ConditioningCombine`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
