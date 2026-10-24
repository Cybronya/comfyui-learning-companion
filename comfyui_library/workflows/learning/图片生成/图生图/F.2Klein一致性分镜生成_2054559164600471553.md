---
key: 图片生成/图生图/F.2Klein一致性分镜生成_2054559164600471553.json
name: F.2Klein一致性分镜生成_2054559164600471553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein一致性分镜生成_2054559164600471553.json
hash: 1043483acb921498
coverage: 0.965517
learned_at: 2026-10-23 10:52:45
nodes: [Flux2Scheduler, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, ConditioningZeroOut, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, RandomNoise, VAEDecode, INTConstant, INTConstant, GetImageSize, EmptyFlux2LatentImage, CR Prompt Text, Text Multiline, LoadImage, CLIPLoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, StringConcatenate, Qwen3_VQA, easy showAnything, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2, Int, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein一致性分镜生成_2054559164600471553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein一致性分镜生成_2054559164600471553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `CR Prompt Text`
- `Text Multiline`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `StringConcatenate`
- `Qwen3_VQA`
- `easy showAnything`
- `easy promptLine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `SaveImage`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`VAEDecode`、`INTConstant`、`GetImageSize`、`EmptyFlux2LatentImage`、`CR Prompt Text`、`Text Multiline`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`StringConcatenate`、`Qwen3_VQA`、`easy promptLine`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
