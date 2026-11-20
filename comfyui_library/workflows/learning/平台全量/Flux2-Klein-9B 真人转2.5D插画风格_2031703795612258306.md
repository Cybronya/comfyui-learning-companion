---
key: 平台全量/Flux2-Klein-9B 真人转2.5D插画风格_2031703795612258306.json
name: Flux2-Klein-9B 真人转2.5D插画风格_2031703795612258306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux2-Klein-9B 真人转2.5D插画风格_2031703795612258306.json
hash: 14561084b3ffbe69
coverage: 0.810811
learned_at: 2026-11-14 00:29:28
nodes: [CLIPLoader, VAELoader, Flux2Scheduler, CFGGuider, KSamplerSelect, EmptyFlux2LatentImage, Reroute, Reroute, Image Comparer (rgthree), LoadImage, ReferenceLatent, LoadImage, LoadImage, LoadImage, RandomNoise, ConditioningZeroOut, LoadImage, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, Reroute, Reroute, ReferenceLatent, VAEEncode, LoadImage, LoadImage, PreviewAny, RH_Captioner_Pro, VAEDecode, SamplerCustomAdvanced, SaveImage, LoraLoaderModelOnly, MuyeTextEditOutput, MultiTextConcatenate, PreviewImage, ImageConcanate]
patterns: []
missing: []
---

# 平台全量/Flux2-Klein-9B 真人转2.5D插画风格_2031703795612258306.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux2-Klein-9B 真人转2.5D插画风格_2031703795612258306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `Flux2Scheduler`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `ConditioningZeroOut`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `RH_Captioner_Pro`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `MuyeTextEditOutput`
- `MultiTextConcatenate`
- `PreviewImage`
- `ImageConcanate`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`CLIPLoader`、`VAELoader`、`Flux2Scheduler`、`CFGGuider`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`LoadImage`、`ReferenceLatent`、`RandomNoise`、`ConditioningZeroOut`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`VAEEncode`、`RH_Captioner_Pro`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`MuyeTextEditOutput`、`MultiTextConcatenate`、`ImageConcanate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、SaveImage
