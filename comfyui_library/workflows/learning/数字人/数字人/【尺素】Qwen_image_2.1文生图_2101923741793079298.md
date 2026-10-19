---
key: 数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json
name: 【尺素】Qwen_image_2.1文生图_2101923741793079298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json
hash: e39a0018687fd68d
coverage: 0.846154
learned_at: 2026-10-19 00:19:16
nodes: [ResolutionSelector, Note, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, Label (rgthree), Label (rgthree), MarkdownNote, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
---

# 数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ResolutionSelector`
- `Note`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
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

覆盖率 **85%**（11/13）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`Label (rgthree)`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
