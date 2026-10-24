---
key: 图片生成/图生图/Flux.2：90年代港风风格化_2079049505210724353.json
name: Flux.2：90年代港风风格化_2079049505210724353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2：90年代港风风格化_2079049505210724353.json
hash: 0f5b1bed2c7a9f25
coverage: 1
learned_at: 2026-10-23 10:58:53
nodes: [KSamplerSelect, RandomNoise, SaveImage, VAELoader, CLIPLoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, Flux2Scheduler, SetUnionControlNetType, ControlNetLoader, VAEEncode, ImageScaleToTotalPixels, AIO_Preprocessor, ConditioningZeroOut, CFGGuider, GetImageSize, FluxUnionControlNetApply, ReferenceLatent, VAEDecode, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": "canny"}
---

# 图片生成/图生图/Flux.2：90年代港风风格化_2079049505210724353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2：90年代港风风格化_2079049505210724353.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `CFGGuider`
- `GetImageSize`
- `FluxUnionControlNetApply` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `controlnet_strength` = `canny`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`KSamplerSelect`、`RandomNoise`、`SaveImage`、`VAELoader`、`CLIPLoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`SetUnionControlNetType`、`ControlNetLoader`、`VAEEncode`、`ImageScaleToTotalPixels`、`AIO_Preprocessor`、`ConditioningZeroOut`、`CFGGuider`、`GetImageSize`、`FluxUnionControlNetApply`、`ReferenceLatent`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
