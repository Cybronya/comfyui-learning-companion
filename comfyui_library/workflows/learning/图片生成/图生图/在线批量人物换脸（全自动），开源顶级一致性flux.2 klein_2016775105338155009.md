---
key: 图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json
name: 在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json
hash: b402fc8e9576fd29
coverage: 0.942857
learned_at: 2026-10-23 12:44:16
nodes: [KSamplerSelect, Flux2Scheduler, VAEEncode, SamplerCustomAdvanced, Get Image Size, CLIPLoader, VAEEncode, CFGGuider, RandomNoise, SaveImage, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAELoader, CLIPTextEncode, VAEDecode, InvertMask, ImageCropByMask, ColorToMask_UTK, RH_ExtractImage, RHBatchImages:, easy imageCount, easy forLoopEnd, easy batchAnything, LoadImage, EmptyFlux2LatentImage, ReferenceLatent, UNETLoader, LoraLoaderModelOnly, LoadImage, RHHiddenNodes, easy forLoopStart, easy showAnything, RHUploadZip, Note]
patterns: []
missing: []
---

# 图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/在线批量人物换脸（全自动），开源顶级一致性flux.2 klein_2016775105338155009.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Get Image Size`
- `CLIPLoader`
- `VAEEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `SaveImage`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `InvertMask`
- `ImageCropByMask`
- `ColorToMask_UTK`
- `RH_ExtractImage`
- `RHBatchImages:`
- `easy imageCount`
- `easy forLoopEnd`
- `easy batchAnything`
- `LoadImage`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RHHiddenNodes`
- `easy forLoopStart`
- `easy showAnything`
- `RHUploadZip`
- `Note`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`VAEEncode`、`SamplerCustomAdvanced`、`Get Image Size`、`CLIPLoader`、`CFGGuider`、`RandomNoise`、`SaveImage`、`ConditioningZeroOut`、`ReferenceLatent`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`InvertMask`、`ImageCropByMask`、`ColorToMask_UTK`、`RH_ExtractImage`、`RHBatchImages:`、`easy imageCount`、`easy forLoopEnd`、`easy batchAnything`、`LoadImage`、`EmptyFlux2LatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`RHHiddenNodes`、`easy forLoopStart`、`RHUploadZip`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
