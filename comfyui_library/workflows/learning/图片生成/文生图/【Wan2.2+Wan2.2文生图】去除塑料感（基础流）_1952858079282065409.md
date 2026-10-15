---
key: 图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json
name: 【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json
hash: 8d381031d935a595
coverage: 0.6
learned_at: 2026-10-10 20:59:30
nodes: [UNETLoader, easy cleanGpuUsed, UNETLoader, easy cleanGpuUsed, VAELoader, Anything Everywhere, Anything Everywhere, MathExpression|pysssss, EmptyLatentImage, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CR Seed, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, RH_Prompter, ShowText|pysssss, CR Text Concatenate, RHHiddenNodes, ImageCASharpening+, CR Text, CR Text, FluxResolutionNode, VAEDecode, SaveImage, KSamplerAdvanced, KSamplerAdvanced, ColorCorrectOfUtils]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, CR Seed]
parameters: {"batch_size": 1, "cfg": 16, "denoise": "bong_tangent", "height": 1216, "sampler_name": 2, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 840}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json`

## 结构

**节点**（35 个）：
- `UNETLoader`
- `easy cleanGpuUsed`
- `UNETLoader`
- `easy cleanGpuUsed`
- `VAELoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `MathExpression|pysssss`
- `EmptyLatentImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `CR Seed`
- `PathchSageAttentionKJ`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `RH_Prompter`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `RHHiddenNodes`
- `ImageCASharpening+`
- `CR Text`
- `CR Text`
- `FluxResolutionNode`
- `VAEDecode`
- `SaveImage`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `ColorCorrectOfUtils`

## 关键参数

- `batch_size` = `1`
- `cfg` = `16`
- `denoise` = `bong_tangent`
- `height` = `1216`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `fixed`
- `width` = `840`

## 知识

覆盖率 **60%**（21/35）

**有卡**：`UNETLoader`、`easy cleanGpuUsed`、`VAELoader`、`Anything Everywhere`、`MathExpression|pysssss`、`EmptyLatentImage`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CR Seed`、`CLIPTextEncode`

**缺卡**（11）：`CR Text`、`CR Text`、`CR Text Concatenate`、`ImageCASharpening+`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Seed`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
