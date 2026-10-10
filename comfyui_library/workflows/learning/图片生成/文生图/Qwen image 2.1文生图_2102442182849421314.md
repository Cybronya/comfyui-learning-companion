---
key: Qwen image 2.1文生图_2102442182849421314.json
name: Qwen image 2.1文生图_2102442182849421314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json
hash: 203e395ed8ffcfd6
coverage: 0.75
learned_at: 2026-10-10 20:58:57
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, KSampler, VAEDecode, EmptyLatentImage, MarkdownNote, MarkdownNote, MarkdownNote, ResolutionSelector, CLIPLoader, TextGenerateLTX2Prompt, SaveImage, 孤海注释, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 842850240, "steps": 50, "width": 1024}
---

# Qwen image 2.1文生图_2102442182849421314.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `SaveImage`
- `孤海注释`
- `Text`

## 关键参数

- `seed` = `842850240`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（12/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
