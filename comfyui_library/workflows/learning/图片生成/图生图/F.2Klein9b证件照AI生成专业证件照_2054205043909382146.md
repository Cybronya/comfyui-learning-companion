---
key: 图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json
name: F.2Klein9b证件照AI生成专业证件照_2054205043909382146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json
hash: 89405e530a5296de
coverage: 0.964286
learned_at: 2026-10-23 10:52:43
nodes: [KSamplerSelect, VAELoader, CFGGuider, CLIPLoader, UNETLoader, RandomNoise, SamplerCustomAdvanced, VAEEncode, CLIPTextEncode, VAEDecode, ImageScaleToTotalPixels, BasicScheduler, ReferenceLatent, ConditioningZeroOut, EmptyFlux2LatentImage, SaveImage, Int, Int, easy promptConcat, easy showAnything, LoraLoaderModelOnly, easy promptConcat, CR Text, CR Text, CR Text, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `KSamplerSelect` ★核心
- `VAELoader`
- `CFGGuider`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `BasicScheduler`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `Int`
- `Int`
- `easy promptConcat`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `easy promptConcat`
- `CR Text`
- `CR Text`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`KSamplerSelect`、`VAELoader`、`CFGGuider`、`CLIPLoader`、`UNETLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`ImageScaleToTotalPixels`、`BasicScheduler`、`ReferenceLatent`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`SaveImage`、`Int`、`easy promptConcat`、`LoraLoaderModelOnly`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
