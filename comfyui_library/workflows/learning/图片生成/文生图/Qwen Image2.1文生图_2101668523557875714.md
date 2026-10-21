---
key: 图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json
name: Qwen Image2.1文生图_2101668523557875714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json
hash: 134d42b2b039c275
coverage: 0.842105
learned_at: 2026-10-20 01:51:05
nodes: [CLIPLoader, VAELoader, TextGenerate, ResolutionSelector, Text, RegexExtract, JsonExtractString, StringCompare, ComfySwitchNode, PreviewAny, MarkdownNote, UNETLoader, CLIPLoader, EmptyLatentImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `TextGenerate`
- `ResolutionSelector`
- `Text`
- `RegexExtract`
- `JsonExtractString`
- `StringCompare`
- `ComfySwitchNode`
- `PreviewAny`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

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

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`VAELoader`、`TextGenerate`、`ResolutionSelector`、`Text`、`RegexExtract`、`JsonExtractString`、`StringCompare`、`UNETLoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
