---
key: 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json
name: Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json
hash: 6cbef2f25e306f87
coverage: 0.645161
learned_at: 2026-10-10 20:59:00
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, ResolutionSelector, EmptyLatentImage, PrimitiveBoolean, PrimitiveStringMultiline, StringFormat, TextGenerate, JsonExtractString, StringCompare, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, BasicGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, StringFormat, MathExpression|pysssss, MarkdownNote, PreviewAny, PrimitiveStringMultiline]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss]
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-t2i-auto-sigma_2104764845521461250.json`

## 结构

**节点**（31 个）：
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `StringFormat`
- `TextGenerate`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect`
- `ManualSigmas`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `SaveImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `StringFormat`
- `MathExpression|pysssss`
- `MarkdownNote`
- `PreviewAny`
- `PrimitiveStringMultiline`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1024`

## 知识

覆盖率 **65%**（20/31）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`PrimitiveBoolean`、`PrimitiveStringMultiline`、`StringFormat`、`TextGenerate`、`JsonExtractString`、`StringCompare`、`ComfySwitchNode`、`TextEncodeQwenImage21`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`

**缺卡**（5）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
