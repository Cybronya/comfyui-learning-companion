---
key: 数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json
name: Qwen Image2.1 全能_2102320159447937026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json
hash: 70b288272cb82b42
coverage: 0.630435
learned_at: 2026-10-19 00:19:13
nodes: [PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, StringConcatenate, StringConcatenate, StringConcatenate, PrimitiveBoolean, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, StringConcatenate, CLIPLoader, TextGenerate, RegexExtract, JsonExtractString, RegexMatch, ComfySwitchNode, ComfySwitchNode, StringCompare, ComfySwitchNode, ComfySwitchNode, VAELoader, EmptyLatentImage, KSampler, SaveImageAdvanced, SaveImage, JsonExtractString, StringCompare, ComfySwitchNode, MarkdownNote, UNETLoader, CLIPLoader, VAEDecode, PreviewImage, RegexMatch, PrimitiveStringMultiline, TextEncodeQwenImage21, PrimitiveInt, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, LoadImage, ComfyMathExpression, ComfySwitchNode, PrimitiveBoolean, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1088}
---

# 数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（92 个）：
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `StringConcatenate`
- `StringConcatenate`
- `CLIPLoader`
- `TextGenerate`
- `RegexExtract`
- `JsonExtractString`
- `RegexMatch`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `RegexMatch`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `LoadImage`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（58/92）

**有卡**：`StringConcatenate`、`PrimitiveBoolean`、`CLIPLoader`、`TextGenerate`、`RegexExtract`、`JsonExtractString`、`RegexMatch`、`StringCompare`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`SaveImageAdvanced`、`SaveImage`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`ComfyMathExpression`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
