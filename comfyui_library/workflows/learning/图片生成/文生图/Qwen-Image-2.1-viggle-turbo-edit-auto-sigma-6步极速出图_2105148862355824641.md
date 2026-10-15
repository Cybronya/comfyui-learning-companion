---
key: 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json
name: Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json
hash: 3dd6c7f9da44f1ea
coverage: 0.658537
learned_at: 2026-10-10 20:59:00
nodes: [PrimitiveStringMultiline, MarkdownNote, CLIPLoader, CLIPLoader, PrimitiveBoolean, UNETLoader, UNETLoader, Model Input Switch, QwenImage21Cache, SeedNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, PreviewImage, VAEDecode, StringFormat, BasicGuider, TextGenerateLTX2Prompt, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, EmptyLatentImage, VAELoader, TextEncodeQwenImage21, Image Comparer (rgthree), LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), ResolutionSelector, SamplerCustomAdvanced, VAEDecode, SaveImage, PreviewImage, VAEDecode, SamplerCustomAdvanced, BasicGuider, Reroute, Reroute]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Model Input Switch]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 981118936264082, "steps": 25, "width": 1024}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Model Input Switch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json`

## 结构

**节点**（41 个）：
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `UNETLoader`
- `UNETLoader`
- `Model Input Switch`
- `QwenImage21Cache`
- `SeedNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PreviewImage`
- `VAEDecode`
- `StringFormat`
- `BasicGuider`
- `TextGenerateLTX2Prompt`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `KSamplerSelect`
- `ManualSigmas`
- `EmptyLatentImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly`
- `KSampler`
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `SaveImage`
- `PreviewImage`
- `VAEDecode`
- `SamplerCustomAdvanced`
- `BasicGuider`
- `Reroute`
- `Reroute`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `981118936264082`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **66%**（27/41）

**有卡**：`PrimitiveStringMultiline`、`MarkdownNote`、`CLIPLoader`、`PrimitiveBoolean`、`UNETLoader`、`Model Input Switch`、`QwenImage21Cache`、`SeedNode`、`MathExpression|pysssss`、`PreviewImage`、`VAEDecode`、`StringFormat`、`BasicGuider`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`EmptyLatentImage`、`VAELoader`、`TextEncodeQwenImage21`

**缺卡**（6）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Model Input Switch`

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Model Input Switch` 知识库中没有该节点类型的任何知识
