---
key: 图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json
name: Qwen2.1文生图PE增强【已清理think】_2101861743575261186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json
hash: 5fb32cdf270cd418
coverage: 0.833333
learned_at: 2026-10-20 01:51:22
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, StringConstantMultiline, StringReplace, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, CLIPLoader, ResolutionSelector, PreviewAny, Note, StringConstantMultiline, TextGenerate, easy showAnything, StringFunction|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图PE增强【已清理think】_2101861743575261186.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `StringConstantMultiline`
- `StringReplace`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `ResolutionSelector`
- `PreviewAny`
- `Note`
- `StringConstantMultiline`
- `TextGenerate`
- `easy showAnything`
- `StringFunction|pysssss`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`StringConstantMultiline`、`StringReplace`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`TextGenerate`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
