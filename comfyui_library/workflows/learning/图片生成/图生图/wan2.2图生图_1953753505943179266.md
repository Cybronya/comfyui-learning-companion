---
key: 图片生成/图生图/wan2.2图生图_1953753505943179266.json
name: wan2.2图生图_1953753505943179266
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2图生图_1953753505943179266.json
hash: aae666db91b45435
coverage: 0.902439
learned_at: 2026-10-23 11:46:04
nodes: [VAELoader, Anything Everywhere, Anything Everywhere, MathExpression|pysssss, MathExpression|pysssss, CLIPLoader, MathExpression|pysssss, MathExpression|pysssss, FluxResolutionNode, easy cleanGpuUsed, Note, CR Seed, CR Text, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LayerUtility: GetImageSize, KSampler, CLIPTextEncode, CLIPTextEncode, KSampler, easy cleanGpuUsed, ImageCASharpening+, VAEDecode, VAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, ColorCorrectOfUtils, ImageResize+, PreviewImage, LoadImage, RH_Captioner, ttN concat, Text Multiline, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "bong_tangent", "seed": 538709716066401, "steps": 15}
---

# 图片生成/图生图/wan2.2图生图_1953753505943179266.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2图生图_1953753505943179266.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPLoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `FluxResolutionNode`
- `easy cleanGpuUsed`
- `Note`
- `CR Seed`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: GetImageSize`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `ImageCASharpening+`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ColorCorrectOfUtils`
- `ImageResize+`
- `PreviewImage`
- `LoadImage`
- `RH_Captioner`
- `ttN concat`
- `Text Multiline`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `538709716066401`
- `steps` = `15`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`VAELoader`、`MathExpression|pysssss`、`CLIPLoader`、`FluxResolutionNode`、`easy cleanGpuUsed`、`CR Seed`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LayerUtility: GetImageSize`、`KSampler`、`CLIPTextEncode`、`ImageCASharpening+`、`VAEDecode`、`VAEEncode`、`UNETLoader`、`ColorCorrectOfUtils`、`ImageResize+`、`LoadImage`、`RH_Captioner`、`ttN concat`、`Text Multiline`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
