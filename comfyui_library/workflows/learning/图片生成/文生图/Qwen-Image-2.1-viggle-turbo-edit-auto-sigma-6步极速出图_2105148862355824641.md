---
key: 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json
name: Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json
hash: 3dd6c7f9da44f1ea
coverage: 0.658537
learned_at: 2026-10-07 02:24:50
nodes: [PrimitiveStringMultiline, MarkdownNote, CLIPLoader, CLIPLoader, PrimitiveBoolean, UNETLoader, UNETLoader, Model Input Switch, QwenImage21Cache, SeedNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, PreviewImage, VAEDecode, StringFormat, BasicGuider, TextGenerateLTX2Prompt, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, EmptyLatentImage, VAELoader, TextEncodeQwenImage21, Image Comparer (rgthree), LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), ResolutionSelector, SamplerCustomAdvanced, VAEDecode, SaveImage, PreviewImage, VAEDecode, SamplerCustomAdvanced, BasicGuider, Reroute, Reroute]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Model Input Switch]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 981118936264082, "steps": 25, "width": 1024}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Model Input Switch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-viggle-turbo-edit-auto-sigma-6步极速出图_2105148862355824641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Model Input Switch`
- `QwenImage21Cache`
- `SeedNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PreviewImage`
- `VAEDecode` ★核心
- `StringFormat`
- `BasicGuider`
- `TextGenerateLTX2Prompt`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `Reroute`
- `Reroute`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `981118936264082`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（27/41）

**有卡**：`CLIPLoader`、`PrimitiveBoolean`、`UNETLoader`、`QwenImage21Cache`、`SeedNode`、`VAEDecode`、`StringFormat`、`BasicGuider`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`EmptyLatentImage`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`ResolutionSelector`、`SamplerCustomAdvanced`、`SaveImage`

**缺卡**（6）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`Model Input Switch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Model Input Switch` 知识库中没有该节点类型的任何知识
