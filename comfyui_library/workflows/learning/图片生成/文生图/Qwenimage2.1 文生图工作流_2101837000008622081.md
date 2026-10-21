---
key: 图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json
name: Qwenimage2.1 文生图工作流_2101837000008622081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json
hash: 99e83b7f1fc3da88
coverage: 0.866667
learned_at: 2026-10-20 01:51:28
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImage21, TextGenerateLTX2Prompt, StringConcatenate, EmptyLatentImage, VAEDecode, CLIPLoader, UNETLoader, easy showAnything, PrimitiveStringMultiline, ResolutionSelector, SaveImageAdvanced, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwenimage2.1 文生图工作流_2101837000008622081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `StringConcatenate`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy showAnything`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`ResolutionSelector`、`SaveImageAdvanced`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
