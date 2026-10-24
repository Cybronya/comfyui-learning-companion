---
key: 图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json
name: 【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json
hash: a89cf8a3e13b38c6
coverage: 0.885714
learned_at: 2026-10-23 11:49:03
nodes: [UNETLoader, easy cleanGpuUsed, easy cleanGpuUsed, VAELoader, Anything Everywhere, Anything Everywhere, MathExpression|pysssss, MathExpression|pysssss, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, ImageCASharpening+, CR Text, VAEDecode, SaveImage, ColorCorrectOfUtils, CLIPTextEncode, MathExpression|pysssss, MathExpression|pysssss, RHHiddenNodes, FluxResolutionNode, ImageResize+, PreviewImage, VAEEncode, CR Seed, KSamplerAdvanced, UNETLoader, KSamplerAdvanced, Note, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "bong_tangent", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ImageCASharpening+`
- `CR Text`
- `VAEDecode` ★核心
- `SaveImage`
- `ColorCorrectOfUtils`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `FluxResolutionNode`
- `ImageResize+`
- `PreviewImage`
- `VAEEncode` ★核心
- `CR Seed`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `16`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`UNETLoader`、`easy cleanGpuUsed`、`VAELoader`、`MathExpression|pysssss`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`ImageCASharpening+`、`CR Text`、`VAEDecode`、`SaveImage`、`ColorCorrectOfUtils`、`RHHiddenNodes`、`FluxResolutionNode`、`ImageResize+`、`VAEEncode`、`CR Seed`、`KSamplerAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced
