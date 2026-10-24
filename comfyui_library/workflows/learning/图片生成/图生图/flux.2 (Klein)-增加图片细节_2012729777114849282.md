---
key: 图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json
name: flux.2 (Klein)-增加图片细节_2012729777114849282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json
hash: 1b03aa5d6d52f802
coverage: 0.857143
learned_at: 2026-10-23 11:35:51
nodes: [ImpactInt, SetNode, SimpleMath+, ResizeImageMixlab, VAEEncode, CLIPTextEncode, VAEEncode, VAEDecode, PreviewImage, LoraLoaderModelOnly, SimpleMath+, easy imageSize, EasyCache, LyingSigmaSampler, ReferenceLatent, FluxGuidance, SamplerCustomAdvanced, ConditioningZeroOut, CFGGuider, GetNode, Image Comparer (rgthree), KSamplerSelect, KSamplerSelect, CR Text, DiffusionModelLoaderKJ, CLIPLoader, VAELoader, LoadImage, Note, ImpactInt, SaveImage, BasicScheduler, KSamplerSelect, ColorMatch, RandomNoise]
patterns: []
missing: []
---

# 图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ImpactInt`
- `SetNode`
- `SimpleMath+`
- `ResizeImageMixlab`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `easy imageSize`
- `EasyCache`
- `LyingSigmaSampler` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CR Text`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `Note`
- `ImpactInt`
- `SaveImage`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ColorMatch`
- `RandomNoise`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`ImpactInt`、`SimpleMath+`、`ResizeImageMixlab`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`easy imageSize`、`EasyCache`、`LyingSigmaSampler`、`ReferenceLatent`、`FluxGuidance`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`CR Text`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`、`BasicScheduler`、`ColorMatch`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
