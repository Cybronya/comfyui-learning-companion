---
key: 图片生成/图生图/F.2Klein一致性分镜生成_2057782704892112897.json
name: F.2Klein一致性分镜生成_2057782704892112897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein一致性分镜生成_2057782704892112897.json
hash: 8b41eadbf85b8ed9
coverage: 0.964286
learned_at: 2026-10-23 10:52:45
nodes: [Flux2Scheduler, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, ConditioningZeroOut, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, RandomNoise, VAEDecode, INTConstant, INTConstant, GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, CR Prompt Text, Text Multiline, LoadImage, CLIPLoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, SaveImage, StringConcatenate, Qwen3_VQA, easy showAnything, easy promptLine]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein一致性分镜生成_2057782704892112897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein一致性分镜生成_2057782704892112897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `CR Prompt Text`
- `Text Multiline`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `StringConcatenate`
- `Qwen3_VQA`
- `easy showAnything`
- `easy promptLine`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`VAEDecode`、`INTConstant`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`CR Prompt Text`、`Text Multiline`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`、`StringConcatenate`、`Qwen3_VQA`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
