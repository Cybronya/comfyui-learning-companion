---
key: 图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json
name: Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json
hash: 2dc366b528e9fc35
coverage: 0.68
learned_at: 2026-10-07 02:23:51
nodes: [MarkdownNote, Note, UNETLoader, TextEncodeQwenImage21, VAELoader, EmptyLatentImage, CLIPLoader, PrimitiveStringMultiline, RegexExtract, StringConcatenate, SeedVR2LoadVAEModel, SaveImage, SaveImageAdvanced, VAEDecode, SetNode, SeedVR2VideoUpscaler, GetNode, TextGenerate, PreviewAny, KSampler, SeedVR2LoadDiTModel, SaveImage, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 537375866660005, "steps": 25, "width": 1024}
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

覆盖率 **68%**（17/25）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`RegexExtract`、`StringConcatenate`、`SeedVR2LoadVAEModel`、`SaveImage`、`SaveImageAdvanced`、`VAEDecode`、`SeedVR2VideoUpscaler`、`TextGenerate`、`KSampler`、`SeedVR2LoadDiTModel`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
