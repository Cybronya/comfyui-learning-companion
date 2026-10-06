---
key: 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json
name: Qwen Image2.1文生图_2103745897376079874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json
hash: 1368ce4b5a27c155
coverage: 0.888889
learned_at: 2026-10-07 02:23:37
nodes: [CLIPLoader, VAELoader, TextGenerate, RegexExtract, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, PreviewAny, JsonExtractString, StringCompare, KSampler, SaveImage, TextEncodeQwenImage21, Text, SaveImageAdvanced, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2103745897376079874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `TextGenerate`
- `RegexExtract`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `JsonExtractString`
- `StringCompare`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `Text`
- `SaveImageAdvanced`
- `ResolutionSelector`

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

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`VAELoader`、`TextGenerate`、`RegexExtract`、`UNETLoader`、`EmptyLatentImage`、`VAEDecode`、`JsonExtractString`、`StringCompare`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`Text`、`SaveImageAdvanced`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
