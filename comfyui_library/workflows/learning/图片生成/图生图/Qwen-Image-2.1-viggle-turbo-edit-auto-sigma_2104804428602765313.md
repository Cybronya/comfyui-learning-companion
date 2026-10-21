---
key: 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json
name: Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json
hash: 1104547469f5362b
coverage: 0.810811
learned_at: 2026-10-21 00:43:13
nodes: [MarkdownNote, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, PrimitiveStringMultiline, PrimitiveBoolean, PrimitiveStringMultiline, StringFormat, TextGenerate, JsonExtractString, StringCompare, ComfySwitchNode, ComfySwitchNode, PreviewAny, TextEncodeQwenImage21, BasicGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, BatchImagesNode, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, StringFormat, LoadImage, ResolutionSelector, EmptyLatentImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_2104804428602765313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `StringFormat`
- `TextGenerate`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BatchImagesNode`
- `QwenImage21Cache`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `StringFormat`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PrimitiveBoolean`、`StringFormat`、`TextGenerate`、`JsonExtractString`、`StringCompare`、`TextEncodeQwenImage21`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`BatchImagesNode`、`QwenImage21Cache`、`MathExpression|pysssss`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
