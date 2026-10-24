---
key: 图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json
name: Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json
hash: 0f000ffb5ef81e21
coverage: 0.756757
learned_at: 2026-10-23 10:59:21
nodes: [VAELoader, UNETLoader, CLIPLoader, VAEEncode, ConditioningZeroOut, ReferenceLatent, Flux2Scheduler, KSamplerSelect, CFGGuider, GetImageSize, ImageScaleToTotalPixels, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, QwenMultiangleCameraNode, ReferenceLatent, KepStringList, CR Text Concatenate, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), QwenMultiangleCameraNode, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Image Comparer (rgthree), LoadImage, VAEDecode, SaveImage, QwenMultiangleCameraNode, Note, CR Prompt Text, Note, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `QwenMultiangleCameraNode`
- `ReferenceLatent`
- `KepStringList`
- `CR Text Concatenate`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `QwenMultiangleCameraNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `QwenMultiangleCameraNode`
- `Note`
- `CR Prompt Text`
- `Note`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`GetImageSize`、`ImageScaleToTotalPixels`、`QwenMultiangleCameraNode`、`KepStringList`、`CR Text Concatenate`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`LoadImage`、`VAEDecode`、`SaveImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
