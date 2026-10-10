---
key: 时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json
name: 时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json
hash: 548bec76b0944b83
coverage: 0.655172
learned_at: 2026-10-10 20:59:50
nodes: [VAEDecode, RandomNoise, SamplerCustomAdvanced, BasicGuider, FluxGuidance, FluxForwardOverrider, ApplyTeaCachePatch, SetNode, Int Literal, GetNode, ModelSamplingFlux, Int Literal, GetNode, LoraLoaderModelOnly, KSamplerSelect, BasicScheduler, Note, SaveImage, PlaySound|pysssss, Note, VAELoader, EmptySD3LatentImage, String Literal, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, ConditioningCombine, UNETLoader, Reroute]
patterns: []
missing: [Int Literal, Int Literal, PlaySound|pysssss, String Literal]
discoveries: [次要节点 `Int Literal` 知识库中没有该节点类型的任何知识, 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json

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

覆盖率 **66%**（19/29）

**有卡**：`VAEDecode`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`FluxGuidance`、`FluxForwardOverrider`、`ApplyTeaCachePatch`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`KSamplerSelect`、`BasicScheduler`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`DualCLIPLoader`、`CLIPTextEncode`、`ConditioningCombine`、`UNETLoader`

**缺卡**（4）：`Int Literal`、`Int Literal`、`PlaySound|pysssss`、`String Literal`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `Int Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
