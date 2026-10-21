---
key: 图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json
name: Qwen Image2.1文生图_2107782937193308162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json
hash: 37e16c994c7ba0a6
coverage: 0.904762
learned_at: 2026-10-20 01:51:05
nodes: [CLIPLoader, VAELoader, ResolutionSelector, RegexExtract, ComfySwitchNode, UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, JsonExtractString, StringCompare, KSampler, SaveImage, TextEncodeQwenImage21, SaveImageAdvanced, PreviewAny, TextGenerate, Text, Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `RegexExtract`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `JsonExtractString`
- `StringCompare`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `PreviewAny`
- `TextGenerate`
- `Text`
- `Text`
- `LoadImage`
- `LoadImage`

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

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`RegexExtract`、`UNETLoader`、`EmptyLatentImage`、`VAEDecode`、`JsonExtractString`、`StringCompare`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`TextGenerate`、`Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
