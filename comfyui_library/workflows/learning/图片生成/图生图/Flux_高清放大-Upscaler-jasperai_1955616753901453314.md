---
key: 图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json
name: Flux_高清放大-Upscaler-jasperai_1955616753901453314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json
hash: 8cf607d12fc79350
coverage: 0.931034
learned_at: 2026-10-23 11:01:51
nodes: [BasicGuider, ControlNetLoader, ResizeLongestToNode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAELoader, ConditioningCombine, ConditioningZeroOut, GetImageSize+, ImpactInt, ImageResize+, VAEEncode, RH_Captioner, Image Comparer (rgthree), SaveImage, CLIPTextEncode, ControlNetApplyAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, BasicScheduler, Note, RandomNoise, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux_高清放大-Upscaler-jasperai_1955616753901453314.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `BasicGuider`
- `ControlNetLoader`
- `ResizeLongestToNode`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningCombine`
- `ConditioningZeroOut`
- `GetImageSize+`
- `ImpactInt`
- `ImageResize+`
- `VAEEncode` ★核心
- `RH_Captioner`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Note`
- `RandomNoise`
- `LoadImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`BasicGuider`、`ControlNetLoader`、`ResizeLongestToNode`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ConditioningCombine`、`ConditioningZeroOut`、`GetImageSize+`、`ImpactInt`、`ImageResize+`、`VAEEncode`、`RH_Captioner`、`SaveImage`、`ControlNetApplyAdvanced`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、ControlNetApplyAdvanced
