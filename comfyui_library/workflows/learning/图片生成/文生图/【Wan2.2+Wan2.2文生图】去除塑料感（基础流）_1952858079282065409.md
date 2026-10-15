---
key: 图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json
name: 【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json
hash: 8d381031d935a595
coverage: 0.914286
learned_at: 2026-10-15 22:28:02
nodes: [UNETLoader, easy cleanGpuUsed, UNETLoader, easy cleanGpuUsed, VAELoader, Anything Everywhere, Anything Everywhere, MathExpression|pysssss, EmptyLatentImage, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CR Seed, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, RH_Prompter, ShowText|pysssss, CR Text Concatenate, RHHiddenNodes, ImageCASharpening+, CR Text, CR Text, FluxResolutionNode, VAEDecode, SaveImage, KSamplerAdvanced, KSamplerAdvanced, ColorCorrectOfUtils]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 16, "denoise": "bong_tangent", "height": 1216, "sampler_name": 2, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 840}
---

# 图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `EmptyLatentImage` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CR Seed`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_Prompter`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `RHHiddenNodes`
- `ImageCASharpening+`
- `CR Text`
- `CR Text`
- `FluxResolutionNode`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ColorCorrectOfUtils`

## 关键参数

- `width` = `840`
- `height` = `1216`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `16`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`UNETLoader`、`easy cleanGpuUsed`、`VAELoader`、`MathExpression|pysssss`、`EmptyLatentImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CR Seed`、`CLIPTextEncode`、`RH_Prompter`、`CR Text Concatenate`、`RHHiddenNodes`、`ImageCASharpening+`、`CR Text`、`FluxResolutionNode`、`VAEDecode`、`SaveImage`、`KSamplerAdvanced`、`ColorCorrectOfUtils`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、KSamplerAdvanced
