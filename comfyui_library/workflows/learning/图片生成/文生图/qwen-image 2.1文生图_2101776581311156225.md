---
key: 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json
name: qwen-image 2.1文生图_2101776581311156225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json
hash: effcdad4f255d6cb
coverage: 0.818182
learned_at: 2026-10-20 01:51:55
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, MarkdownNote, MarkdownNote, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `2`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
