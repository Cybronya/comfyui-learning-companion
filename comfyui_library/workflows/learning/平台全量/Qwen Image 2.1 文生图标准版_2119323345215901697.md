---
key: 平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json
name: Qwen Image 2.1 文生图标准版_2119323345215901697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json
hash: 29de39d5ab0cdf97
coverage: 0.818182
learned_at: 2026-11-14 00:49:57
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, MarkdownNote, MarkdownNote, ResolutionSelector, EmptyLatentImage, SaveImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 文生图标准版_2119323345215901697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
