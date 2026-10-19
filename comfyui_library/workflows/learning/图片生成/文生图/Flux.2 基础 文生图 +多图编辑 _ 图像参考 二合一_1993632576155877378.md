---
key: 图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json
name: Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json
hash: a2657263d6bc6fe4
coverage: 0.64557
learned_at: 2026-10-19 21:32:32
nodes: [BasicGuider, KSamplerSelect, PrimitiveInt, GetNode, RandomNoise, SetNode, GetNode, GetNode, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, GetNode, GetNode, EmptyFlux2LatentImage, SamplerCustomAdvanced, FluxGuidance, SetNode, SetNode, SetNode, SetNode, easy imageRemBg, VAEDecode, PrimitiveInt, LoadImage, Note, SaveImage, easy seed, CLIPTextEncode, PrimitiveInt, PathchSageAttentionKJ, LoadImage, Flux2Scheduler, LoraLoaderModelOnly, EasyCache, CLIPLoader, VAELoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, ModelPatchTorchSettings, PreviewImage, Note, PreviewImage, FastCanvas, Note, PreviewImage, LoadImage, LoadImage, 孤海-图像与遮罩描边, FastCanvasTool, LoadImage, Note, LoadImage, Qwen3_VQA, PreviewAny, LoadImage, DrawMaskOnImage, LoadImage, AIO_Preprocessor, Note, JoinImageWithAlpha, easy imageRemBg, JoinImageWithAlpha, Note, PreviewImage, SaveImage, LoadImage, easy imageRemBg, easy imageRemBg, Text, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 基础 文生图 +多图编辑 _ 图像参考 二合一_1993632576155877378.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `GetNode`
- `GetNode`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetNode`
- `GetNode`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy imageRemBg`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `LoadImage`
- `Note`
- `SaveImage`
- `easy seed`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PathchSageAttentionKJ`
- `LoadImage`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `EasyCache`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `ModelPatchTorchSettings`
- `PreviewImage`
- `Note`
- `PreviewImage`
- `FastCanvas`
- `Note`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `孤海-图像与遮罩描边`
- `FastCanvasTool`
- `LoadImage`
- `Note`
- `LoadImage`
- `Qwen3_VQA`
- `PreviewAny`
- `LoadImage`
- `DrawMaskOnImage`
- `LoadImage`
- `AIO_Preprocessor`
- `Note`
- `JoinImageWithAlpha`
- `easy imageRemBg`
- `JoinImageWithAlpha`
- `Note`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `easy imageRemBg`
- `easy imageRemBg`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心

## 知识

覆盖率 **65%**（51/79）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`FluxGuidance`、`easy imageRemBg`、`VAEDecode`、`LoadImage`、`SaveImage`、`easy seed`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`EasyCache`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`FastCanvas`、`孤海-图像与遮罩描边`、`FastCanvasTool`、`Qwen3_VQA`、`DrawMaskOnImage`、`AIO_Preprocessor`、`JoinImageWithAlpha`、`Text`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
