---
key: 图片生成/图生图/flux.2单图编辑_2013969319683690498.json
name: flux.2单图编辑_2013969319683690498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2单图编辑_2013969319683690498.json
hash: c21ba1617145ffa1
coverage: 0.909091
learned_at: 2026-10-23 11:35:55
nodes: [SetNode, SimpleMath+, VAEEncode, CLIPTextEncode, VAEEncode, ReferenceLatent, SamplerCustomAdvanced, FluxGuidance, ConditioningZeroOut, easy imageSize, CR Text, CFGGuider, easy imageSize, GetNode, ResizeImageMixlab, SimpleMath+, RandomNoise, EasyCache, KSamplerSelect, KSamplerSelect, Note, ImpactInt, KSamplerSelect, BasicScheduler, PathchSageAttentionKJ, LoraLoaderModelOnly, LoadImage, ImpactInt, VAELoader, CLIPLoader, GGUFLoaderKJ, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/flux.2单图编辑_2013969319683690498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2单图编辑_2013969319683690498.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `SetNode`
- `SimpleMath+`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `easy imageSize`
- `CR Text`
- `CFGGuider`
- `easy imageSize`
- `GetNode`
- `ResizeImageMixlab`
- `SimpleMath+`
- `RandomNoise`
- `EasyCache`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `Note`
- `ImpactInt`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImpactInt`
- `VAELoader`
- `CLIPLoader`
- `GGUFLoaderKJ`
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`SimpleMath+`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`SamplerCustomAdvanced`、`FluxGuidance`、`ConditioningZeroOut`、`easy imageSize`、`CR Text`、`CFGGuider`、`ResizeImageMixlab`、`RandomNoise`、`EasyCache`、`KSamplerSelect`、`ImpactInt`、`BasicScheduler`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`、`VAELoader`、`CLIPLoader`、`GGUFLoaderKJ`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
