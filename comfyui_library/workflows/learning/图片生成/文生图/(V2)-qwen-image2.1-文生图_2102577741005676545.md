---
key: (V2)-qwen-image2.1-文生图_2102577741005676545.json
name: (V2)-qwen-image2.1-文生图_2102577741005676545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json
hash: c84c17f722fb4dc2
coverage: 0.722222
learned_at: 2026-10-10 21:24:02
nodes: [MarkdownNote, Note, UNETLoader, TextEncodeQwenImage21, VAELoader, EmptyLatentImage, PreviewAny, StringConcatenate, TextGenerate, VAEDecode, KSampler, SaveImage, SaveImageAdvanced, CLIPLoader, PrimitiveStringMultiline, ResolutionSelector, RegexExtract, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# (V2)-qwen-image2.1-文生图_2102577741005676545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `Note`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `PreviewAny`
- `StringConcatenate`
- `TextGenerate`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `RegexExtract`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`StringConcatenate`、`TextGenerate`、`VAEDecode`、`KSampler`、`SaveImage`、`SaveImageAdvanced`、`CLIPLoader`、`ResolutionSelector`、`RegexExtract`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
