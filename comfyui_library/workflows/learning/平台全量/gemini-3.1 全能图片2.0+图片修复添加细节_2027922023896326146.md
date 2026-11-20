---
key: 平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json
name: gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json
hash: d4d89e0ab2c2556f
coverage: 0.9
learned_at: 2026-11-14 01:12:14
nodes: [RH_Nano_Banana2_Gemini31Flash, Repeater|pysssss, KSamplerSelect, CFGGuider, CLIPLoader, GrowMaskWithBlur, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, ConditioningZeroOut, Flux2Scheduler, VAEDecode, VAELoader, VAEEncode, ReferenceLatent, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, DifferentialDiffusion, UNETLoader, CR Text, SaveImage, LoraLoaderModelOnly, Image Comparer (rgthree), LoadImage, MuyeTextEditOutput, SaveImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
---

# 平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json

> 来源文件 `comfyui_library/workflows/平台全量/gemini-3.1 全能图片2.0+图片修复添加细节_2027922023896326146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `RH_Nano_Banana2_Gemini31Flash`
- `Repeater|pysssss`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPLoader`
- `GrowMaskWithBlur`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `CR Text`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `MuyeTextEditOutput`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`RH_Nano_Banana2_Gemini31Flash`、`Repeater|pysssss`、`KSamplerSelect`、`CFGGuider`、`CLIPLoader`、`GrowMaskWithBlur`、`EmptyFlux2LatentImage`、`RandomNoise`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`Flux2Scheduler`、`VAEDecode`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`DifferentialDiffusion`、`UNETLoader`、`CR Text`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`MuyeTextEditOutput`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、SaveImage
