---
key: 图片生成/文生图/Qwen2.1文生图_2102393926710816769.json
name: Qwen2.1文生图_2102393926710816769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_2102393926710816769.json
hash: 2b8361da1a93cd0d
coverage: 0.785714
learned_at: 2026-10-20 01:51:23
nodes: [ResolutionSelector, MarkdownNote, MarkdownNote, TextEncodeQwenImage21, EmptyLatentImage, TextGenerateLTX2Prompt, ShowText|pysssss, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, KSampler, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen2.1文生图_2102393926710816769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图_2102393926710816769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `ShowText|pysssss`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
