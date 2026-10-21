---
key: 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json
name: Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json
hash: ae739be665973d15
coverage: 0.822222
learned_at: 2026-10-21 00:43:14
nodes: [MarkdownNote, QwenImage21Cache, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, SamplerCustomAdvanced, ResolutionSelector, VAELoader, Reroute, Reroute, SeedNode, MathExpression|pysssss, BasicGuider, VAEDecode, StringFormat, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, TextEncodeQwenImage21, EmptyLatentImage, UNETLoader, UNETLoader, CR Model Input Switch, StringToInt, CLIPLoader, SaveImage, LoadImage, LoadImage, LoadImage, CLIPLoader, BatchImagesNode, PrimitiveStringMultiline, StringFormat, PrimitiveStringMultiline, TextGenerate, JsonExtractString, easy showAnything, ShowText|pysssss, ImageConcatMulti, ImageConcatMulti, ImageConcanate, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma_三图编辑6步快速出图_2105184881469911042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `MarkdownNote`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `VAELoader`
- `Reroute`
- `Reroute`
- `SeedNode`
- `MathExpression|pysssss`
- `BasicGuider`
- `VAEDecode` ★核心
- `StringFormat`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Model Input Switch`
- `StringToInt`
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `BatchImagesNode`
- `PrimitiveStringMultiline`
- `StringFormat`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `JsonExtractString`
- `easy showAnything`
- `ShowText|pysssss`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcanate`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`QwenImage21Cache`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`ResolutionSelector`、`VAELoader`、`SeedNode`、`MathExpression|pysssss`、`BasicGuider`、`VAEDecode`、`StringFormat`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`UNETLoader`、`CR Model Input Switch`、`StringToInt`、`CLIPLoader`、`SaveImage`、`LoadImage`、`BatchImagesNode`、`TextGenerate`、`JsonExtractString`、`ImageConcatMulti`、`ImageConcanate`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
