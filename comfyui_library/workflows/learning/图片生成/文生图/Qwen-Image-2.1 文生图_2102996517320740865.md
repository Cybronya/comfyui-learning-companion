---
key: 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json
name: Qwen-Image-2.1 文生图_2102996517320740865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json
hash: 36c70be71b3cdeba
coverage: 0.818182
learned_at: 2026-10-10 20:59:00
nodes: [UNETLoader, SaveImage, KSampler, EmptyLatentImage, TextEncodeQwenImage21, VAEDecode, CLIPLoader, VAELoader, MarkdownNote, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 142902463237002, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json`

## 结构

**节点**（11 个）：
- `UNETLoader`
- `SaveImage`
- `KSampler`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `142902463237002`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`SaveImage`、`KSampler`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`MarkdownNote`
