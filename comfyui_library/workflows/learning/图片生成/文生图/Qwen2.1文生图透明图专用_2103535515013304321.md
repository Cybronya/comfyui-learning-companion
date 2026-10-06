---
key: 图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json
name: Qwen2.1文生图透明图专用_2103535515013304321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json
hash: b40b23946803306f
coverage: 0.933333
learned_at: 2026-10-07 02:28:28
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, StringConstantMultiline, TextEncodeQwenImage21, KSampler, VAEDecode, SaveImage, ResolutionSelector, Note, StringConcatenate, StringConstantMultiline, StringConcatenate, StringConstantMultiline, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 40, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图透明图专用_2103535515013304321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `StringConstantMultiline`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `Note`
- `StringConcatenate`
- `StringConstantMultiline`
- `StringConcatenate`
- `StringConstantMultiline`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `40`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`StringConstantMultiline`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`StringConcatenate`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
