---
key: 图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json
name: 【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json
hash: 93e9fbdfc38601c6
coverage: 0.8125
learned_at: 2026-10-19 20:34:29
nodes: [UNETLoader, easy cleanGpuUsed, easy cleanGpuUsed, VAELoader, Anything Everywhere, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ImageCASharpening+, VAEDecode, ColorCorrectOfUtils, UNETLoader, Note, KSamplerAdvanced, KSamplerAdvanced, CR Seed, CLIPTextEncode, CLIPTextEncode, Note, FluxResolutionNode, RHHiddenNodes, Note, EmptyLatentImage, Anything Everywhere, Note, LoadImage, SaveImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 16, "denoise": "bong_tangent", "height": 512, "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 512}
---

# 图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAELoader`
- `Anything Everywhere`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ImageCASharpening+`
- `VAEDecode` ★核心
- `ColorCorrectOfUtils`
- `UNETLoader` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CR Seed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `FluxResolutionNode`
- `RHHiddenNodes`
- `Note`
- `EmptyLatentImage` ★核心
- `Anything Everywhere`
- `Note`
- `LoadImage`
- `SaveImage`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `16`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `bong_tangent`
- `width` = `512`
- `height` = `512`
- `batch_size` = `4`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`UNETLoader`、`easy cleanGpuUsed`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ImageCASharpening+`、`VAEDecode`、`ColorCorrectOfUtils`、`KSamplerAdvanced`、`CR Seed`、`CLIPTextEncode`、`FluxResolutionNode`、`RHHiddenNodes`、`EmptyLatentImage`、`LoadImage`、`SaveImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
