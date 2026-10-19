---
key: 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json
name: Qwen Image 2.1 文生图 T2I_2101822255830495234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json
hash: 0fd040de0d72c752
coverage: 0.857143
learned_at: 2026-10-19 00:19:13
nodes: [MarkdownNote, MarkdownNote, TextEncodeQwenImage21, VAELoader, EmptyLatentImage, CLIPLoader, KSampler, VAEDecode, SaveImageAdvanced, SaveImage, ResolutionSelector, UNETLoader, CLIPLoader, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 842850240, "steps": 25, "width": 1024}
---

# 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `842850240`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
