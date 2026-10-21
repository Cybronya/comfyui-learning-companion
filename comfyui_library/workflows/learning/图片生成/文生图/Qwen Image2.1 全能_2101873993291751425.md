---
key: 图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json
name: Qwen Image2.1 全能_2101873993291751425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json
hash: 12551dee90774fd0
coverage: 0.619048
learned_at: 2026-10-20 01:51:04
nodes: [PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, StringConcatenate, StringConcatenate, StringConcatenate, PrimitiveBoolean, PrimitiveBoolean, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, StringConcatenate, CLIPLoader, TextGenerate, RegexExtract, JsonExtractString, RegexMatch, ComfySwitchNode, RegexMatch, ComfySwitchNode, PrimitiveStringMultiline, StringCompare, ComfySwitchNode, ComfySwitchNode, VAELoader, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, KSampler, VAEDecode, PreviewImage, SaveImageAdvanced, SaveImage, JsonExtractString, StringCompare, ComfySwitchNode, MarkdownNote, UNETLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
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
- `RegexMatch`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `StringCompare`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAELoader`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImageAdvanced`
- `SaveImage`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（26/42）

**有卡**：`StringConcatenate`、`PrimitiveBoolean`、`CLIPLoader`、`TextGenerate`、`RegexExtract`、`JsonExtractString`、`RegexMatch`、`StringCompare`、`VAELoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
