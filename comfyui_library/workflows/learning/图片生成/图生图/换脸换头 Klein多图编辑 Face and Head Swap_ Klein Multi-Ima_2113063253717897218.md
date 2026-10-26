---
key: 图片生成/图生图/换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218.json
name: 换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218.json
hash: 909864da755420f3
coverage: 0.962963
learned_at: 2026-10-26 22:06:07
nodes: [EmptyFlux2LatentImage, Flux2Scheduler, CFGGuider, RandomNoise, KSamplerSelect, UNETLoader, CLIPLoader, VAEEncode, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, CLIPTextEncode, ReferenceLatent, VAELoader, CLIPTextEncode, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, Int, LoadImage, SaveImage, Fast Groups Bypasser (rgthree), LoadImage, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `Int`
- `LoadImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`EmptyFlux2LatentImage`、`Flux2Scheduler`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`VAEEncode`、`ReferenceLatent`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`Int`、`LoadImage`、`SaveImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
