---
key: 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json
name: Qwen Image2.1文生图_2103745897376079874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json
hash: 1368ce4b5a27c155
coverage: 0.888889
learned_at: 2026-10-10 21:27:49
nodes: [CLIPLoader, VAELoader, TextGenerate, RegexExtract, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, PreviewAny, JsonExtractString, StringCompare, KSampler, SaveImage, TextEncodeQwenImage21, Text, SaveImageAdvanced, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json`

## 结构

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `TextGenerate`
- `RegexExtract`
- `ComfySwitchNode`
- `UNETLoader`
- `CLIPLoader`
- `EmptyLatentImage`
- `VAEDecode`
- `PreviewAny`
- `JsonExtractString`
- `StringCompare`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `Text`
- `SaveImageAdvanced`
- `ResolutionSelector`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `42`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`VAELoader`、`TextGenerate`、`RegexExtract`、`ComfySwitchNode`、`UNETLoader`、`EmptyLatentImage`、`VAEDecode`、`PreviewAny`、`JsonExtractString`、`StringCompare`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`Text`
