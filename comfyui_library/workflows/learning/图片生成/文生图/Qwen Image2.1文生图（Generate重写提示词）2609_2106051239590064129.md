---
key: 图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json
name: Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json
hash: 2dc366b528e9fc35
coverage: 0.4
learned_at: 2026-10-06 21:49:44
nodes: [MarkdownNote, Note, UNETLoader, TextEncodeQwenImage21, VAELoader, EmptyLatentImage, CLIPLoader, PrimitiveStringMultiline, RegexExtract, StringConcatenate, SeedVR2LoadVAEModel, SaveImage, SaveImageAdvanced, VAEDecode, SetNode, SeedVR2VideoUpscaler, GetNode, TextGenerate, PreviewAny, KSampler, SeedVR2LoadDiTModel, SaveImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), ResolutionSelector]
patterns: []
missing: [Fast Groups Bypasser (rgthree), RegexExtract, StringConcatenate, TextGenerate, PreviewAny, SaveImageAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 537375866660005, "steps": 25, "width": 1024}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `RegexExtract` 知识库中没有该节点类型的任何知识, 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `StringConcatenate`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SetNode`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `TextGenerate`
- `PreviewAny`
- `KSampler` ★核心
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `537375866660005`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（10/25）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`SaveImage`、`VAEDecode`、`KSampler`、`ResolutionSelector`

**缺卡**（9）：`Fast Groups Bypasser (rgthree)`、`RegexExtract`、`StringConcatenate`、`TextGenerate`、`PreviewAny`、`SaveImageAdvanced`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexExtract` 知识库中没有该节点类型的任何知识
- 次要节点 `StringConcatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
