---
key: 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json
name: Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json
hash: 3c0d6da92a174bfe
coverage: 0.9
learned_at: 2026-10-10 20:58:51
nodes: [SaveImage, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, KSampler, VAEDecode, EmptyLatentImage, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 524782537916451, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步（无PE）_2106930676925812737.json`

## 结构

**节点**（10 个）：
- `SaveImage`
- `UNETLoader`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `KSampler`
- `VAEDecode`
- `EmptyLatentImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `524782537916451`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`SaveImage`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`
