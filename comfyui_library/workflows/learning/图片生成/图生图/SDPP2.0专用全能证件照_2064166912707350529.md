---
key: 图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json
name: SDPP2.0专用全能证件照_2064166912707350529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json
hash: eea94872c2b2c048
coverage: 0.903226
learned_at: 2026-10-21 00:44:16
nodes: [KSamplerSelect, VAELoader, CFGGuider, RandomNoise, CLIPTextEncode, BasicScheduler, ConditioningZeroOut, ReferenceLatent, VAEEncode, CLIPLoader, VAEDecode, EmptyFlux2LatentImage, Int, Int, BiRefNet_Hugo, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustomAdvanced, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, PrimitiveNode, easy imageRemBg, RH_RhartImageG2ImageToImage, SaveImage, PreviewImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `KSamplerSelect` ★核心
- `VAELoader`
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `Int`
- `Int`
- `BiRefNet_Hugo`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `easy imageRemBg`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `PreviewImage`
- `CR Prompt Text`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`KSamplerSelect`、`VAELoader`、`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`BasicScheduler`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`CLIPLoader`、`VAEDecode`、`EmptyFlux2LatentImage`、`Int`、`BiRefNet_Hugo`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoadImage`、`easy imageRemBg`、`RH_RhartImageG2ImageToImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
