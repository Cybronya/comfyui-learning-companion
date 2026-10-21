---
key: 图片生成/文生图/文生图-图像编辑-FLUX.2-klein-_2034521906816225282.json
name: 文生图-图像编辑-FLUX.2-klein-_2034521906816225282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-图像编辑-FLUX.2-klein-_2034521906816225282.json
hash: 8d4e70ce47f8f152
coverage: 0.919355
learned_at: 2026-10-21 03:00:37
nodes: [Flux2Scheduler, ModelPatchTorchSettings, CLIPLoader, VAELoader, UNETLoader, VAEDecode, RandomNoise, LoadImage, LoadImage, LoadImage, VAEEncode, ReferenceLatent, easy boolean, easy boolean, easy boolean, easy int, easy int, easy int, Image Comparer (rgthree), VAEEncode, VAEEncode, Bjornulf_IfElse, Bjornulf_IfElse, ReferenceLatent, LazySwitch1way, ConditioningZeroOut, GetImageSize, KSamplerSelect, CLIPTextEncode, Bjornulf_IfElse, ReferenceLatent, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PreviewAny, LazySwitch1way, SaveImage, easy boolean, Note, RH_LLMAPI_NODE, Note, CR Text, LazySwitch2way, LazySwitch1way, ReferenceLatent, LazySwitch1way, LazySwitch1way, CFGGuider, SamplerCustomAdvanced, InpaintModelConditioning, LazySwitch1way, LazySwitch2way, EmptyFlux2LatentImage, GrowMaskWithBlur, Note, easy boolean, CR Text, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ]
patterns: []
missing: []
---

# 图片生成/文生图/文生图-图像编辑-FLUX.2-klein-_2034521906816225282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-图像编辑-FLUX.2-klein-_2034521906816225282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `Flux2Scheduler`
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `easy boolean`
- `easy boolean`
- `easy boolean`
- `easy int`
- `easy int`
- `easy int`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `Bjornulf_IfElse`
- `Bjornulf_IfElse`
- `ReferenceLatent`
- `LazySwitch1way`
- `ConditioningZeroOut`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Bjornulf_IfElse`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `PreviewAny`
- `LazySwitch1way`
- `SaveImage`
- `easy boolean`
- `Note`
- `RH_LLMAPI_NODE`
- `Note`
- `CR Text`
- `LazySwitch2way`
- `LazySwitch1way`
- `ReferenceLatent`
- `LazySwitch1way`
- `LazySwitch1way`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `InpaintModelConditioning`
- `LazySwitch1way`
- `LazySwitch2way`
- `EmptyFlux2LatentImage`
- `GrowMaskWithBlur`
- `Note`
- `easy boolean`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`

## 知识

覆盖率 **92%**（57/62）

**有卡**：`Flux2Scheduler`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`RandomNoise`、`LoadImage`、`VAEEncode`、`ReferenceLatent`、`easy boolean`、`easy int`、`Bjornulf_IfElse`、`LazySwitch1way`、`ConditioningZeroOut`、`GetImageSize`、`KSamplerSelect`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`SaveImage`、`RH_LLMAPI_NODE`、`CR Text`、`LazySwitch2way`、`CFGGuider`、`SamplerCustomAdvanced`、`InpaintModelConditioning`、`EmptyFlux2LatentImage`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
